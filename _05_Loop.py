favLanguages = ['Java', 'Python', 'C++', 'Javascript']

############ Loop through list ############ 
for lang in favLanguages:
    print(lang, end=", ")
print()

############ Counting using range() ############ 
for value in range(1, 20):
    print(value)

############ Add value to the list using range() ############ 
list = range(1, 10000, 1000) #add values from 1-10000, steps bewtween each value should be 1000
for l in list:
    print(l, end=", ")
print()

############ find min() max() and sum() from list of numbers ############ 
list = range(1, 101)
print( f"min: {min(list)}" )
print( f'max: {max(list)}' )
print( f'Sum: {sum(list)}' )


############ List comprehensions ############ 
list = [value * 2 for value in range(1, 51)]  #loop through 1-50, multiply each value with 2 and add it to list
print(list)