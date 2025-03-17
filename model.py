import spacy
from spacy.training import Example
from spacy.training import offsets_to_biluo_tags
from train_data import TRAIN_DATA
import random

# Initialize the blank model and add the NER pipeline
nlp = spacy.blank("en")
ner = nlp.add_pipe("ner")

# Add labels based on the entities in the training data
for _, annotations in TRAIN_DATA:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])


# Function to verify and correct offsets
def verify_and_correct_offsets(nlp, text, entities):
    doc = nlp.make_doc(text)
    biluo_tags = offsets_to_biluo_tags(doc, entities)
    for i, tag in enumerate(biluo_tags):
        if tag == "-":
            print(f"Misaligned entity found in text: '{text}' with entities: {entities}")
            return False
    return True


# Train the model

optimizer = nlp.begin_training()
for i in range(20):
    random.shuffle(TRAIN_DATA)
    losses = {}
    for text, annotations in TRAIN_DATA:
        if not verify_and_correct_offsets(nlp, text, annotations["entities"]):
            print(f"Error in text: '{text}' with entities: {annotations['entities']}")
        example = Example.from_dict(nlp.make_doc(text), annotations)
        nlp.update([example], drop=0.5, losses=losses)
    print(f"Iteration {i}: {losses}")

# Save the trained model
nlp.to_disk("custom_ner_model")


# Test the trained model
'''
nlp = spacy.load("custom_ner_model")
doc = nlp("The customer wants to monitor releases closely")
for ent in doc.ents:
    print(ent.text, ent.label_)
    '''
