**Step 1: Create an AWS Lambda Function**

1. **Navigate to Lambda Console**: Sign in to your AWS Management Console and navigate to the Lambda service.

2. **Create Function**:
   - Click on the "Create function" button.
   - Choose the "Author from scratch" option.

3. **Configure Function**:
   - **Function name**: `imageLabelDetectionFunction`
   - **Runtime**: Python 3.10
   - **Execution role**: Create a new role with basic Lambda permissions.

4. **Create Function**:
   - Click on "Create function" to create your Lambda function.

**Step 2: Configure Lambda Function**

1. **Replace Default Code**:
   - Replace the default code in the Lambda function editor with [Lambda Function Code]([https://github.com/keithrozario/Klayers](https://github.com/Hrushi-d/Image-Label-Detection-Using-AWS/blob/main/Lambda%20Function%20Code.py))

2. **Permissions**:
   - Ensure that the Lambda function's execution role has appropriate permissions to access AWS Rekognition. You may need to attach a policy like `AmazonRekognitionFullAccess` to the execution role.

**Step 3: Adjust Lambda Function Settings (Optional)**

1. **Set Timeout and Memory**:
   - If necessary, adjust the function timeout and memory settings under the "Configuration" tab. For this application, a timeout of 1 minute and memory of 256 MB should suffice.

**Step 4: Add Lambda Layer**

1. **Add a Lambda Layer**:
   - Lambda layers allow you to include additional libraries and dependencies in your Lambda functions without increasing the package size.
   - Since we're using the Pillow library for image processing, we need to add a Lambda layer that includes this library.
   - Visit the [Klayers repository](https://github.com/keithrozario/Klayers) and find the appropriate layer for Pillow and Python 3.10 in the region where your Lambda function is running.
   - Once you find the correct ARN for the Pillow layer for Python 3.10 in the region, add it to your Lambda function.

**Step 5: Create API Gateway**

1. **Navigate to API Gateway Console**:
   - Go to the API Gateway service in the AWS Management Console.

2. **Create API**:
   - Click on "Create API" and choose the "HTTP API" type.

3. **Create Resource and Method**:
   - Create a resource named `/detection`.
   - Create a POST method under this resource.

4. **Integration**:
   - Choose "Lambda Function" as the integration type.
   - Select the Lambda function `imageLabelDetectionFunction` created earlier.

5. **Enable Lambda Proxy Integration**:
   - Enable the Lambda proxy integration to pass the entire request to the Lambda function.

**Step 6: Configure API Gateway**

1. **Binary Media Type**:
   - In the API Gateway settings, add `image/*` as a binary media type. This ensures that the API Gateway can handle binary image data.

**Step 7: Deploy API**

1. **Deploy API**:
   - Deploy your API to a stage (e.g., "prod").
   - Copy the URL of the deployed API endpoint.

**Step 8: Testing**

1. **Send Test Request**:
   - Use Postman or any other HTTP client to send a POST request to the API endpoint.
   - Include a custom image as binary data in the request body.
   - Ensure that the request body contains base64-encoded image data.
   - Verify that the response contains the detected labels and their confidence scores.

**Services Used:**
1. AWS Lambda
2. AWS Rekognition
3. API Gateway

**Contact Us 📧**

Have questions, feedback, or need assistance? Reach out to:

Email: hrushikeshdagwar@gmail.com
