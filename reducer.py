import pickle

file= open('shuffled.pkl','rb')
shuffled = pickle.load(file)

def reduce(shuffled_dict):
    reduced = {}
    
    for i in shuffled_dict: 
        
        reduced[i] = sum(shuffled_dict[i])/len(shuffled_dict[i])
    
    return reduced

final = reduce(shuffled)

print("Средняя летучая кислотность в разных сортах вина: ")
for i in final:

	print(i,':',final[i])