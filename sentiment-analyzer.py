
#Opening the files and storing it in a variable lines
with open("./netflix.txt", "r") as text_file:
    lines = text_file.read().split('\n')

with open("./hbo.txt", "r") as text_file:
    lines = text_file.read().split('\n')


#Text Processing data
lines = [line.split("\t") for line in lines if len(line.split("\t"))==2 and line.split("\t")]

#Storing only reviews text into variable train_documents
train_documents = [line[0] for line in lines]


#Storing only review labels into variable train_labels
train_labels = [int(line[1]) for line in lines]


#Importing CountVectorizer from Sklearn
from sklearn.feature_extraction.text import CountVectorizer
count_vectorizer = CountVectorizer(binary='true')
train_documents = count_vectorizer.fit_transform(train_documents)

#Training
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier

#classifier = GaussianNB().fit(train_documents,train_labels)
#classifier = BernoulliNB().fit(train_documents,train_labels)
classifier = RandomForestClassifier(max_depth=2, random_state=0).fit(train_documents, train_labels)


#Testing
global counter
counter = 0

def pred ():
   global counter
   inputtext =  input('Write a review: ')
   prediction = classifier.predict(count_vectorizer.transform([inputtext]))

   if prediction == 1:
    print('Its a positive review')
   else:
    print('Its a negetive review')

   more_reviews = input('Would you like to see more reviews(Y/N): ')

   if more_reviews == "Y":
        counter = 0
   elif more_reviews == "N":
        counter = 1
   else:
        counter = 1

while counter == 0:
                pred()



