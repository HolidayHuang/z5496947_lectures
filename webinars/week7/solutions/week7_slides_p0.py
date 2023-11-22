""" week7_slides_p0.py

Topic: Review of Assignment Statements, Objects, and Variables

Scaffold (and solutions) with the examples discussed during the review portion
of the class in week 7 


Notes
-----

Solutions can be identified by the tag <solution>. Simply un-comment the
statements inside the tagged blocks. For example:

    Before:

    # <solution>
    #res = ser.loc[start:end]
    # </solution>

    After:

    # <solution>
    res = ser.loc[start:end]
    # </solution>

Examples are identified by the tag <example>. To see a particular example,
simply uncomment the statements inside the tagged block:

    Before:

    # <example>
    #res = df.loc[clabel] # -> KeyError ('close' is not part of df.index)
    # </example>

    After:

    # <example>
    res = df.loc[clabel] # -> KeyError ('close' is not part of df.index)
    # </example>

"""
# NOTE:
# We will discuss the module copy later in this code.
# 
    import copy

import pprint as pp

def printit(obj, msg):
    """ Pretty printer. Print both the object `obj`, its type, and the object
    ID

    Parameters
    ----------
    obj: Any instance

    msg: str, optional
        An optional message

    """
    sep = '-' * 30
    to_print = [
        sep,
        msg,
        '',
        pp.pformat(obj),
        '',
        f"Type: {type(obj)}",
        f"Object Address: {id(obj)}",
        sep,
        ]
    print('\n'.join(to_print))



def example1():
    """ Example illustrating assignment statements of the form 

        <target> = <expression>

    where `<target>` is a (variable) name 

    This will assign the object generated by the expression to the target

    """

    # Create a list instance and assign the object to the name `lst0`
    lst0 = [1, 2]

    # Intuition for the statement above:
    # 1. is "lst0" a valid name for a variable? Yes
    # 2. Evaluate the expression [1, 2]
    #    - The result will be an instance of the "list" type with elements
    #      1 and 2. This instance is stored somewhere in the computer memory
    # 3. Assign the object created to the target. In this case, it's the
    #    variable "lst0". 
    # 
    # As long as the variable "lst0" is not reassigned (or rebound), it will
    # serve as an alias for the object created in step 2. Intuitively, when
    # Python "sees" the name "lst0", it will "plug in" the object [1, 2]
    # already stored in the computer memory.

    # The following will also print the object ID. You can think of it as a
    # unique identifier for objects stored in the computer memory.
    printit(lst0, "EXAMPLE 1: This is lst0")

    # We can create a new list with the same elements as `lst0`:
    lst1 = [1, 2]

    # Intuition for the statement above:
    # 1. is "lst1" a valid name for a variable? Yes
    # 2. Evaluate the expression [1, 2]
    #    - The result will be A NEW instance of the "list" type with elements
    #      1 and 2. This instance is stored somewhere in the computer memory.
    #      Again, this is a NEW list, not the one bound to `lst0`
    # 3. Assign the object created to the target. In this case, it's the
    #    variable "lst1". 

    # The following will also print the object ID of the new list. You can
    # tell this is a different list because it has a different object ID than
    # the object assigned to `lst0`
    printit(lst1, "EXAMPLE 1: This is lst1")

    # SUMMARY: Two distinct list instances are created by the statements:
    #   lst0 = [1, 2]
    #   lst1 = [1, 2]

    

def example2():
    """ Example illustrating assignment statements of the form 

        <target> = <expression>

    where BOTH `<target>` and <expression> are variables names

    """

    # First, create new lists (just like in example 1)
    # Just like in Example 1, these will create TWO list instances and assign
    # them to the variables `lst0` and `lst1`
    lst0 = [1, 2]
    lst1 = [1, 2]

    # Now, consider the following statement
    lst2 = lst0

    # The question is: Does `lst2 = lst0` above create a new list with the
    # same values as `lst0`?
    # Answer: NO
    # 
    # To understand why, let's go through the execution of this statement:
    # 
    # lst2 = lst0
    #
    # 1. Is lst2 a valid name? Yes
    # 2. Evaluate the expression on the right side of =
    #    - In this case, the expression is a variable. Python will simply
    #    "plug-in" the object assigned to this variable, that is, the list
    #    instance already in the computer memory (this instance was created by
    #    the statement `lst0 = [1, 2]` above). 
    # 3. Assign the existing list instance to the target, in this case, the
    #    variable `lst2`

    # The important thing to understand is that the same object is assigned to
    # two variables, `lst0` and `lst2`. You can see this by comparing the
    # object IDs below:
    #
    # NOTE: The object IDs will be different than in example 1. The important
    # thing to notice is that the object ID is the same for `lst0` and `lst2`
    # 

    printit(lst0, "EXAMPLE 2: This is lst0")
    printit(lst1, "EXAMPLE 2: This is lst1")
    printit(lst2, "EXAMPLE 2: This is lst2")




