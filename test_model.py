from extractor import Extractor

prompt = "I care about environments"
extractor = Extractor()
entities = extractor.extract_entities(prompt)
configurations = extractor.map_entities_to_configurations(entities)
print("relevant configs: ", configurations)