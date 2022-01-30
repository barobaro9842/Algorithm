X = [1,2,3,4,4,7,7,8,9,10]

Y = []    
for x in X :
    Y.append(x % 42)
    

dic = {i : 0 for i in X}
print(len(dic))
print(dic)