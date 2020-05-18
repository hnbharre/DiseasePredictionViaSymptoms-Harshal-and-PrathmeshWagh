import bottle
import string
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import pandas as pd

@bottle.route('/')
def front():
	return bottle.template('sample.html')

@bottle.post('/next')
def next():
	input1=bottle.request.forms.get('symp1')
	return preprocess(input1)

@bottle.post('/preprocess')
def preprocess(sentence):
	sentence = sentence.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(sentence)
	filtered_words = [w for w in tokens if not w in stopwords.words('english')]
	l=" ".join(filtered_words).split()
	return model(l)

@bottle.post('/model')
def model(l):
	df = pd.read_csv ('OHAS Dataset.csv')
	df = pd.DataFrame(df, columns= ['Disease','Symptoms','Intensity'])
	dicts = df.to_dict('records')
	a=[]
	for i in l:
		for j in range(0,len(dicts)):
			if i == dicts[j]['Symptoms']:
				a.append(dicts[j]['Disease'])
	
	aa=set(a)
	aaa=[]
	maxx=0
	for i in aa:
		if a.count(i)>=maxx:
			aaa.append(str(str(i)+" - "+str(a.count(i))))
			maxx=a.count(i)
	
	return bottle.template('next.html',{'inputt1':aaa[::-1]})

def ab():
	bottle.debug(True)
	bottle.run(host='localhost', port=7777)
	
#--------------------------------------------
if __name__ == '__main__':
	ab()
	front()	

