# LISTS
friends = ['Sarah', 'Frenne', 'Tom', 'Reaha', 'Kevin', 'Aanya' ] # can be a mix of strings, ints, bools
#             0         1       2       3       4

numbers = [4, 6, 8, 10, 12, 24, 42]

print(friends)
print(friends[1])
print(friends[-1])
print(friends[1:4])

# friends.append("Faahh")
friends.insert(1, "Oorry") # insert orryy at index 1
friends.remove('Frenne')
print("Tom is at index : ", friends.index("Tom"))

friends.sort()
print(friends)
friends.clear() # clears whole list
print(friends)

numbers.sort()
print("Sorted : ", numbers)
numbers.reverse()
print("Reversed : ", numbers)
