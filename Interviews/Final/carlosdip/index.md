## Final Interview

### Question: How do you reverse a linked list with constant space complexity?

- Description:
This problem was found at [codeburst.io](https://codeburst.io/100-coding-interview-questions-for-programmers-b1cf74885fb7), number 21 on a list of 100 problems. The challenge comes from doing so inplace, and having to worry about where you keep pointers and how do you move through the list efficiently.

- Hints:
    1. Do you need to manipulate the values inside the nodes?
    2. Maybe you can keep track of previous node pointers as you traverse the list?
    3. How far back do you need to keep track of the node pointers? 1, 2, 3 nodes back?

- Solution:
The goal is to reverse the linked list. To do so, it would suffice to simply reverse the pointers on every node, such that children nodes point to their parents. Of course, a single linked list does not have a parent attribute, so the search through the list is a little more in-depth.

First, you must keep track of three nodes at any given moment, let's call them **previous**, **current** and **next**. The algorith is as follows: Initially, **previous** and **next** are set to null, and **current** is set to the head node of the list (as received via input to the function). We then store the **current** node's next value in the **next** pointer. Then we update our **current** node's next pointer to the **previous** value, set **previous** to be our **current** pointer and update **current** to match **next**. We repeat this untill **current** has no next node (end of list).

The algorithm described above has a time complexity of O(n) and a space complexity of O(1) (inplace).
