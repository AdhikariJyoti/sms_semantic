import spacy

nlp = spacy.load('en_core_web_sm')
text = "Dear Customer, Your 110##01978 has been withdrawn by NPR 98.00 on 28/08/22 21:00:32, Remarks: MPAY 9861168873 " \
       "Activate bit.ly/2U2dzlO for a/c balance "
doc = nlp(text)
tokens = [token.text for token in doc]
for token in doc:
    print("Tokens are:", token, token.idx)
sentences = list(doc.sents)
len(sentences)
for sentence in sentences:
    print("sentence detection", sentence)
for token in doc:
    if not token.is_stop:
        print("Tokens after removing stop words", token)
for token in doc:
    print("Token after lemmentization", token, token.lemma_)

print("token list", tokens)
