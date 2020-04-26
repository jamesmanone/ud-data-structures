# Problem 2: LinkedList Union and Intersection

Files used:
* `./problem6.py`
* `./DataStructures/LinkedList.py`

### LinkedList.union
To return the union of two linked lists we need to combine both lists, omitting duplicates that are not in the original lists. to keep time complexity at O(n) as we traverse the first list and append its items to the target list we store the quantity of the items in a map (dictionary). As we go through the second list we can check for duplicates using O(1) lookups on the map. The map presents us with space complexity of O(n) to store a copy of one of the lists

### LinkedList.Intersect
To return the intersection of two lists we need to produce a list comprised of only the entries that occur in both lists. Again we produce a map of one list for O(n) space complexity. This time we do not add these values to the target list. Instead we perform those constant time lookups as we go though the second list, appending only those items which occurred in the first list. once again the O(n) space we dedicate to the map keeps the time complexity to O(n)
