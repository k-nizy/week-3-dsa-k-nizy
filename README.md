# Data Structures Implementation Lab
## Enterprise Web Development - Week 3 Assignment


## Repository Structure
```
data-structures-lab/
├── README.md                 # This file - your instructions
├── requirements.txt          # Python dependencies
├── .github/
│   └── workflows/
│       └── test.yml         # Auto-grading workflow
├── src/
│   ├── __init__.py
│   ├── stack.py             # Stack implementation (choose one)
│   ├── queue.py             # Queue implementation (choose one)  
│   └── linked_list.py       # Linked List implementation (choose one)
├── tests/
│   ├── __init__.py
│   ├── test_stack.py
│   ├── test_queue.py
│   └── test_linked_list.py
├── docs/
│   └── COMPLEXITY_ANALYSIS.md
└── examples/
    └── demo.py
```


## Learning Objectives
- Implement a core data structure from scratch in Python
- Analyze and document time complexity of operations
- Write comprehensive unit tests
- Connect implementation to enterprise web development scenarios
- Practice Git workflow and documentation


## Assignment Overview

### Step 1: Choose Your Data Structure
Select **ONE** data structure to implement:

- **Stack** (LIFO) - Browser history, function calls, undo operations
- **Queue** (FIFO) - Print jobs, request handling, BFS algorithms  
- **Linked List** - Dynamic data, implementing other structures

**Important:** Only implement the structure you choose. Leave other files as starter templates.

### Step 2: Implementation
Complete your chosen data structure following the provided template and TODO comments.

### Step 3: Testing & Documentation
- Run and complete unit tests
- Fill out complexity analysis documentation
- Update README with your chosen structure

### Step 4: Submission
- Commit your changes with clear messages
- Push to your repository



## Getting Started

### 1. Accept Assignment & Clone
```bash
# Accept the GitHub Classroom assignment link (provided by instructor)
# Clone your assigned repository
git clone https://github.com/your-classroom-org/data-structures-lab-yourusername.git
cd data-structures-lab-yourusername
```

### 2. Set Up Environment
```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Choose and Implement
- Open the file for your chosen data structure (e.g., `src/stack.py`)
- Follow TODO comments to complete implementation




## Implementation Templates

### Stack Template (`src/stack.py`)
```python
"""
Stack Implementation - Last In, First Out (LIFO)
Enterprise Use Case: Browser back button, undo operations, function call management
"""

class Stack:
    def __init__(self):
        """Initialize empty stack using Python list."""
        # TODO: Initialize internal storage
        pass
    
    def push(self, item):
        """
        Add item to top of stack.
        Time Complexity: O(1)
        
        Args:
            item: Element to add to stack
        """
        # TODO: Implement push operation
        pass
    
    def pop(self):
        """
        Remove and return top item from stack.
        Time Complexity: O(1)
        
        Returns:
            Top item from stack
        
        Raises:
            IndexError: If stack is empty
        """
        # TODO: Implement pop operation with error handling
        pass
    
    def peek(self):
        """
        Return top item without removing it.
        Time Complexity: O(1)
        
        Returns:
            Top item from stack
        
        Raises:
            IndexError: If stack is empty
        """
        # TODO: Implement peek operation
        pass
    
    def is_empty(self):
        """
        Check if stack is empty.
        Time Complexity: O(1)
        
        Returns:
            bool: True if stack is empty, False otherwise
        """
        # TODO: Implement empty check
        pass
    
    def size(self):
        """
        Get number of items in stack.
        Time Complexity: O(1)
        
        Returns:
            int: Number of items in stack
        """
        # TODO: Return stack size
        pass
    
    def __str__(self):
        """String representation of stack (top to bottom)."""
        # TODO: Implement string representation
        pass
```


## Testing Your Implementation

### Run Tests Locally
```bash
# Run tests for your chosen data structure
python -m pytest tests/test_stack.py -v      # For Stack
python -m pytest tests/test_queue.py -v     # For Queue  
python -m pytest tests/test_linked_list.py -v # For Linked List

# Run all tests
python -m pytest tests/ -v
```

### Test Structure Example (`tests/test_stack.py`)
```python
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
        # This test is already implemented - you need to make it pass!
        pass
    
    def test_empty_stack_operations(self):
        """Test operations on empty stack raise appropriate errors."""
        # TODO: Complete this test
        pass
    
    # Additional tests provided...
```


## Complexity Analysis

Complete `docs/COMPLEXITY_ANALYSIS.md` with your analysis:

```markdown
# Time Complexity Analysis

## Chosen Data Structure: [Your Choice]

### Operations Analysis

| Operation | Best Case | Average Case | Worst Case | Explanation |
|-----------|-----------|--------------|------------|-------------|
| Insert    | O(?)      | O(?)         | O(?)       | [Your explanation] |
| Delete    | O(?)      | O(?)         | O(?)       | [Your explanation] |
| Search    | O(?)      | O(?)         | O(?)       | [Your explanation] |
| Access    | O(?)      | O(?)         | O(?)       | [Your explanation] |

### Enterprise Web Development Use Case

**Scenario:** [Describe a specific web development scenario]

**Why this data structure:** [Explain why your choice is optimal]

**Performance Impact:** [How does this improve web application performance]

### Space Complexity
- **Space used:** O(?)
- **Explanation:** [Why does your implementation use this much space]
```


## Git Workflow

### Making Commits
```bash
# Stage your changes
git add src/stack.py                    # Your implementation
git add tests/test_stack.py            # Completed tests  
git add docs/COMPLEXITY_ANALYSIS.md    # Your analysis

# Commit with clear message
git commit -m "Implement Stack with push, pop, peek operations

- Add LIFO functionality with error handling
- Complete unit tests for edge cases  
- Document O(1) time complexity for all operations
- Include enterprise use case analysis"

# Push to GitHub
git push origin main
```

### Commit Message Guidelines
- Use present tense ("Add feature" not "Added feature")
- First line < 50 characters
- Include bullet points for multiple changes
- Reference any issues: "Fixes #1"


## Getting Help

### Common Issues
**ImportError:** Make sure you're in the correct directory and the virtual environment is activated.

**Tests failing:** Check that you've implemented all required methods exactly as specified in the template.

**GitHub Actions failing:** Ensure all files are committed and pushed to the repository.

### Resources
- [Python unittest documentation](https://docs.python.org/3/library/unittest.html)
- [Big O Cheat Sheet](https://www.bigocheatsheet.com/)
- Course video transcript (reference the specific algorithms and time complexities discussed)


### Update This Section
**My chosen data structure:** [Stack/Queue/LinkedList]

**Enterprise use case:** [Brief description of your chosen real-world scenario]

**Key insight:** [One thing you learned about performance trade-offs]


## Reflection Questions (Include in COMPLEXITY_ANALYSIS.md)
1. How does your implementation compare to Python's built-in `list` for your use case?
2. What trade-offs did you make between simplicity and performance?
3. When would you choose your data structure over alternatives in a web application?
4. What enterprise scenarios would benefit most from your implementation?
