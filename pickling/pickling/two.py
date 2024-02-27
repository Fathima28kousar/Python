import pickle

f1 = open('abc.xyz','rb')
data2 = pickle.load(f1)
print(data2)

f1.close()