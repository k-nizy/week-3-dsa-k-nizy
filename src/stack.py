"""
Stack Implementation - Last In, First Out (LIFO)
Enterprise Use Case: Browser back button, undo operations, function call management
"""

class Stack:
    def __init__(self):
        """Initialize empty stack using Python list."""
        self.items = []
    
    def push(self, item):
        """
        Add item to top of stack.
        Time Complexity: O(1)
        
        Args:
            item: Element to add to stack
        """
        self.items.append(item)
    
    def pop(self):
        """
        Remove and return top item from stack.
        Time Complexity: O(1)
        
        Returns:
            Top item from stack
        
        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self.items.pop()
    
    def peek(self):
        """
        Return top item without removing it.
        Time Complexity: O(1)
        
        Returns:
            Top item from stack
        
        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("Cannot peek an empty stack")
        return self.items[-1]
    
    def is_empty(self):
        """
        Check if stack is empty.
        Time Complexity: O(1)
        
        Returns:
            bool: True if stack is empty, False otherwise
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Get number of items in stack.
        Time Complexity: O(1)
        
        Returns:
            int: Number of items in stack
        """
        return len(self.items)
    
    def __str__(self):
        """String representation of stack (top to bottom)."""
        return "Stack(top to bottom): " + str(self.items[::-1])