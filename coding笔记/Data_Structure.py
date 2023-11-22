
### list
# lst = [1, 2, 3]
# print(lst) # --> [1, 2, 3]
#
# t = type(lst) # --> <class 'list'>
# print(t)

# lst = [1, 2, 3]
# lst = list([1,2,3])


# lst = [1, "string", True, None]
# print(f"The item at index 0 is {lst[0]}")
# print(f"The item at index 1 is {lst[1]}")
# print(f"The item at index 2 is {lst[2]}")
# print(f"The item at index 3 is {lst[3]}")

# lst = ["a", "b", "c", "d", "e", "f"]
# print(f"The slice from index 1 through 4 is {lst[1:4]}" )
# # --> The slice from index 1 through 4 is ['b', 'c', 'd']
# print(f"The slice from index -5 through -2 is {lst[-5:-2]}" )
# # --> The slice from index -5 through -2 is ['b', 'c', 'd']


# lst_a = [1]       # lst_a is [1]
# lst_a.append(2)   # lst_a is now [1, 2]
# print(lst_a)


# lst_a = [1]
# lst_b = [2, 3]
# lst_a.extend(lst_b) # --> lst_a now is [1, 2, 3]
# print(lst_a)
#
# lst_a = [1]
# lst_b = [2, 3]
# lst_a.append(lst_b) # --> lst_a now is [1, [2, 3] ]
# print(lst_a)


# lst = [1, True, None]
# print(f"lst is originally {lst}" )  # lst is originally [1, True, None]
# lst.insert(1, "string")       # lst is now [1, "string", True, None]
# print(f"After insertion, lst is now {lst}")
# insert(i, x) --> i indicates the element location; the new object x to be inserted



### tuple
# # Create a tuple with two elements
# tup = (1, 2)
#
# # unpack the tuple into two variables:
# (a, b) = tup
#
# # print
# print(f"`a` is {a} and `b` is {b}")



### set
# s = set()
# s.add("QAN.AX")   # s is {"QAN.AX"}
# s.add("WES.AX")   # s is {"QAN.AX", "WES.AX"}
# s.add("CBA.AX")   # s is {"QAN.AX", "WES.AX", "CBA.AX"}
# s.add("CBA.AX")   # s is {"QAN.AX", "WES.AX", "CBA.AX"} (so no change)
#
# print(f"After adding objects, s is {s}")
#
# s.remove("CBA.AX") # s is {"QAN.AX", "WES.AX"}
# print(f"After removing 'CBA.AX', s is {s}")