# Intro-to-NLP

Instructions
_____________

To be able to run this file you need to install SpaCy, the Python NLP Library.
For users who have Python, version 3.11.0 installed, type the following commands into your code editors terminal.

py -m pip install spacy

py -m spacy download en_core_web_sm

py
import spacy

nlp = spacy.load('en_core_web_sm')

doc = nlp('this is a test')
print([(w.text, w.pos_) for w in doc])

if you have installed SpaCy correctly it should output the following back to you:
[('this', 'PRON'), ('is', 'AUX'), ('a', 'DET'), ('test', 'NOUN')]

