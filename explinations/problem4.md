# Problem 4: Active Directory
Files used:
* `./problem4.py`
* `./Group.py`
* `./DataStructures/Stack.py`
* `./DataStructures/Set.py`

Here I used a stack to perform a depth first search to get all groups that are members of the group in question. I store the groups in a set, allowing for O(1) lookups to check if I've already seen that group. Then I iterate over the groups to check their users (I changed the users to a set for constant time lookups). O(n) space (storing pointers to groups in a set). Time is harder, we're looping over all the groups (O(n)) and the groups of all the groups (O(?)? the number of groups in the groups are not a function of the number of groups) plus some constant time set lookups.
