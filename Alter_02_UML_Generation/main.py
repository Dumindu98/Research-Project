import spacy
from tokenization import *
from generate_class_diagram import *
from generate_use_case_diagram import *
from generate_activity_diagram import gen_activity_diagram
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOADS_FOLDER = os.path.join(APP_ROOT, 'uploads')

def remove_unwanted_values(data):
    remove_element = 'None'
    if remove_element in data:
        data.pop(data.index(remove_element))
    return data

def remove_duplicates(data):
    return list(set(data))

def remove_punctuation(sentence):
    text_no_punct = [token for token in sentence if not token.is_punct]
    cleaned_sentence = ' '.join(token.text for token in text_no_punct)
    return cleaned_sentence

# load the text file
def main(filepath):
    with open(UPLOADS_FOLDER+"/"+filepath, "r",errors='ignore') as f:
        requirement_text = f.read().replace("\n\n"," ").replace("\n"," ")
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(requirement_text)

# sentence splitting
    sentences = list(doc.sents)
    nc = []
    cleaned_extracted_actions = []
    cleaned_sentences = []
    splitted_actions_array = []

# looping 4 arrays
    for sentence in sentences:
        res = get_nouns_pnouns(sentence)
        nc.append(str(res))
        cleaned_sentence = remove_punctuation(sentence)
        cleaned_sentences.append(cleaned_sentence)

        splitted_actions = split_actions(str(cleaned_sentence))
        splitted_actions_array.append(splitted_actions)

        extracted_actions = get_actions(splitted_actions)
        if extracted_actions is not None:
            cleaned_extracted_actions.append(extracted_actions)

# remove duplicates of the actors
    nc = list(dict.fromkeys(nc))
    data = remove_unwanted_values(nc)

    generated_class_diagram_path = generate_class(data,cleaned_extracted_actions)

# usecase
    extracted_relationships = get_include_extend_relationships(splitted_actions_array)
    actors_and_use_cases_array = identify_use_cases(cleaned_extracted_actions)
    generated_usecase_diagram_path = generate_use_case_diagram(data,extracted_relationships,actors_and_use_cases_array)
    generated_activity_diagram_path = gen_activity_diagram(data,extracted_relationships,actors_and_use_cases_array)
    return generated_class_diagram_path,generated_usecase_diagram_path,generated_activity_diagram_path