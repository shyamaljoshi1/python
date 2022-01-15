# ID : 20CE038
# NAME : Joshi Shyamal Bhaveshbhai


## A.Write a Python program to add member(s) in a set and clear a set
SET = {'H', 'e', 'l', 'l', 'o'}
SET.add('!')
print("Letters are:", SET)
print("Set before clear:", SET)
print("Set after clear:", SET.clear())

## B.Write a Python program to remove an item from a set if it is present in the set.
set = {'H', 'e', 'l', 'l', 'o'}
set.remove('o')
print("Letters are:", set)

## C.Write a Python program to create an intersection, Union, difference of sets.
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("Union of A and B:", A.union(B))
print("Intersection of A and B:", A.intersection(B))
print("Difference of A and B:", A.difference(B))

## D.Write a Python program to find maximum and the minimum value in a set.
set = {1, 2, 3, 4, 5}
print(min(set))
print(max(set))

## E.Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
def intersection(A, B, C):
    s1 = set(A)
    s2 = set(B)
    s3 = set(C)
    print("List =", A)
    print("Tuple =", B)
    print("Dictionary =", C)
    set1 = s1.intersection(s2)
    result_set = set1.intersection(s3)
    final_list = list(result_set)

    print("Common of members of list, tuple and dictionary:", final_list)

if __name__== "__main__":
    list1 = [1, 2, "ABC", 3.4]
    tuple1 = (12, 20, "ABC", 3.4)
    dictionary1 = {"ABC", 1, 3.4, "PQR"}
    intersection(list1, tuple1, dictionary1)