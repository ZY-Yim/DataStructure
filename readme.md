# Problem Solving with Algorithms and Data Structures

[TOC]

## Introduction
### Review of Basic Python
#### Data
int float \ bool \ 
list string tuple \ set dict

#### Input and Output
input \ output

#### Control Structures
while for

#### Exception Handing
try except

#### Defining Functions
def 

#### Object-Oriented Programming
class

## ALGORITHM ANALYSIS
### What is Algothrm Analysis
#### Big-O Notation
Our goal is to show how the algorithm’s execution time changes
with respect to the size of the problem.
order of magnitude, it provides a useful approximation to the actual number of steps in the computation.

#### Anagram Detection
Checking Off: $ 𝑂(n^2) $
Sort and Compare: $ 𝑂(n^2) $ or $ 𝑂(nlogn) $
Brute Force: $ O(n!) $
Count and Compare: $ O(n) $

### Performance of Python Data Structures
the Big-O performance for the operations on Python lists and dictionaries
#### List
common operations: indexing and assign to an index position $ O(1) $ \ grow a list 

generate a list of $ n $ numbers: 
* concatenation: $ O(k) $
* append: $ O(1) $
* comprehension: 
* range function: 

Big-O Efficiency of Python List Operations

![image-20211009160325627](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211009160325627.png)

#### Dict
![image-20211009170052665](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211009170052665.png)

## BASIC DATA STRUCTURES

### What Are Linear Structures

linear structure: stacks, queues, deques, and lists (whose items are ordered depending on how they are added or removed)

### Stacks

an ordered collection of items
top base
LIFO(last-in-first-out)

#### The Stack Abstract Data Type

 stack operations:

* Stack()
* push(item)
* pop()
* peek()
* is_empty()
* size()

![image-20211013145538783](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211013145538783.png)

#### Implementing A Stack in Python

class Stack()

#### Simple Balance Parentheses

whether the string of parentheses is balanced

#### Balanced Symbols (A General Case)

When a closing symbol does appear, the only difference is that we must check to be sure that it correctly matches the type of the opening symbol on top of the stack.

#### Converting Decimal Numbers to Binary Numbers

Divide by 2

#### Infix, Prefix, and Postfix Expressions

* Conversion of Infix Expressions to Prefix and Postfix 

![image-20211011222019474](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211011222019474.png)

* General Infix-to-Postfix Conversion

When we see a left parenthesis, we will save it to denote that another operator of high precedence will be coming. That operator will need to wait until the corresponding right parenthesis appears to denote its position (recall the fully parenthesized technique). When that right parenthesis does appear, the operator can be popped from the stack.

![image-20211012142231400](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211012142231400.png)

Steps:

> 1. Create an empty stack called op_stack for keeping operators. Create an empty list for output.
>
> 2. Convert the input infix string to a list by using the string method split.
>
> 3. Scan the token list from left to right.
>
>    • If the token is an operand, append it to the end of the output list.
>    • If the token is a left parenthesis, push it on the op_stack.
>    • If the token is a right parenthesis, pop the op_stack until the corresponding left parenthesis is removed. Append each operator to the end of the output list.
>    • If the token is an operator, *, /, +, or −, push it on the op_stack. However, first remove any operators already on the op_stack that have higher or equal precedence and append them to the output list.
>
> 4. When the input expression has been completely processed, check the op_stack. Any operators still on the stack can be removed and appended to the end of the output list.

* Postfix Evaluation

![image-20211012142116611](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211012142116611.png)

> 1. Create an empty stack called operand_stack.
> 2. Convert the string to a list by using the string method split.
> 3. Scan the token list from left to right.
>    • If the token is an operand, convert it from a string to an integer and push the value onto the operand_stack.
>    • If the token is an operator, *, /, +, or −, it will need two operands. Pop the operand_stack twice. The first pop is the second operand and the second pop is the first operand. Perform the arithmetic operation. Push the result back on the operand_stack.
> 4. When the input expression has been completely processed, the result is on the stack. Pop the operand_stack and return the value.

### Queues

an ordered collection of items
front(remove) rear(add)
FIFO, first-in first-out

#### The Queue Abstract Data Type

* Queue() 
* enqueue(item): $ O(n) $
* dequeue(): $ O(1) $
* is_empty()
* size()

![image-20211013145612829](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211013145612829.png)

#### Implementing A Queue in Python

the rear is at position 0 in the list. 
class Queue()

