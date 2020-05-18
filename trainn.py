import pandas as pd
l=["cold","fever"]
df = pd.read_csv ('OHAS Dataset.csv')
df = pd.DataFrame(df, columns= ['Disease','Symptoms','Intensity'])
dicts = df.to_dict('records')
a=[]
for i in l:
	for j in range(0,len(dicts)):
		if i == dicts[j]['Symptoms']:
			a.append(dicts[j]['Disease'])
# print (a)
aa=set(a)
aaa=[]
maxx=0
for i in aa:
	if a.count(i)>=maxx:
		aaa.append([i,a.count(i)])
		maxx=a.count(i)
print(aaa[::-1])

