# Problem 2: File Recursion

Files used:<br />
`./problem2.py`<br />
`./DataStructures/Stack.py`

Find files is preorder depth first search. The search take O(n) time complexity

1. Push the results of `os.listdir()` onto a stack.
2. Pop an item off the stack.
3. If the item is a file and `endswith` the ext we're looking for:
  * add to results
4. if the item is a dir, push its contents to the stack
5. Repeat

I couldn't see any reason to choose dfs or bfs since we have to touch every node.
