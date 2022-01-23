""" Student ID: 20CS048
    Student Name : DISHA PATEL 
"""

#Python program to add member(s) in a set and clear a set
Colours = {'Blue','Black','White','Pink','Green',}
print(Colours)
Colours.add('Yellow')
print(Colours)
#Fun to clear the set.
Colours.clear()


#Python program to remove an item from a set if it is present in the set.
Birds = {'Sparrow', 'Crow', 'Peacock','Parrot','Pigeon'}
print(Birds)
#fun will remove the mentioned item.
Birds.remove('Crow')
print(Birds)


#Python program to create an intersection, Union, difference of sets.
Set1 ={1, 2 , 3 , 4 , 5}
Set2 = {4 , 5 , 6 ,7 ,8}
#OR operator is used for union.
print(Set1 | Set2)
#AND operator is used for intersection.
print(Set1 & Set2)
#(-) is used for difference.
print(Set1 - Set2)


#Python program to find maximum and the minimum value in a set.
Numbers = {12, 15 , 25, 56, 89}
print(Numbers)
print(max(Numbers))
print(min(Numbers))


#Python program to find the most common elements and their counts from list.
Lst = {1, 2, 3, 2, 4, 5}
def most_frequent(Lst) :
    print(most_frequent(Lst))
