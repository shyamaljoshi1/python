# ID : 20CE038
# NAME : Joshi Shyamal Bhaveshbhai


## A.Write a Python script to check whether a given key already exists in a dictionary.
dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
key1 = 'A'
key2 = 'G'
if key1 in dic:
    print(dic[key1], "is present in the dictionary")
else:
    print("Key is not present in the dictionary")
if key2 in dic:
    print(dic[key2], "is present in the dictionary")
else:
    print("Key is not present in the dictionary")

## B.Write a Python script to merge two Python dictionaries.
dic1 = {'a': 100, 'b': 200}
dic2 = {'x': 300, 'y': 200}
dic = dic1.copy()
dic.update(dic2)
print(dic)

## C.Write a Python program to sum all the items in a dictionary.
dic = {'a': 100, 'b': 200}
print("Total Sum of values in the dictionary:", sum(dic.values()))

## D.Write a Python script to add a key to a dictionary.
##Sample Dictionary : {0: 10, 1: 20}
##Expected Result : {0: 10, 1: 20, 2: 30}
dic = {'0': 10, '1': 20}
dic.update({'2': 30})
print(dic)

## E. Write a Python script to concatenate following dictionaries to create a new one.
##Sample Dictionary :
##dic1={1:10, 2:20}
##dic2={3:30, 4:40}
##dic3={5:50,6:60}
##Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)
print(dic4)