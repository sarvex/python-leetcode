# Project Structure

## File Organization

### Naming Convention
- Files follow the pattern: `{problem_number}.{Problem Title}.py`
- Examples: `0001.Two Sum.py`, `0002.Add Two Numbers.py`
- Problem numbers are zero-padded to 4 digits for proper sorting
- Spaces and special characters in titles are preserved from LeetCode

### Root Directory Layout
```
├── 0001.Two Sum.py                    # Individual problem solutions
├── 0002.Add Two Numbers.py
├── ...
├── 3500+.{Problem Title}.py           # 3500+ problems total
├── setup.sh                           # Unix setup script
├── setup.ps1                          # Windows setup script
├── LICENSE                            # MIT License
└── .kiro/                            # Kiro configuration
    └── steering/                      # AI assistant guidance
```

## Code Structure Standards

### File Template
Each solution file follows this structure:
```python
from typing import Optional, List  # Import type hints as needed

# Data structure definitions (if required)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def methodName(self, params) -> return_type:
        """
        Problem description and approach.
        
        Intuition:
        Brief explanation of the core insight.
        
        Approach:
        Step-by-step algorithm explanation.
        
        Complexity:
        Time: O(n) - explanation
        Space: O(1) - explanation
        """
        # Implementation here
        pass
```

### Documentation Requirements
- **Docstring**: Every solution method must include comprehensive documentation
- **Intuition**: High-level approach explanation
- **Approach**: Detailed step-by-step algorithm
- **Complexity Analysis**: Both time and space complexity with explanations
- **Inline Comments**: Key algorithmic steps and edge cases

### Code Conventions
- Use descriptive variable names (`left`, `right`, `max_length` vs `l`, `r`, `ml`)
- Include type hints for all method parameters and return values
- Follow PEP 8 style guidelines
- Prefer clarity over brevity in algorithm implementation
- Use standard library data structures when appropriate (`collections.deque`, `heapq`, etc.)

## Problem Categories
Solutions cover all major algorithmic topics:
- Array/String manipulation (0001-0100+)
- Linked Lists (0002, 0019, 0021+)
- Trees and Graphs (0094, 0100+)
- Dynamic Programming (0053, 0070+)
- Sorting and Searching (0033, 0034+)
- Math and Bit Manipulation (0007, 0009+)
- Database problems (SQL solutions in .py format)