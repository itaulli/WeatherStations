import pickle

with open('weather.pkl', 'rb') as file:
    datalist = pickle.load(file)

for i in range(len(datalist)):
    print(datalist[i])