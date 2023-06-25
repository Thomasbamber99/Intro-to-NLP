import spacy

nlp = spacy.load('en_core_web_sm')

sample = u"The old man the boat."
doc = nlp(sample)
print([(i, i.label_, i.label) for i in doc.ents])
print("\n")

sample1 = u"The horse raced past the barn fell."
doc1 = nlp(sample1)
print([(i, i.label_, i.label) for i in doc1.ents])
print("\n")

sample2 = u"The complex houses married and single soldiers and their families."
doc2 = nlp(sample2)
print([(i, i.label_, i.label) for i in doc2.ents])
print("\n")

sample3 = u"The man who hunts ducks out-on weekends."
doc3 = nlp(sample3)
print([(i, i.label_, i.label) for i in doc3.ents])
print("\n")

sample4 = u"The prime number few."
doc4 = nlp(sample4)
print([(i, i.label_, i.label) for i in doc4.ents])
print("\n")

# Splitting up the multiple sentences by the words and the sentences.
garden_path_sentences = [doc.text.split(),doc1.text.split(),doc2.text.split(),doc3.text.split(),doc4.text.split()]

[token.orth_ for token in doc]
[token.orth_ for token in doc1]
[token.orth_ for token in doc2]
[token.orth_ for token in doc3]
[token.orth_ for token in doc4]


garden_path_sentences = [doc.text.split(),doc1.text.split(),doc2.text.split(),doc3.text.split(),doc4.text.split()]

print(garden_path_sentences)
print("\n")

# Utilising token.orth_Method and Entity recognition for each of the sentences

print([(token, token.orth_, token.orth) for token in doc])
print("\n")

print([(token, token.orth_, token.orth) for token in doc1])
print("\n")

print([(token, token.orth_, token.orth) for token in doc2])
print("\n")


print([(token, token.orth_, token.orth) for token in doc3])
print("\n")


print([(token, token.orth_, token.orth) for token in doc4])
print("\n")









