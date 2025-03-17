import spacy
import json
from extractor import Extractor
from flask import Flask, request, jsonify
from flask_cors import CORS

'''
nlp = spacy.load('en_core_web_sm')

def run():
    text = "John (Customer): I would like to use Sentry to track health of new releases"
    keywords = extract_keywords(text)
    print(keywords)

def extract_keywords(text):
    doc = nlp(text)
    keywords = [chunk.text for chunk in doc.noun_chunks]
    return keywords
'''


app = Flask(__name__)
CORS(app)

@app.route('/health')
def check_health():
    return "server is healthy"

@app.route('/parse', methods=["POST"])
def parse_context():
    data = request.get_json()
    extractor = Extractor()
    entities = extractor.extract_entities(data)
    configurations = extractor.map_entities_to_configurations(entities)
    print("relevant configs: ", configurations)
    return jsonify({'status': 200, 'data': {'configurations' : configurations}})



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True) 
    '''   
    nlp = spacy.load("custom_ner_model")

    # Function to process and extract entities from text
    def extract_entities(text):
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities

    # Function to map extracted entities to relevant configurations
    def map_entities_to_configurations(entities, config_map):
        relevant_configs = []
        keyword_endpoints = config_map["keywords"]
        print(keyword_endpoints)
        print(entities)
        for entity_text, entity_label in entities:
            if entity_label in config_map:
                print(entity_label)
                relevant_configs.extend(keyword_endpoints[entity_label])
        return relevant_configs

    # Example customer conversation
    conversation = "John (Customer): I would like to use Sentry to track health of new releases"

    # Extract entities from the conversation
    entities = extract_entities(conversation)
    print("Extracted Entities:", entities)

    # Example configuration map (similar to your config_map.json)

    with open('config_map.json', 'r') as file:
        config_map = json.load(file)

    # Map extracted entities to relevant configurations
    relevant_configurations = map_entities_to_configurations(entities, config_map)
    #print("Relevant Configurations:", relevant_configurations)
    '''