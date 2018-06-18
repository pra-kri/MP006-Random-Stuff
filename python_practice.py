"""
To cover today:
--------------+
    [/] - Enumerate
    [/] - Lambdas
    [/] - args/kwargs
    [/] - testing membership within different data structures
    [X] - debugging
    [/] - generators
    [/] - Functional programming concepts
        [/] - map
        [/] - filter
        [/] - reduce
    [/] - Ternary operators/ conditional expressions
    [X] - optimising python code.. (especially loops, using vectorisation and FP...)
    [/] - exception handling
    [/] - how to make Python modules ... just put an empty __init__.py file in the directory...

--> Didnt cover debugging or optimisation today. Do that another day....


References: 
----------+
Intermediate Python book: http://book.pythontips.com/en/latest/index.html
Python Performance Tips:  https://nyu-cds.github.io/python-performance-tips/08-loops/


Also, should check out these pages later. Looks pretty useful...:
----------+
essay on optimising loops:  https://www.python.org/doc/essays/list2str/
wiki on performance tips:   https://wiki.python.org/moin/PythonSpeed/PerformanceTips#Loops
pandas optimising tips:     https://engineering.upside.com/a-beginners-guide-to-optimizing-pandas-code-for-speed-c09ef2c6a4d6
Python for Finance txtbook: Ch 4, 8


"""

#=============================================#
#==============    ENUMERATE    ==============#
#=============================================#

list1 = ['a', 'b', 'c', 'd', 'eeee', 'f', 'g', 'h', 'z']


# the optional 2nd argument in enumerate is the number you start enumerating from...
aaa = enumerate(list1, 3) 

for i in aaa:
    print(i)

print("----------------------------")

bbb = list(enumerate(list1, 4))


print(bbb)



#=============================================#
#===============  LAMBDAS  ===================#
#=============================================#
print("----------------------------")
# lambda = temporary 1-line function, pretty much...
# Behave exactly like normal functions.#
# Possible use cases: - you may only want to use a quick function once or twice, in which case it will be too much effort to def a new function. So could just use a lambda instead. This would probably be very useful for simple mathematical functions that dont require too much thinking to understand... :)

test1 = lambda x, y: x**y

print(test1(3,4))
print(test1(2,10))





#=============================================#
#=============  *args, **kwargs  =============#
#=============================================#

# *args
def test_var_woah(intentional_arg, *args):
    print("this is intentional: " + intentional_arg)
    for i in args:
        print("extra from *args : " + i)

test_var_woah('1','2','3','a','b','c','d','e')

print("================================")


# *kwargs
def test_var_twooo(intentional_kwarg, **kwargs):
    print("This is your first kwarg:" + intentional_kwarg)
    for i in kwargs:
        print("These are your extra kwargs: " + i)
        print type(i)
    print(kwargs)

test_var_twooo(intentional_kwarg = "onetwothree",
                kwarg1 = "ok lets see if this works",
                kwarg2 = "hmmmmmmmmm",
                kwarg3 = "string 1223",
                kwarg4 = 12345,
                kwarg5 = True)

# ok, so the kwargs that are added to the function are stored as dictionaries, where the keyword is the key in the dictionary.




#=============================================#
#===========  Membership Testing  ============#
#=============================================#
"""
# Commenting this entire section out, since it takes quite a bit of time...
# Reference: https://nyu-cds.github.io/python-performance-tips/05-membership/

# Which data structure is best to use when testing if an element is part of a collection of elements?

# Dictionaries {} and sets () will be the best, because they are both implemented using a hash table. Lists will be quite bad, because you'd have to check each element of a list (unless you have a sorted list and use binary search or something...)


import time


letters = 'abcdefghijklmnopqrstuvwxyz'
letters_list = [x+y+z+k+l for x in letters for y in letters for z in letters for k in letters for l in letters]

time0 = time.time()
print('aaaaa' in letters_list)
time1 = time.time()

print("Time taken to find 'aaaaa' in letters_list = " + str(time1-time0)) # turns out to be 0.0 sec.


time2 = time.time()
print('zzzzz' in letters_list)
time3 = time.time()

print("Time taken to find 'zzzzz' in letters_list = " + str(time3-time2)) # turns out to be 0.20 sec
# Finding zzzzz takes much longer than finding aaaaa, presumably because you have to do a linear search through a list.



letters_dict = dict([(x,x) for x in letters_list])

time4 = time.time()
print('aaaaa' in letters_dict)
time5 = time.time()
print("Time taken to find 'aaaaa' in letters_dict = " + str(time5-time4)) # turns out to be 0.0 sec


time6 = time.time()
print('zzzzz' in letters_dict)
time7 = time.time()
print("Time taken to find 'zzzzz' in letters_dict = " + str(time7-time6)) # turns out to be 0.0 sec

# For the dictionary, times taken to find zzzzz and aaaaa are the same, since there is no linear search.
# Instead the dictionary uses a hashing function on the key.
"""