#### Simulation: Hot Potato

![image-20211013153228265](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211013153228265.png)

#### Simulation: Printing Tasks

![image-20211013163835399](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211013163835399.png)

Main Simulation Steps:

1. Create a queue of print tasks. Each task will be given a timestamp upon its arrival. The queue is empty to start.
2. For each second (current_second):
   • Does a new print task get created? If so, add it to the queue with the current_second
   as the timestamp.
   • If the printer is not busy and if a task is waiting,
     – Remove the next task from the print queue and assign it to the printer.
     – Subtract the timestamp from the current_second to compute the waiting time
   for that task.
     – Append the waiting time for that task to a list for later processing.
     – Based on the number of pages in the print task, figure out how much time will be required.
   • The printer now does one second of printing if necessary. It also subtracts one second from the time required for that task.
   • If the task has been completed, in other words the time required has reached zero, the printer is no longer busy.
3. After the simulation is complete, compute the average waiting time from the list of waiting times generated.

### Deques

an ordered collection of items
It has two ends, a front and a rear, and the items remain positioned in the collection. What makes a deque different is the unrestrictive nature of adding and removing items. New items can be added at either the front or the rea

#### The Deque Abstract Data Type

* Deque()
* add_front()
* add_rear()
* remove_front
* remove_rear()
* is_empty()
* size()

#### Implementing a Deque in Python

class Deque()

#### Palindrome Checker

A palindrome is a string that reads the same forward and backward, for
example, radar, toot, and madam.
![image-20211013171017277](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211013171017277.png)

### Lists

#### The Unordered List Abstract Data Type

The structure of an unordered list, as described above, is a collection of items where each item holds a relative position with respect to the others.

Some possible unordered list operations:

* List() 
* add(item) 
* remove(item)
* search(item): return a boolean value
* is_empty()
* size()
* append(item)
* index(item)
* insert(pos, item)
* pop()
* pop(pos)

#### Implementing an Unordered List: Linked Lists

* The Node Class
  ![image-20211013190910286](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211013190910286.png)
* The Unordered List Class
  the linked list structure provides us with only one entry point, the head of the list. we will make the new item the first item of the list and the existing
  items will need to be linked to this new first item so that they follow.
  ![image-20211013192438986](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211013192438986.png)

#### The Ordered List Abstract Data Type

The structure of an ordered list is a collection of items where each item holds a relative position that is based upon some underlying characteristic of the item. The ordering is typically either ascending or descending and we assume that list items have a meaningful comparison operation that is already defined. 

* OrderedList() 
* add(item) 
* remove(item)
* search(item)
* is_empty()
* size()
* index(item)
* pop()
* pop(pos)

#### Implementing an Ordered List

overwrite search and add method

#### Analysis of Linked Lists

is_empty: $ O(1) $
size: $ O(n) $
add for unordered list: $ O(1) $
add search remove for ordered list: $ O(n) $

> linked lists are not the way Python lists are implemented. The actual implementation of a Python list is based on the notion of an array. 

## RECURSION

### What is Recursion

Recursion is a method of solving problems that involves breaking a problem down into smaller and smaller subproblems until you get to a small enough problem that it can be solved trivially.

#### Calculating the Sum of a List of Numbers

list_sum(num_list) = first(num_list) + list_sum(rest(num_list))

#### The Three Laws of Recursion

1. A recursive algorithm must have a base case.
2. A recursive algorithm must change its state and move toward the base case.
3. A recursive algorithm must call itself, recursively.

#### Converting an Integer to a String in Any Base

Knowing what our base is suggests that the overall algorithm will involve three components:

1. Reduce the original number to a series of single-digit numbers.
2. Convert the single digit-number to a string using a lookup.
3. Concatenate the single-digit strings together to form the final result

### Stack Frames: Implementing Recursion

When a function is called in Python, a stack frame is allocated to handle the local variables of the function. When the function returns, the return value is left on top of the stack for the calling function to access

### Visualising Recursion

* spiral
* tree
* Sierpinski Triangle
  ![image-20211014202654928](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211014202654928.png)

### Complex Recursive Problems

#### The Towers Of Hanoi

Here is a high-level outline of how to move a tower from the starting pole, to the goal pole, using an intermediate pole:

1. Move a tower of height-1 to an intermediate pole, using the final pole.
2. Move the remaining disk to the final pole.
3. Move the tower of height-1 from the intermediate pole to the final pole using the original pole.

