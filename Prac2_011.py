""" Student ID: 20CS048
    Student Name : DISHA PATEL 
"""
#Python script to check whether a given key already exists in a dictionary.
#Dictionary name is Student and keys are ID, Age etc.
Student = {
    'ID' : '20cc048',
    'first_Name' : 'Disha',
    'last_Name' : 'Patel',
    'Age' : 19,
    'Gender' : 'Female',
    'skills' : ['Python', 'CSS', 'Django']
}
#It will print the dictionary alaong with keys.
print(Student)

#Using this fun to check whether the entered key is present or not.
def is_key_present(x):
    if x in Student:
        print('Key is present')
    else:
        print('Key is not present')
is_key_present('ID') 
is_key_present('Skills') 

# Python script to merge two Python dictionaries.
#Dictionary named Marks1.
Marks1 = { 
    'Disha': 98,
    'Harsh' : 99,
    'Drashti' : 98,
    'Mohit': 99,
    'Anuj' : 98
} 
#Dictionary named Marks2.
Marks2 = { 
    'Harshiv': 98,
    'Dev' : 99,
    'Darsh' : 98,
    'Khushi': 99,
    'Shubhangi' : 98
} 
#It will print Original individual dict.
print("Original dictionaries:")
print(Marks1)
print(Marks2)
#After merging it will print dict.
print("\nmerge dictionaries : ")
#OR operator is used to merge the dict.
print(Marks1 | Marks2)

# Python program to sum all the items in a dictionary.
Data = {
    'data1' : 100,
    'data2' : 200,
    'data3' : 200,
    'data4' : 100,
    'data5' : 100
}
print(Data)
#It will sum the values od the keys and print it.
print(sum(Data.values()))

# Python script to add a key to a dictionary.
Student['skills'].append('C')
#After adding the particular key it will print the dict.
print(Student)

#Python script to concatenate following dictionaries to create a new one.
Dict1 = {
    'One' : 10,
    'Two': 20,
    'Three' : 30
}
Dict2 = {
    'Four': 40,
    'Five': 50,
    'Six': 60
}
Dict3 = {
    'Seven' : 70,
    'Eight': 80,
    'Nine': 90
}
#It will concatenate the above dictionaries and display it in Dict4.
Dict4 = {}
for d in (Dict1, Dict2,Dict3) : Dict4.update(d)
print(Dict4)