#=============================================#
#===============  Generators  ================#
#=============================================#


"""
Quick overview of definitions...
 
-> Iterable: Any object which can provide us with an ITERATOR. The object will have an __iter__ or a __getitem__ method. These methods will return an iterator.

-> Iterator: Any object which has a __next__ method defined. That's all.

-> Iteration: the process of taking an item from something...

-> Generators: Generators are basically just iterators that you can only iterate over once. 
    Why? Because they do NOT store all the values in memory.
    They GENERATE values as needed, when being iterated over. 

    You mostly implement a GENERATOR as a function. Instead of using 'return', use 'yield'.

    Since generators dont store all values in memory, they are resource-efficient.

"""

def generator_1(N):
    for i in range(N):
        yield i 

def not_generator_1(N):
    for i in range(N):
        return i

print(generator_1(10))


gen_test = generator_1(10)
print(next(gen_test))
print(next(gen_test))
print(next(gen_test))
print(next(gen_test))
print(next(gen_test))


not_gen_test = not_generator_1(10)
print(not_gen_test)
#print(next(not_gen_test)) # this doesnt have a __next__ method, so wont work.



#=============================================#
#==================  Map  ====================#
#=============================================#

# map(function_to_apply, inputs_list)
# And instead of using a defined function, can also easily use a lambda function.

def square_number(x):
    return x**2

test_list_1 = [0,1,2,3,4,5,6,7,8,9,10]
test_map = map(square_number, test_list_1)

print(test_map)


# do another method, this time using lambdas, and a different function...
test_map2 = map(lambda x: x**x,test_list_1)
print(test_map2)


#=============================================#
#=================  Filter  ==================#
#=============================================#

# filter(function_to_apply_that_should_return_TRUE, inputs_list)

# If even, should % 2 to equal 0. 
even_number_list = filter(lambda x: x % 2 == 0, test_list_1)
print(even_number_list)


#=============================================#
#=================  Reduce  ==================#
#=============================================#


# allows you to apply a rolling computation to sequential pairs of values in a list.


# reduce(function_to_apply_on_pairs, inputs_list)

total_product = reduce(lambda x, y: x, test_list_1)
print(total_product)


"""
Its kind of like...:
-> Funciton is applied to the first two elements of the list.
-> Output of the function replaces the first two elements.
   (Now the first element of the list is the output of the last calculation.)
-> Now just do the same thing again: apply the funciton to the new first two elements of the list.
->>> and so on....
"""



#===============================================#
#=  Ternary Operators/ Conditional Expressions =#
#===============================================#


test_state = True

state = "okkkkk" if test_state is True else "nope not Trueeee"

print(state)


# Also, note that True = 1, and False = 0

# so you can refer to element 1 of a list by using: list_to_check[True]
# And you can replace the 'True' with something you want to test.





#===============================================#
#===========  Exception Handling ===============#
#===============================================#

# basic code: try/except
try:
    file = open('test_file12323323.txt', 'rb')
except IOError as e:
    print(e)

# more advanced: handling multiple specific exceptions...
try:
    file = open('test_file12323323.py', 'rb')
except EOFError as e:
    print(e)
    #raise e
except IOError as f:
    print(f)


# or, if you want to handle ALL exceptions, regardless of type...
try:
    file = open('test_file12323323', 'rb')
except Exception as e:
    # whatever you want to happen in here
    print(e)
    #raise(e)




# and then there's also the 'finally' clause, which will run whether or not an exception is raised.
try:
    file = open('test_file12323323.txt', 'rb')
except IOError as e:
    #raise e
    print(e)
finally:
    print('This will be printed regardless of what happens')



# and there's also the else clause:

try:
    file = open('test_file12323323.txt', 'rb')
except IOError as e:
    #raise e
    print(e)
else:
    #file = open('test_file12323323.eeee', 'rb')
    print('else part worked!!!!!!!!!!')
    # this part will run if there are NO exceptions raised in the try.
    # but any exceptions that occur here will not be caught...
finally:
    print('This will be printed regardless of what happens aaaaa')
