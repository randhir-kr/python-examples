# Sets{} : Unordered, mutable, no duplicate values allowed

color = {"blue", "black", "blue", "white"}

print(color)

color.add("white")

"""
Sets are mutable, but they don't support index-based access or assignment.
Here's why:
Sets are unordered — Unlike lists where [0] is the first element, sets have no inherent order. There's no concept of "first" or "second" element, so color[0] doesn't make sense.
Mutable ≠ Index assignment — "Mutable" means you can add or remove items from the collection, but not necessarily modify them by index. Lists are also mutable AND support index assignment. Sets are mutable but use a different modification approach.
You can only modify sets via methods:

.add() — add an item
.remove() — remove an item (raises error if not found)
.discard() — remove an item (no error if not found)
.pop() — remove and return an arbitrary item
.clear() — remove all items
"""

print("color after modifying: ", color)
