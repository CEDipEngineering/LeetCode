## Final Interview

### Question: How do you reverse a linked list inplace?

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


#### Notes:

- H. Mualem
First attempt was to save last node in variable and attach back at beginning. Upon realizinh he could alter the nodes next element pointer, he quickly jumped closer to the solution. I might have tipped a bit too hard, but I think he got the gist of it pretty quickly after trying a bit. Tip #2 (keep track) might be a bit strong. He made two mistakes, one was trying to skip the first iteration of while loop, and forgetting to update the head node pointer (node 0 <-> node 1). The second was he forgot to return the last node at the end.

- Felipe
First attempt involved trying to move around values inside the list, swapping back and forth.
Second attempt was to move node by node to the end of the list
When told repeatedly to try only reversing the pointers, the subject eventually started coding.