def example3():
    """ Example illustrating how you can use different names to manipulate the
    same object

    """

    # Start with the same example as above
    lst0 = [1, 2]
    lst1 = [1, 2]
    lst2 = lst0

    # Let's print these objects before any changes
    printit(lst0, "EXAMPLE 3: This is the ORIGINAL lst0")
    printit(lst1, "EXAMPLE 3: This is the ORIGINAL lst1")
    printit(lst2, "EXAMPLE 3: This is the ORIGINAL lst2")

    # Now, let's change the value of the first element of `lst2`
    lst2[0] = -99

    # Note that this statement has the form:
    #
    #   <target> = <expression>
    #
    # Python will evaluate this statement from left to right (target first,
    # then expression). Intuitively, it works like this:
    # 
    # 1. Start with `<target>`: Python "reads" the name `lst2` followed by [0]
    #    - This tells Python that the <target> is not a simple variable name
    #      but a "reference" to "something".
    #    - Think of it as Python breaking down `lst2[0]` into two parts:
    #
    #       a. Is there an object in the computer memory assigned to the
    #       (variable) name `lst2`?
    #           If Yes, "plug-in" that object right ehre. 
    #           Otherwise raise an exception.
    #       In this case, the name `lst2` points to the list [1, 2] already in
    #       the computer memory
    #
    #       b. At this stage, we have the "plugged" list object followed by [0].
    #       Python understands that [0] preceded by a list instance means 
    #       "select the first element from that list object". 
    #
    #       This means that the `<target>` part of the assignment
    #       statement is a reference to the first element of the list instance
    #       assigned to both `lst0` and `lst2`.
    #
    # 2. Evaluate the `<expression>`:  In this case, the expression
    #   produces an instance of the "int" type with value -99. 
    #
    # 3. Assign the result of `<expression>` (the instance -99) to the
    # `<target>` (the first element in the list)
    #
    # This means that the list instance stored in the computer memory CHANGED
    # in place. Since this list is assigned to both `lst0` and `lst2` we have:

    printit(lst0, "EXAMPLE 3: This is lst0 after setting lst2[0] = -99")
    printit(lst1, "EXAMPLE 3: This is lst1 after setting lst2[0] = -99")
    printit(lst2, "EXAMPLE 3: This is lst2 after setting lst2[0] = -99")
    
    # This is because both variables point to the same object. Similarly,
    # since `lst1` is a completely different object, it was not affected by
    # the change.


def example4():
    """ Nested lists

    """

    # Consider the following example:
    lst0 = [1, 2]
    lst1 = [3, [1, 2] ]

    # Following the discussion in our previous examples:

    # lst0 = [1, 2] -> Creates one list with ID `x0` (x0 is some integer)
    # lst1 = [3, [1, 2] ] -> Creates two lists: 
    #        The "outer" list [3, ...] with ID `x1_0` 
    #        The "inner" list [1, 2] with ID `x1_1` 
    #
    # You can access the inner list of `lst1` using:
    # lst1[1] -> [1, 2]

    # It should be clear that there are three lists instances at this point
    # All the object IDs below are different
    printit(lst0, "EXAMPLE 4: This is lst0 (single list)")
    printit(lst1, "EXAMPLE 4: This is lst1 (nested lists, the ID is for the outer list)")
    printit(lst1[1], "EXAMPLE 4: This is lst1[1] (the inner list)")


