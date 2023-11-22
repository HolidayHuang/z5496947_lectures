#
# less_than_test = "That" < "This"
# print(f'"That" < "This" yields {less_than_test}') # --> "That" < "This" yields True
# greater_than_test = "That" > "This"
# print(f'"That" > "This" yields {greater_than_test}') # --> "That" > "This" yields False
#
#
# a = -1
# b = True
# if a != 0:
#    print("a is non-zero")
# elif b is True:
#    print("b is True")
# elif a < 0 and b is True:
#    print("a is negative and b is True")
# else:
#    print("None of the conditions above hold") # --> a is non-zero
#
#
# # for loops
# for <variable> in <iterable>:
#     <statements>
#
# tic_base = tic.lower().split('.')[0]
#
# tic = "QAN.AX"
#
# # Convert the ticker to lower case
# tic_base = tic.lower()              # --> 'qan.ax'
#
# # Split the string into a list,
# # using '.' as a separator
# tic_base = tic_base.split('.')    # --> ['qan', 'ax']
#
# # Fetch the first element of the list
# tic_base = tic_base[0]            # --> 'qan'
#
#
#
#
#
# d = {
#     "beauty": True,
#     "truth": True,
#     "red wheelbarrow": 100000,
#     5: "fingers",
#     }
# for key in d:
#     print(key)
#
#
#
# d = {
#     "beauty": True,
#     "truth": True,
#     "red wheelbarrow": 100000,
#     5: "fingers",
#     }
# for val in d.values():
#     print(val)
#
#
#
#
# # unpacking
# d = {
#     "beauty": True,
#     "truth": True,
#     "red wheelbarrow": 100000,
#     5: "fingers",
#     }
# for key, value in d.items():
#     print(f'KEY: {key} VALUE: {value}')
#
# # KEY: beauty VALUE: True
# # KEY: truth VALUE: True
# # KEY: red wheelbarrow VALUE: 100000
# # KEY: 5 VALUE: fingers
#
#
#
# for i in range(5):
#     print("i is now {}".format(i))
# # i is now 0
# # i is now 1
# # i is now 2
# # i is now 3
# # i is now 4
#
# for even in range(0, 10, 2):
#     print("even is now {}".format(even))
# # even is now 0
# # even is now 2
# # even is now 4
# # even is now 6
# # even is now 8
#
#
# # Enumerations
#
#
# letters = ["a", "b", "c", "d", "e"]
# print(f"letters = {letters}")
# i = 0
# for x in letters:
#     print(f"letters[{i}] --> {x}")
#     i += 1
# # letters = ['a', 'b', 'c', 'd', 'e']
# # letters[0] --> a
# # letters[1] --> b
# # letters[2] --> c
# # letters[3] --> d
# # letters[4] --> e
#
#
# d = {
#     "beauty": True,
#     "truth": True,
#     "red wheelbarrow": 100000,
#     5: "fingers",
#     }
# for i, tup in enumerate(d.items()):
#     print(f'Iteration {i} gives {tup}')
# # Iteration 0 gives ('beauty', True)
# # Iteration 1 gives ('truth', True)
# # Iteration 2 gives ('red wheelbarrow', 100000)
# # Iteration 3 gives (5, 'fingers')
#
#
# # While Loops
# while <condition_is_true>:
#     <statements>
#
# the_sum = 0
# for i in range(1,101):
#    the_sum = the_sum + i
# print(the_sum) # --> 5050
#
# the_sum = 0
# i = 1
# while i <= 100:
#     the_sum = the_sum + i
#     i = i + 1
# print(the_sum) # --> 5050
#
#
# # Nested structures and conditional statements
# for outer_variable in outer_iteratable:
#     statement_a
#     statement_b
#
#     for inner_variable in inner_iteratable:
#         statement_c
#         statement_d
#         statement_e
#
#     statement_f
#     statement_g
# # Python will begin working on the outer loop. It will set the outer_variable
# # equal to the first item in outer_iteratable. Then, it executes statement_a and statement_b.
# # Next, Python does the entire inner loop.
# # It sets inner_variable equal to the first object in inner_iteratable and executes statement_c,
# # statement_d , and statement_e.
# # Then it sets inner_variable equal to the second object in inner_iteratable,
# # if it exists, and executes those same statements.
# # Once the inner loop is completed, Python finally executes statement_f and statement_g.
# # Now, Python has completed the first pass through the outer loop.
# # It sets outer_variable to the second object in outer_iteratable,
# # if it exists, and works through the code again.
#
#
# # Functions
# def func_name ( <parameter expression> ) :
#     <function body>
#
#
