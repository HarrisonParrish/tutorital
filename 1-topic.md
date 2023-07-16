# Tutorial on Stacks in Python

## Welcome to the Tutorial on Stacks in Python!

### Introduction

Hey there! Welcome to this tutorial where we'll dive into the exciting world of stacks in Python. Stacks are like virtual stacks of pancakes where you can only add or remove the top pancake. In this tutorial, we'll cover the basics of stacks, how to implement them in Python, and solve some cool problems using stacks. Before we get started, make sure you're already familiar with Python programming.

## Table of Contents

1. [Stack Overview](#stack-overview)
2. [Implementing a Stack in Python](#implementing-a-stack-in-python)
3. [Stack Operations](#stack-operations)
4. [Problem Solving with Stacks](#problem-solving-with-stacks)
5. [Conclusion and Next Steps](#conclusion-and-next-steps)

# 1. Stack Overview

So, what exactly is a stack? Well, imagine a stack of plates in a cafeteria. You can only add a plate to the top of the stack or remove the topmost plate. This "Last-In-First-Out" (LIFO) behavior defines a stack. In programming terms, a stack is a linear data structure that stores a collection of elements.

# 2. Implementing a Stack in Python

To implement a stack in Python, we can use the built-in list data type. It's super convenient! Here's how you can do it:

```python
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

3. Stack Operations

Let's go through some basic operations that you can perform on a stack:

push(item): Adds an item to the top of the stack.
pop(): Removes and returns the topmost item from the stack.
peek(): Returns the topmost item without removing it.
is_empty(): Checks if the stack is empty.
size(): Returns the number of elements in the stack.


4. Problem Solving with Stacks

Now, let's solve a problem to see how stacks can be useful in real-life scenarios!

Problem: Balanced Parentheses
You're given a string containing parentheses, and you need to determine if the parentheses are balanced or not. For example, the string "(())" has balanced parentheses, while the string "(()))" does not.



Solution:


def is_balanced_parentheses(expression):
    stack = Stack()
    for char in expression:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

# Testing the function
print(is_balanced_parentheses("(())"))  # Output: True
print(is_balanced_parentheses("(()))"))  # Output: False

Problem: Reverse String using a Stack
Write a Python function reverse_string that takes a string as input and uses a stack to reverse the characters in the string. The function should return the reversed string.

Example:


print(reverse_string("Hello, World!"))  # Output: "!dlroW ,olleH"
print(reverse_string("Python"))  # Output: "nohtyP"





Solution:
def reverse_string(string):
    stack = Stack()
    for char in string:
        stack.push(char)
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string
Now it's your turn to give it a try! Solve the problem and compare your solution with the provided solution above.

5. Conclusion and Next Steps

That's it for this tutorial on stacks in Python! We covered the basics of stacks, how to implement them using Python's list, and performed some cool operations. We even solved a problem involving balanced parentheses using stacks.

To further expand your knowledge, consider exploring more applications of stacks or learning about other data structures like queues and linked lists. Keep practicing and challenging yourself with coding problems. The more you code, the better you'll get!

Hope you enjoyed this tutorial! If you have any questions, feel free to reach out.

Link to the Welcome Page