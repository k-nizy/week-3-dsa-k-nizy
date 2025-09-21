#!/usr/bin/env python3
"""
Demo script for Stack implementation
Shows practical usage of the Stack data structure
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.stack import Stack

def browser_history_demo():
    """Demonstrate browser history using stack."""
    print("=== Browser History Demo ===")
    history = Stack()
    
    # Simulate user navigation
    pages = ["homepage", "products", "product-detail", "cart", "checkout"]
    
    print("User navigates through pages:")
    for page in pages:
        history.push(page)
        print(f"  Visited: {page} (History size: {history.size()})")
    
    print(f"\nCurrent page: {history.peek()}")
    print(f"History: {history}")
    
    # Simulate back button clicks
    print("\nUser clicks back button:")
    while not history.is_empty():
        current_page = history.pop()
        print(f"  Back to: {current_page}")
        if not history.is_empty():
            print(f"  Current page: {history.peek()}")
        else:
            print("  No more history!")

def undo_operations_demo():
    """Demonstrate undo operations using stack."""
    print("\n=== Undo Operations Demo ===")
    undo_stack = Stack()
    
    # Simulate text editor operations
    operations = [
        "Type 'Hello'",
        "Type ' World'", 
        "Bold text",
        "Change font size",
        "Add bullet points"
    ]
    
    print("User performs operations:")
    for op in operations:
        undo_stack.push(op)
        print(f"  {op}")
    
    print(f"\nUndo stack: {undo_stack}")
    
    # Simulate undo operations
    print("\nUser presses Ctrl+Z (undo):")
    while not undo_stack.is_empty():
        undone_op = undo_stack.pop()
        print(f"  Undid: {undone_op}")
        if not undo_stack.is_empty():
            print(f"  Next undo available: {undo_stack.peek()}")
        else:
            print("  No more operations to undo!")

if __name__ == "__main__":
    browser_history_demo()
    undo_operations_demo()