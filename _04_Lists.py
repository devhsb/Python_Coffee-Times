

print('\n\n############## Add, Remove , Modify ##############')

list = ["item1, item2, item3"]
print(list)

# Add item to the end
list.append('item4')
print(list)

# Add item to specific index
list.insert(0, "item0")
print(list)

# Remove item pemanently
del list[0]
print(list)

# Remove item and return it's value
list = [1,2,3,4,5]
print(list.pop())
print(list)
print(list.pop(0))

# Remove item using it's value
list = ["item1", "item2", "item3"]
list.remove('item2')
print(list)

# Modify list
list = [1,2,4,4]
list[2] = 3
print(list)


print('\n\n############## list length ##############')
# List length
list = [1,2,3,4,5]
length = len(list)
print(length)



print('\n\n############## Sorting ##############')
# Methods
    # sort()    sort(reverse = True)
    # sorted(list)
    # list.reverse()


# Sort List Alphabetically for parmanent
list = ['B', 'D', 'W', 'A']
list.sort()
print(list)

# Sort List Reverse Alphabetically for parmanent
list.sort(reverse=True)
print(list)

# Sort list temporary
print(sorted(list))
print(list)

# Reverse order of the list
list = [5,4,3,2,1]
list.reverse()
print(list)


print('\n\n############## Slice ##############')
list = [1,2,3,4,5,6]
print(list)

print("#print first 3 values")
print( list[:3] )

print("#print middle values")
print( list[2:4] )

print("#print 3 last values")
print( list[-3:] )


print('\n\n############## Copy List ##############')
list1 = [1,2,3,4]
list2 = list1
print(f'list1: {list1}')
print(f'list2: {list2}')

list1.append(5)
list2.append(55)
print(f'list1: {list1}')
print(f'list2: {list2}') #both print 1,2,3,4,5,55 because with this copy method python associate one list to another

print('\n\n############## Copy List Using Slice ##############')
list1 = [1,2,3,4]
list2 = list1[:] #copy items from 0 index to the last
print(f'list1: {list1}')
print(f'list2: {list2}')

list1.append(5)
list2.append(55)
print(f'list1: {list1}')
print(f'list2: {list2}') #here each list is individual and not assiciate with each other