### Exploring a Maze

a systematic procedure:

* From our starting position we will first try going North one square and then recursively try our procedure from there.
* If we are not successful by trying a Northern path as the first step then we will take a step to the South and recursively repeat our procedure.
* If South does not work then we will try a step to the West as our first step and recursively apply our procedure.
* If North, South, and West have not been successful then apply the procedure recursively from a position one step to our East.
* If none of these directions works then there is no way to get out of the maze and we fail.

> in order to avoid infinite loop, we must have a strategy to remember where we have been. In this case we will assume that we have a bag of bread crumbs we can drop along our way. If we take a step in a certain direction and find that there is a bread crumb already on that square, we know that we should immediately back up and try the next direction in our procedure. 

In this algorithm, there are four base cases to consider:

1. The turtle has run into a wall. Since the square is occupied by a wall no further exploration can take place.
2. The turtle has found a square that has already been explored. We do not want to continue exploring from this position or we will get into a loop.
3. We have found an outside edge, not occupied by a wall. In other words we have found an exit from the maze.
4. We have explored a square unsuccessfully in all four directions.

![image-20211015160812816](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211015160812816.png)

## SORTING AND SEARCHING

### Searching

#### The Sequential Search

![image-20211016151938648](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211016151938648.png)

Starting at the first item in the list, we simply move from item to item, following the underlying sequential ordering until we either find what we are looking for or run out of items.

* unordered list

![image-20211016152327963](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211016152327963.png)

the complexity of the sequential search, is 𝑂(𝑛)

* ordered list

![image-20211016153109098](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211016153109098.png)

the complexity of the sequential search, is 𝑂(𝑛)

#### The Binary Search

the binary search is designed for an ordered list
a binary search will start by examining the middle item. If that item is the one
we are searching for, we are done. If it is not the correct item, we can use the ordered nature of the list to eliminate half of the remaining items. If the item we are searching for is greater than the middle item, we know that the entire lower half of the list as well as the middle item can be eliminated from further consideration. The item, if it is in the list, must be in the upper half.

![image-20211016154348454](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211016154348454.png)

the complexity of the binary search, is 𝑂(log𝑛)

#### Hashing

build a data structure that can be searched in 𝑂(1) time. This concept is referred to as hashing.
A hash table is a collection of items which are stored in such a way as to make it easy to find them later. Each position of the hash table, often called a slot, can hold an item and is named by an integer value starting at 0.
The mapping between an item and the slot where that item belongs in the hash table is called the hash function. The hash function will take any item in the collection and return an integer in the range of slot names, between 0 and 𝑚−1.
![image-20211016161908858](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211016161908858.png)
![image-20211016161920414](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211016161920414.png)
![image-20211016161930183](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211016161930183.png)

##### Hash Functions

Our goal is to create a hash function that minimizes the number of collisions, is easy to compute, and evenly distributes the items in the hash table.

* folding method
  The folding method for constructing hash functions begins by dividing the item into equal-size pieces (the last piece may not be of equal size). These pieces are then added together to give the resulting hash value.436-555-
  436-555-4601, (43, 65, 55, 46, 01), sum() = 210, 210%11 = 1
  some folding methods reverse every other piece before addition

* mid-square method
  we first square the item, and then extract some portion of the resulting digits
  44, 44^2 = 1936, extract 93, 93%11 = 5

* hash functions for character-based items such as strings

  ![image-20211016191248698](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211016191248698.png)

  We can then take these three ordinal values, add them up, and use the remainder method to get a hash value.
  cat, 99+97+116 = 312, 312%11 = 4

##### Collision Resolution

When two items hash to the same slot, we must have a systematic method for placing the second item in the hash table.

* linear probing(open addressing)
  start at the original hash value position and then move in a sequential manner through the slots until we encounter the first slot that is empty. 
  
  ![image-20211016204153003](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211016204153003.png)A disadvantage to linear probing is the tendency for clustering; items become clustered in the table. This means that if many collisions occur at the same hash value, a number of surrounding slots will be filled by the linear probing resolution.
  One way to deal with clustering is to extend the linear probing technique so that instead of looking sequentially for the next open slot, we skip slots, thereby more evenly distributing the items that have caused collisions.
  
  ![image-20211016204214402](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211016204214402.png)new_hash_value = rehash(old_hash_value)
  rehash(pos) = (pos + 1)%size_of_table
  rehash(pos) = (pos + 3)%size_of_table
  in general, rehash(pos) = (pos + skip)%size_of_table
  