def example5():
    """ Nested lists using references

    """

    # Consider the following example:
    lst0 = [1, 2]
    lst1 = [3, [1, 2] ]
    lst2 = [3, lst0 ]

    # Following the discussion in our previous examples:

    # lst0 = [1, 2] -> Creates one list with ID `x0` (x0 is some integer)
    # lst1 = [3, [1, 2] ] -> Creates two lists: 
    #        The "outer" list [3, ...] with ID `x1_0` 
    #        The "inner" list [1, 2] with ID `x1_1` 
    # lst2 = [3, lst0] -> Creates ONE list
    #        The "outer" list [3, ...] with ID `x2_0` 
    #        The second element is a REFERENCE to a list already created
    #        (with ID x0)
    #
    # This means that lst2[1] points to the same object as lst0

    # It should be clear that there are three lists instances at this point
    # All the object IDs below are different
    printit(lst0, "EXAMPLE 5: This is lst0 (single list)")
    printit(lst1, "EXAMPLE 5: This is lst1 (nested lists, the ID is for the outer list)")
    printit(lst1[1], "EXAMPLE 5: This is lst1[1] (the inner list)")
    printit(lst2, "EXAMPLE 5: This is lst2 (the outer list)")
    printit(lst2[1], "EXAMPLE 5: This is lst2[1] (the same list as lst0)")


def example6():
    """ Shallow copies
    """

    # Consider the following example:
    # lst0 = [1, 2] -> Creates one list with ID `x0` (x0 is some integer)
    lst0 = [1, 2]

    # We know that lst1 = lst0 will NOT create a new list
    #
    # So how can we create a copy of lst0?
    # 
    # Use the function `copy` inside the module `copy`
    lst1 = copy.copy(lst0)

    # These two lists will have different object IDs
    printit(lst0, "EXAMPLE 6: This is lst0")
    printit(lst1, "EXAMPLE 6: This is lst1")


def example7():
    """ Deep copies
    """

    # Consider the following example:
    lst0 = [1, 2]
    lst1 = [3, lst0 ]

    # Suppose we use to function `copy.copy` to generate a copy of lst1
    lst2 = copy.copy(lst1)

    # All the outer lists have different IDs
    printit(lst0, "EXAMPLE 7: This is lst0")
    printit(lst1, "EXAMPLE 7: This is lst1")
    printit(lst2, "EXAMPLE 7: This is lst2")

    # This is because copy.copy creates a "shallow" copy of `lst1`. Shallow
    # means that it won't RECURSIVELY copy nested objects. In other words, 
    # Both lst1[1] and lst2[1] will point to the same object as lst0
    printit(lst0, "EXAMPLE 7: This is lst0 (again)")
    printit(lst1[1], "EXAMPLE 7: This is lst1[1]")
    printit(lst2[1], "EXAMPLE 7: This is lst2[1]")

    # To copy nested objects, use `copy.deepcopy`
    lst3 = copy.deepcopy(lst1)

    printit(lst0, "EXAMPLE 7: This is lst0 (again)")
    printit(lst3[1], "EXAMPLE 7: This is lst3[1] (different than lst0)")





def main():
    """
    """


    # --------------------------------------------------------
    #  Example 1  
    # --------------------------------------------------------
    # Uncomment to run example 1

    #example1()

    # --------------------------------------------------------
    #  Example 2  
    # --------------------------------------------------------
    # Uncomment to run example 2 (please COMMENT all the previous function
    # calls, like example1(*))

    #example2()

    # --------------------------------------------------------
    #  Example 3  
    # --------------------------------------------------------
    # Uncomment to run example 3 (please COMMENT all the previous function
    # calls: example1(), example2())

    #example3()

    # --------------------------------------------------------
    #  Example 4  
    # --------------------------------------------------------
    # Uncomment to run example 3 (please COMMENT all the previous function
    # calls: example1(), example2(), example3())

    #example4()

    # --------------------------------------------------------
    #  Example 5  
    # --------------------------------------------------------
    # Uncomment to run example 3 (please COMMENT all the previous function
    # calls: example1(), example2(), example3(), example4())

    #example5()

    # --------------------------------------------------------
    #  Example 6  
    # --------------------------------------------------------
    # Uncomment to run example 3 (please COMMENT all the previous function
    # calls: example1(), ...

    #example6()

    # --------------------------------------------------------
    #  Example 7  
    # --------------------------------------------------------
    # Uncomment to run example 3 (please COMMENT all the previous function
    # calls: example1(), ...

    #example7()

if __name__ == "__main__":
    main()

