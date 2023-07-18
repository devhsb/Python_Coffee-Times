# CRUD Operation Methods
    # CREATE 
        # append(value)  insert(index, value)    
    # REMOVE
        # del   pop(index)   remove(value)
    # UPDATE
        # list[index] = "value"



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