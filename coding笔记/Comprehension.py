
# Dictionary comprehensions
pairs = [
  ('a', 1),
  ('b', 2),
  ('c', 3),
  ]
# This WILL work
dic = {key:value for key, value in pairs}
print(dic) # --> {'a': 1, 'b': 2, 'c': 3}




# List comprehensions
# Start with a dictionary
dic = {'a': 1, 'b': 2, 'c': 3}

# Create a list of (key, val) using list comprehensions:
pairs = [(key,value) for key,value in dic.items( )]

print(pairs) # --> [('a', 1), ('b', 2), ('c', 3)]




# Set comprehensions
# Create a list with all even integers from 0 to 1 million
evens = [x for x in range(1_000_000 + 1) if x % 2 == 0]
print(evens[:10])  # --> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]



# Some data (list of tuples)
data = [
  ('a', 1),
  ('b', 2),
  ('c', 3),
  ]

# Create a dict comprehension
dic = {k:v for k, v in data}
print(f'`dic` is {dic}')
print(f'type(dic) is: {type(dic)}')
# --> `dic` is {'a': 1, 'b': 2, 'c': 3}
# type(dic) is: <class 'dict'>

# Create a list comprehension
lst = [(k, v) for k, v in data]
print(f'`lst` is {lst}')
print(f'type(lst) is {type(lst)}')
# --> `lst` is [('a', 1), ('b', 2), ('c', 3)]
# type(lst) is <class 'list'>

# Create a set comprehension
st = {k for k, v in data}
print(f'`st` is {st}')
print(f'type(st) is {type(st)}')
# --> `st` is {'a', 'c', 'b'}
# type(st) is <class 'set'>