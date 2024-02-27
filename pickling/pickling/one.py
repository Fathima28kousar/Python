import pickle

data = ['fathima',20.5,2,True]
f = open('abc.xyz','wb')
pickle.dump(data,f)
f.close

