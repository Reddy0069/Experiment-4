# Number List Operations

values = [45, 15, 35, 25, 55, 15]

print("Initial List:", values)

# Size of List
print("Total elements:", len(values))

# Add at End
values.append(65)
print("List after adding 65:", values)

# Add at Position
values.insert(3, 30)
print("List after inserting 30:", values)

# Duplicate Count
print("Number of 15s:", values.count(15))

# Find Position
print("Position of 35:", values.index(35))

# Remove Value
values.remove(15)
print("List after deleting 15:", values)

# Make a Copy
backup = values.copy()
print("Backup List:", backup)

# Add Multiple Values
values.extend([75, 85])
print("List after adding more values:", values)

# Arrange Values
values.sort()
print("Ascending List:", values)

# Reverse Order
values.reverse()
print("Reversed List:", values)

# Mathematical Operations
print("Largest Value:", max(values))
print("Smallest Value:", min(values))
print("Total of Values:", sum(values))