* quadratic probing
  Instead of using a constant “skip” value, we use a rehash function that increments the hash value by 1,3,5,7,9, and so on.
  This means that if the first hash value is ℎ, the successive values are ℎ+1,ℎ+4,ℎ+9,ℎ+16, and so on. In other words, quadratic probing uses a skip consisting of successive perfect squares.
  ![image-20211016204042874](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211016204042874.png)
  
* Chaining
  Chaining allows many items to exist at the same location in the hash table.
  ![image-20211016204003500](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211016204003500.png)

##### Implementing the Map Abstract Data Type

The map abstract data type is defined as follows. The structure is an unordered collection of associations between a key and a data value(dictionary). The keys in a map are all unique so that there is a one-to-one relationship between a key and a value.

operations:

* Map()
* put(key, value)
* get(key)
* del map(key)
* len()
* in

we will have a result for both a successful and an unsuccessful search. 
For a successful search using open addressing with linear probing, the average number of comparisons is approximately 
$$
\frac{1}{2}(1+\frac{1}{1-𝜆})
$$
and an unsuccessful search gives ︁
$$
\frac{1}{2}(1+{(\frac{1}{1-𝜆})}^{2})
$$
If we are using chaining, the average number of comparisons is 
$$
1+\frac{1}{𝜆}
$$
for the successful case, and simply 𝜆 comparisons if the search is unsuccessful
$$
𝜆
$$

### Sorting

#### Bubble Sort

the complexity of the bubble sort, is 𝑂(𝑛^2)
in the best case, if the list is already ordered, no exchanges will be made. However, in the worst case, every comparison will cause an exchange. On average, we exchange half of the time.
**short bubble sort**: if during a pass there are no exchanges, then we know that the list must be sorted. A bubble sort can be modified to stop early if it finds that the list has become sorted.

#### Selection Sort

the complexity of the selection sort, is 𝑂(𝑛^2)
The selection sort improves on the bubble sort by making only one exchange for every pass through the list and it executes faster in benchmark studies.
![image-20211017182417406](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211017182417406.png)

#### The Insertion Sort

the complexity of the insertion sort, is 𝑂(𝑛^2)
It always maintains a sorted sublist in the lower positions of the list. Each new item is then “inserted” back into the previous sublist such that the sorted sublist is one item larger.
However, in the best case, only one comparison needs to be done on each pass. This would be the case for an already sorted list.
![image-20211017182329514](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211017182329514.png)

#### Shell Sort

the complexity of shell sort tends to fall somewhere between 𝑂(𝑛) and 𝑂(𝑛2)
By changing the increment, for example using 2^𝑘 −1 (1,3,7,15,31, and so on), a shell sort can perform at 𝑂(𝑛^3/2)
The shell sort, sometimes called the “diminishing increment sort,” improves on the insertion sort by breaking the original list into a number of smaller sublists, each of which is sorted using an insertion sort. the shell sort uses an increment *i*, sometimes called the gap, to create a sublist by choosing all items that are *i* items apart.
![image-20211017191049041](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211017191049041.png)

#### The Merge Sort

the complexity of merge sort is 𝑂(𝑛log𝑛), split and merge
Merge sort is a recursive algorithm that continually splits a list in half. If the list is empty or has one item, it is sorted by definition (the base case). If the list has more than one item, we split the list and recursively invoke a merge sort on both halves. Once the two halves are sorted, the fundamental operation, called a merge, is performed. Merging is the process of taking two smaller sorted lists and combining them together into a single, sorted, new list.
![image-20211017194249591](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211017194249591.png)
![image-20211017194301007](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211017194301007.png)

the merge_sort function requires extra space to hold the two halves as they are extracted with the slicing operations. This additional space can be a critical
factor if the list is large and can make this sort problematic when working on large data sets.

#### The Quick Sort

the complexity of quick sort is 𝑂(𝑛log𝑛). for a list of length 𝑛, if the partition always occurs in the middle of the list, there will again be log 𝑛 divisions. In order to find the split point, each of the 𝑛 items needs to be checked against the pivot value. in the worst case, the split points may not be in the middle and can be very skewed to the left or the right, leaving a very uneven division. In this case, sorting a list of 𝑛 items divides into sorting a list of 0 items and a list of 𝑛 − 1 items. Then sorting a list of 𝑛 − 1 divides into a list of size 0 and a list of size 𝑛 − 2, and so on. The result is an 𝑂(𝑛^2) sort with all of the overhead that recursion requires.
The quick sort uses divide and conquer to gain the same advantages as the merge sort, while not using additional storage.
![image-20211017203105573](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211017203105573.png)
![image-20211017203117307](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211017203117307.png)

