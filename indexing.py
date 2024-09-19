#-------------------------------------------------------------------------
# AUTHOR: Justin Ha
# FILENAME: indexing.py
# SPECIFICATION: Read a .csv file simulating the contents of documents. Calculate the document-term matrix and print to console
# FOR: CS 4250- Assignment #1
# TIME SPENT: 4 hours
#-----------------------------------------------------------*/

#Importing some Python libraries
import csv
import math

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])

#Conducting stopword removal for pronouns/conjunctions. Hint: use a set to define your stopwords.
#--> add your Python code here
stopWords = { "I", "and", "She", "her", "They", "their" }
for i, doc in enumerate(documents):
    words = doc.split()
    for word in words:
        if(word in stopWords):
            documents[i] = documents[i].replace(word, "")

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
stemming = {
    "cats" : "cat",
    "loves" : "love",
    "dogs" : "dog"
}
for i, doc in enumerate(documents):
    words = doc.split()
    for word in words:
        if(word in stemming):
            documents[i] = documents[i].replace(word, stemming.get(word))

#Identifying the index terms.
#--> add your Python code here
terms = []
for doc in documents:
    words = doc.split()
    for word in words:
        if(word not in terms):
            terms.append(word)

#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here
docTermMatrix = []
NUM_DOCUMENTS = len(documents)
#Calculate idf value for each term
idfs = {}
for term in terms:
    count = 0
    for doc in documents:
        docTerms = doc.split()
        if(term in docTerms):
            count += 1
    idf = math.log(NUM_DOCUMENTS / count, 10)
    idfs[term] = idf

#Calculate tf-idf values by document
for doc in documents:
    docTerms = doc.split()
    NUM_DOC_TERMS = len(docTerms)
    row = []
    for term in terms:
        tf = docTerms.count(term) / NUM_DOC_TERMS
        tf_idf = tf * idfs[term]
        row.append(tf_idf)
    docTermMatrix.append(row)

#Printing the document-term matrix.
#--> add your Python code here
print("Document-Term Matrix")
#Prints each term to label its respective column. Scalable if more terms are read from documents
print("   |", end="")
for term in terms:
    print(f" {term:<4s} |", end="")
print()
#Prints each row including the document label and its respective tf-idf values per term column
#Scalable if more or less terms are found
#Column width will scale based on term character length
for i, row in enumerate(docTermMatrix):
    print(f"d{i+1} |", end="")
    for j, col in enumerate(row):
        print(f" {col:<{len(terms[j])}.2f} |", end="")
    print()