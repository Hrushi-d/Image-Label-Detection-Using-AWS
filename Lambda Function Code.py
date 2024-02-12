import json
import boto3
import logging
import base64
from io import BytesIO
from PIL import Image

# Initialize AWS Rekognition client
rekognition = boto3.client('rekognition')

# Set the Logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    # Get the image from the API Gateway event
    logger.info("Get the Event")
    try:
        # Assuming the image data is base64-encoded in the request body
        logger.info(f"Got the Event: {event}")

        # Decode the Image Binary
        decoded_data = base64.b64decode(event['body'])

        # Process the Image
        image = Image.open(BytesIO(decoded_data))
        stream = BytesIO()
        image.save(stream, format="JPEG")
        image_binary = stream.getvalue()

        # Perform object detection
        logger.info("Detecting the Labels....")

        # Call AWS Rekognition to detect labels in the image
        response = rekognition.detect_labels(
            Image={
                'Bytes': image_binary
            },
            MaxLabels=15,  # Maximum number of labels to return
            MinConfidence=70  # Minimum confidence level required for a label to be returned
        )

        # Extract only labels and confidence from the response
        labels_info = [
            {
                'Label': label_info['Name'],  # Extracting label name
                'Confidence': label_info['Confidence']  # Extracting confidence score
            }
            for label_info in response['Labels']  # Iterate over each label detected
        ]

        # Return the labels and their confidence scores
        return {
            'statusCode': 200,
            'body': json.dumps(labels_info)
        }
    except Exception as e:
        # Log any exceptions that occur
        logger.info(e)
        return {
            'statusCode': 500,
            'body': json.dumps(f"Failed because of: {e}")
        }