### Summary

• A sequential search is 𝑂(𝑛) for ordered and unordered lists.
• A binary search of an ordered list is 𝑂(log 𝑛) in the worst case.
• Hash tables can provide constant time searching.
• A bubble sort, a selection sort, and an insertion sort are 𝑂(𝑛^2) algorithms.
• A shell sort improves on the insertion sort by sorting incremental sublists. It falls between 𝑂(𝑛) and 𝑂(𝑛^2).
• A merge sort is 𝑂(𝑛log 𝑛), but requires additional space for the merging process.
• A quick sort is 𝑂(𝑛log 𝑛), but may degrade to 𝑂(𝑛^2) if the split points are not near the middle of the list. It does not require additional space

## TREES AND TREE ALGORITHMS

### Examples of Trees

several properties of trees:

* trees are hierarchical
* all of the children of one node are independent of the children of another node
* each leaf node is unique

### Vocabulary and Definition

#### Vocabulary

* Node
* Edge
* Root
* Path
* Children
* Parent
* Sibling
* Subtree
* Leaf Node
* Level: the number of edges on the path from the root node to the node
* Height: the maximum level of any node in the tree

#### Definition

*Definition One:* A tree consists of a set of nodes and a set of edges that connect pairs of nodes. A tree has the following properties:

- One node of the tree is designated as the root node.
- Every node *n*, except the root node, is connected by an edge from exactly one other node *p*, where pp is the parent of *n*.
- A unique path traverses from the root to each node.
- If each node in the tree has a maximum of two children, we say that the tree is a **binary tree**.

![image-20211018160038669](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211018160038669.png)

*Definition Two:* A tree is either empty or consists of a root and zero or more subtrees, each of which is also a tree. The root of each subtree is connected to the root of the parent tree by an edge.

![image-20211018160059972](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211018160059972.png)

### Implementation

The key decision in implementing a tree is choosing a good internal storage technique. Python allows us two very interesting possibilities, so we will examine both before choosing one. The first technique we will call “list of lists,” the second technique we will call “nodes and references.”

#### List of Lists Representation

In a list of lists tree, we will store the value of the root node as the first element of the list. The second element of the list will itself be a list that represents the left subtree. The third element of the list will be another list that represents the right subtree.

![image-20211018161918086](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211018161918086.png)

![image-20211018161933098](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211018161933098.png)

One very nice property of this list of lists approach is that the structure of a list representing a subtree adheres to the structure defined for a tree; the structure itself is recursive! A subtree that has a root value and two empty lists is a leaf node. Another nice feature of the list of lists approach is that it generalizes to a tree that has many subtrees. In the case where the tree is more than a binary tree, another subtree is just another list.

#### Nodes and References

In this case we will define a class that has attributes for the root value, as well as the left and right subtrees. this representation more closely follows the object-oriented programming paradigm.

### Binary Tree Applications

#### Parse Tree

((7+3)∗(5−2))

![image-20211018192448076](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211018192448076.png)

1. If the current token is a `'('`, add a new node as the left child of the current node, and descend to the left child.
2. If the current token is in the list `['+','-','/','*']`, set the root value of the current node to the operator represented by the current token. Add a new node as the right child of the current node and descend to the right child.
3. If the current token is a number, set the root value of the current node to the number and return to the parent.
4. If the current token is a `')'`, go to the parent of the current node.

#### Tree Traversals

There are three commonly used patterns to visit all the nodes in a tree. The difference between these patterns is the order in which each node is visited. We call this visitation of the nodes a “traversal.” The three traversals we will look at are called **preorder**, **inorder**, and **postorder**. 

* **preorder**
  In a preorder traversal, we visit the root node first, then recursively do a preorder traversal of the left subtree, followed by a recursive preorder traversal of the right subtree.

* **inorder**
  In an inorder traversal, we recursively do an inorder traversal on the left subtree, visit the root node, and finally do a recursive inorder traversal of the right subtree.

* postorder
  In a postorder traversal, we recursively do a postorder traversal of the left subtree and the right subtree followed by a visit to the root node.

