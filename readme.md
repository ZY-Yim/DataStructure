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



