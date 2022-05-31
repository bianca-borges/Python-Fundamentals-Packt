my_friends = ['Andre', 'Nataly', 'Suely']
your_friends = ['Lucas', 'Mario', 'Luigi']

my_friends += your_friends
people = list(my_friends)
my_friends[4] = 'Jane'
print(my_friends)
print(people)