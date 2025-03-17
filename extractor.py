import spacy
import json


class Extractor:

    def __init__(self):
        self.nlp = spacy.load("custom_ner_model")

    # Function to process and extract entities from text
    def extract_entities(self, text):
        doc = self.nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities
    
    def map_entities_to_configurations(self, entities):
        with open('config_map.json', 'r') as file:
            config_map = json.load(file)

        relevant_configs = []
        keyword_endpoints = config_map["keywords"]
        print(entities)
        for entity_text, entity_label in entities:
            print(entity_label)
            if entity_label in keyword_endpoints:
                #print(entity_label)
                relevant_configs.extend(keyword_endpoints[entity_label])
        return relevant_configs
