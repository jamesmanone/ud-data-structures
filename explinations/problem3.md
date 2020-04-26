# Problem 4: Huffman Trees
Files used
* `./problem4.py`
* `./DataStructures/HuffmanTree.py`
* `./DataStructures/PriorityQueue.py`
* `./DataStructures/LRU_Cache.py`

### \_\_init\_\_()
This is where the heavy lifting is done. Tree nodes are stored in an unordered map for O(1) lookups while setting frequency (priority). Once priority is set for all chars in the input the nodes are placed in a min priority queue (implementation in PriorityQueue.py). My priority queue has worst case O(n) insertion and O(1) retrieval. The total time complexity to build the tree is O(n log(n)). Each pass through the priority queue we are cutting our remaining root nodes in half.

### encode()
Encode writes out bits one at a time by traversing the tree. This is O(n), but we do pick up a boost by using the LRU_Cache from problem 1. Having a read through cache with the last 30 chars certainly improves best case complexity, but worst case is still all cache misses, so it remains O(n). Because the cache is a fixed size space complexity remains O(n) to store the encoded string.

### decode()
Because of the nature of different length codes, I couldn't think of an efficient was to have a read through cache. Instead we just walk the tree until we find a leaf. O(n) time and space complexity. (tree size doesn't necessarily change with input size)
