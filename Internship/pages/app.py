from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

'''
Authenticate
Authenticates your credentials and creates a client.
'''
subscription_key = "bcb8fd1cbd5445028d2e80d85abc5c8f"
endpoint = "https://computervisionfinalproject.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(
    endpoint, CognitiveServicesCredentials(subscription_key))
'''
END - Authenticate
'''

'''
OCR: Read File using the Read API, extract text - remote
This example will extract text in an image, then print results, line by line.
This API call can also extract handwriting style text (not shown).
'''
print("===== Read File - remote =====")
# Get an image with text

read_image_url = "https://i.pinimg.com/originals/ed/85/30/ed85308eca8abc97d6a3baeb1f6899e7.jpg"
#read_image_url = "https://static01.nyt.com/images/2018/06/19/business/00wheels-digitalplates2-alpha/00wheels-digitalplates2-alpha-superJumbo-v2.jpg"
#read_image_url = "http://img03.platesmania.com/171027/m/10589649.jpg"
# Call API with URL and raw response (allows you to get the operation location)
read_response = computervision_client.read(
    read_image_url ,  raw=True, model_version="2022-04-30")

# Get the operation location (URL with an ID at the end) from the response
read_operation_location = read_response.headers["Operation-Location"]
# Grab the ID from the URL
operation_id = read_operation_location.split("/")[-1]

# Call the "GET" API and wait for it to retrieve the results
while True:
    read_result = computervision_client.get_read_result(operation_id)
    if read_result.status not in ['notStarted', 'running']:
        break
    time.sleep(1)

# Print the detected text, line by line
if read_result.status == OperationStatusCodes.succeeded:
    for text_result in read_result.analyze_result.read_results:
        for line in text_result.lines:
            print(line.text)
print()
'''
END - Read File - remote
'''

print("End of Computer Vision quickstart.")
