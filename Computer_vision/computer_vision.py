from flask import Flask, request, jsonify
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

app = Flask(__name__)

# Replace with your own Azure Cognitive Services values
ENDPOINT = 'https://image-analyze-01.cognitiveservices.azure.com/'
KEY = 'fe666acf8276407b80d13eb6b5352c8d'

@app.route('/analyze', methods=['POST'])
def analyze_image():
    url = request.json['url']
    
    client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))
    
    # Analyze the image
    image_analysis = client.analyze_image(url, visual_features=[VisualFeatureTypes.description])
    
    # Extract the image description
    image_description = image_analysis.description.captions[0].text
    
    return jsonify({'description': image_description})

if __name__ == '__main__':
    app.run()


#use following url in postman
# #{
#   "url": "https://images.pexels.com/photos/6681965/pexels-photo-6681965.jpeg"
# }


# {
#   "url": "https://www.india.com/wp-content/uploads/2015/01/obama22.jpg"
# }

# {
#   "url": "https://www.icccricketschedule.com/wp-content/uploads/2023/05/Virat-Kohli-Ind_11zon.jpg"
# }



