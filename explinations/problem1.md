# Problem 1: Least Recently Used Cache

Files used:<br />
`./problem1.py`<br />
`./DataStructures/LRU_Cache.py`


The cache is set up as a hashtable, so inserts and lookups happen in O(1) time

#### get()
get checks for the key. if it finds it the key is returned and the this becomes the most recently used item.

#### set()/\_\_put()
set attempts to update the key (and make this the most recent key). If the key isn't found it's passed to \_\_put() which inserts the key. If the cache is at capacity it calls \_\_deleteLRU()

#### \_\_deleteLRU()
This method deletes the least recently used item. To keep operations O(1) we keep a transaction history with voidable nodes. When nodes are retrieved or updated a new node is created to replace the original, and we call Node.invalidate() on the original. Node.invalidate() removes the Node from the Deletion_Queue by stitching together Node.qnext and Node.qprev. Finally, to handle the cases of the node being at the head or tail of the deletion queue we notify the queue of the invalidation.

## Edge Case
The only case I know of in which we lose O(1) operations is the event that many items end up in the same bucket. We attempt to prevent this by making the bucket array 1.43x larger than the capacity of the cache
