import time
import numpy as np
from scipy.spatial import distance
import boto3
import cv2
from credentials import access_key, secret_key, region_name

color_threshold = 30
detected_colors_hex = []

rekognition_client = boto3.client('rekognition',
                                aws_access_key_id=access_key,
                                aws_secret_access_key=secret_key,
                                region_name=region_name)
targetClass = 'Car'

def get_dominant_color(image):
    """Get the dominant color of the image."""
    pixels = np.float32(image.reshape(-1, 3))
    n_colors = 5
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    _, counts = np.unique(labels, return_counts=True)
    dominant_color = palette[np.argmax(counts)].astype(int)
    return tuple(dominant_color)

def is_new_color(dominant_color, detected_colors, threshold):
    """Check if the color is new by comparing it to detected colors."""
    for color in detected_colors:
        if distance.euclidean(dominant_color, color) < threshold:
            return False
    return True

def rgb_to_hex(rgb_color):
    """Convert an RGB color to HEX format."""
    return '{:02x}{:02x}{:02x}'.format(rgb_color[2], rgb_color[1], rgb_color[0])

def DetectionAndDisplay(Camera):
    """Detect and display cars in a video stream using AWS Rekognition and OpenCV."""
    global detected_colors_hex

    videocapture = cv2.VideoCapture(Camera)
    if not videocapture.isOpened():
        print("ERROR: COULD NOT OPEN VIDEO SOURCE")
        return
    detected_colors = []

    try:
        frame_skip = 5  # Number of frames to skip
        frame_count = 0

        while True:
            ret, frame = videocapture.read()
            if not ret:
                print("ERROR: COULD NOT READ FRAME")
                break        
            frame_count += 1
            if frame_count % frame_skip != 0:
                continue

            H, W, _ = frame.shape
            _, buffer = cv2.imencode('.jpg', frame)
            images_bytes = buffer.tobytes()

            try:
                response = rekognition_client.detect_labels(Image={'Bytes': images_bytes}, MinConfidence=50)
            except Exception as e:
                print(f"ERROR: AWS Rekognition failed - {e}")
                continue

            for label in response['Labels']:
                if label['Name'] == targetClass:
                    for instance_nmr in range(len(label['Instances'])):
                        bbox = label['Instances'][instance_nmr]['BoundingBox']
                        x1 = int(bbox['Left'] * W)
                        y1 = int(bbox['Top'] * H)
                        width = int(bbox['Width'] * W)
                        height = int(bbox['Height'] * H)

                        car_detected = frame[y1:y1 + height, x1:x1 + width]
                        if car_detected.size != 0:
                            dominant_color = get_dominant_color(car_detected)
                            if is_new_color(dominant_color, detected_colors, color_threshold):
                                detected_colors.append(dominant_color)

                        cv2.rectangle(frame, (x1, y1), (x1 + width, y1 + height), (0, 255, 0), 3)

            detected_colors_hex = [rgb_to_hex(color) for color in detected_colors]
            _, jpg = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + jpg.tobytes() + b'\r\n')

            time.sleep(0.5)  # Add a small delay to control the frame rate
    finally:
        videocapture.release()