### Priority Queues with Binary Heaps

A priority queue acts like a queue in that you dequeue an item by removing it from the front. However, in a priority queue the logical order of items inside a queue is determined by their priority. The highest priority items are at the front of the queue and the lowest priority items are at the back.

The classic way to implement a priority queue is using a data structure called a **binary heap**. A binary heap will allow us both enqueue and dequeue items in *O(log n)*.

The binary heap is interesting to study because when we diagram the heap it looks a lot like a tree, but when we implement it we use only a single list as an internal representation. The binary heap has two common variations: the **min heap**, in which the smallest key is always at the front, and the **max heap**, in which the largest key value is always at the front.

#### Binary Heap Operations

* BinaryHeap()
* insert(k)
* findMin()
* delMin()
* isEmpty()
* size()
* buildHeap(list)

#### Binary Heap Implementation

##### The Structure Property

In our heap implementation we keep the tree balanced by creating a **complete binary tree**. each level has all of its nodes except the bottom level. 

Another interesting property of a complete tree is that we can represent it using a single list. the left child of a parent (at position p) is the node that is found in position 2p in the list. Similarly, the right child of the parent is at position 2p+1 in the list.
![image-20211026201620327](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211026201620327.png)

##### The Heap Order Property

In a heap, for every node *x* with parent *p*, the key in pp is smaller than or equal to the key in *x*.

##### Heap Operations

The assertion that we can build the heap in O(n)

### Binary Search Trees

#### Search Tree Operations

* Map()
* put(key, val)
* get(key)
* del
* len()
* in

#### Search Tree Implementation

A binary search tree relies on the property that keys that are less than the parent are found in the left subtree, and keys that are greater than the parent are found in the right subtree. We will call this the **bst property**.
![image-20211026210808139](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211026210808139.png)
inserting a new node in the tree:

- Starting at the root of the tree, search the binary tree comparing the new key to the key in the current node. If the new key is less than the current node, search the left subtree. If the new key is greater than the current node, search the right subtree.
- When there is no left (or right) child to search, we have found the position in the tree where the new node should be installed.
- To add a node to the tree, create a new `TreeNode` object and insert the object at the point discovered in the previous step.

#### Search Tree Analysis

If the keys are added in a random order, the height of the tree is going to be around log2n where n is the number of nodes in the tree.

The total number of nodes in a perfectly balanced binary tree is 2^(h+1)−1, where h represents the height of the tree.

In a balanced binary tree, the worst-case performance of `put` is *O(log2 n)*, where n is the number of nodes in the tree. it is possible to construct a search tree that has height n simply by inserting the keys in sorted order. In this case the performance of the `put` method is *O(n)*.

### Balanced Binary Search Trees

**AVL tree**: automatically make sure that the tree remains balanced at all times.

we define the balance factor for a node as the difference between the height of the left subtree and the height of the right subtree.
$$
balanceFactor=height(leftSubTree)−height(rightSubTree)
$$
The balance factor is greater than zero then the subtree is left-heavy, and the subtree is right heavy if the balance factor is less than zero. If the balance factor is zero then the tree is perfectly in balance.

we define a tree to be in balance if the balance factor is -1, 0, or 1.

#### AVL Tree Performance

$$
h=1.44logN_h
$$

At any time the height of our AVL tree is equal to a constant(1.44) times the log of the number of nodes in the tree. This is great news for searching our AVL tree because it limits the search to O(logN).

#### AVL Tree Implementation

Since all new keys are inserted into the tree as leaf nodes and we know that the balance factor for a new leaf is zero, there are no new requirements for the node that was just inserted. But once the new leaf is added we must update the balance factor of its parent. How this new leaf affects the parent’s balance factor depends on whether the leaf node is a left child or a right child. If the new node is a right child the balance factor of the parent will be reduced by one. If the new node is a left child then the balance factor of the parent will be increased by one. This relation can be applied recursively to the grandparent of the new node, and possibly to every ancestor all the way up to the root of the tree. Since this is a recursive procedure let us examine the two base cases for updating balance factors:

- The recursive call has reached the root of the tree.
- The balance factor of the parent has been adjusted to zero. You should convince yourself that once a subtree has a balance factor of zero, then the balance of its ancestor nodes does not change.

### Summary of Map ADT Implementations

![image-20211027153743539](C:\Users\Yim\AppData\Roaming\Typora\typora-user-images\image-20211027153743539.png)

























































