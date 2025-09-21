import pytest
from src.stack import Stack

class TestStack:
    def test_push_and_size(self):
        """Test pushing elements increases size correctly."""
        stack = Stack()
        assert stack.size() == 0
        
        stack.push(1)
        assert stack.size() == 1
        
        stack.push(2)
        assert stack.size() == 2
    
    def test_pop_lifo_order(self):
        """Test that pop follows Last In, First Out order."""
        stack = Stack()
        stack.push("first")
        stack.push("second")
        stack.push("third")
        
        assert stack.pop() == "third"
        assert stack.pop() == "second"
        assert stack.pop() == "first"
        assert stack.size() == 0
    
    def test_empty_stack_operations(self):
        """Test operations on empty stack raise appropriate errors."""
        stack = Stack()
        
        # Test pop on empty stack
        with pytest.raises(IndexError):
            stack.pop()
            
        # Test peek on empty stack
        with pytest.raises(IndexError):
            stack.peek()
    
    def test_peek_operation(self):
        """Test that peek returns top element without removing it."""
        stack = Stack()
        stack.push("bottom")
        stack.push("top")
        
        assert stack.peek() == "top"
        assert stack.size() == 2  # Size should remain unchanged
    
    def test_is_empty(self):
        """Test is_empty method."""
        stack = Stack()
        assert stack.is_empty() == True
        
        stack.push("item")
        assert stack.is_empty() == False
        
        stack.pop()
        assert stack.is_empty() == True
    
    def test_string_representation(self):
        """Test string representation of stack."""
        stack = Stack()
        assert "top to bottom" in str(stack)
        
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        # Should show top to bottom: 3, 2, 1
        representation = str(stack)
        assert "3" in representation
        assert "2" in representation
        assert "1" in representation
    
    def test_multiple_data_types(self):
        """Test stack with different data types."""
        stack = Stack()
        
        # Test with integers
        stack.push(42)
        assert stack.peek() == 42
        
        # Test with strings
        stack.push("hello")
        assert stack.peek() == "hello"
        
        # Test with lists
        stack.push([1, 2, 3])
        assert stack.peek() == [1, 2, 3]
        
        # Test with None
        stack.push(None)
        assert stack.peek() is None
    
    def test_large_stack(self):
        """Test stack performance with many elements."""
        stack = Stack()
        
        # Push 1000 elements
        for i in range(1000):
            stack.push(i)
        
        assert stack.size() == 1000
        assert stack.peek() == 999
        
        # Pop all elements and verify LIFO order
        for i in range(999, -1, -1):
            assert stack.pop() == i
        
        assert stack.is_empty()
    
    def test_error_messages(self):
        """Test that error messages are descriptive."""
        stack = Stack()
        
        with pytest.raises(IndexError, match="Cannot pop from an empty stack"):
            stack.pop()
            
        with pytest.raises(IndexError, match="Cannot peek an empty stack"):
            stack.peek()