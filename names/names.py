import time
from binarySearchTree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

#takes ~ 5 seconds
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#Using BST
bst = BinarySearchTree('')
duplicates = []

#First--- insert all the names from list 1 into a bst structure.
for name in names_1:
    bst.insert(name)

for name in names_2:
    # Next check our bst for duplicates
    # compare strings by comparing their ascii value
    if bst.contains(name): 
        # if there is a match then its appended to duplcate list
        duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
