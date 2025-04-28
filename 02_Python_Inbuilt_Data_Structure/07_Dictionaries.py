# -*- coding: utf-8 -*
'''
Dictionaries
-stores data in key-value pair
-unordered
-unindexable
-access the value, with help of keys
'''
user_info = {
    "Name": "Yash",
    "Age": 19,
    "Nationality": "Indian"
}
print(user_info)
#o/p-{'Name': 'Mayuri', 'Age': 19, 'Nationality': 'Indian'}

type(user_info)
#o/p-dict

# accessing element in dictionary
print(user_info['Name'])
print(user_info['Nationality'])
#o/p-Mayuri
#o/p-Indian

# unknow key gives error
print(user_info['Hobby'])
#KeyError: 'Hobby'

# no error
user_info.get('Hobby')

# add data in dictionary
user_info['Hobby'] = ["Cricket", "Coding", "Movie"]
print(user_info)
#o/p-{'Name': 'Mayuri', 'Age': 19, 'Nationality': 'Indian', 'Hobby': ['Cricket', 'Coding', 'Movie']}

# display all keys
user_info.keys()
#o/p-dict_keys(['Name', 'Age', 'Nationality', 'Hobby'])

# display all values
user_info.values()
#o/p-dict_values(['Mayuri', 19, 'Indian', ['Cricket', 'Coding', 'Movie']])

# display (key, value) pair in tuples
user_info.items()
#o/p-dict_items([('Name', 'Mayuri'), ('Age', 19), ('Nationality', 'Indian'), ('Hobby', ['Cricket', 'Coding', 'Movie'])])

for k,v in user_info.items():
    print(k, ":", v)
'''
o/p-
Name : Mayuri
Age : 19
Nationality : Indian
Hobby : ['Cricket', 'Coding', 'Movie']
'''
# delete key, value
user_info.pop('Hobby')
['Cricket', 'Coding', 'Movie']
print(user_info)
#o/p-{'Name': 'Mayuri', 'Age': 19, 'Nationality': 'Indian'}

user_info['Name'] = 'Mayuri D'
print(user_info)
#o/p-{'Name': 'Mayuri D', 'Age': 19, 'Nationality': 'Indian'}

user_info = {
    "Name": "Yash",
    "Age": 19,
    "Nationality": "Indian"
}
print(user_info)
#o/p-{'Name': 'Mayuri', 'Age': 19, 'Nationality': 'Indian'}
 