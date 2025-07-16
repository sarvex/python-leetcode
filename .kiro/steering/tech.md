# Technology Stack

## Language & Runtime
- **Python 3.x** - Primary implementation language
- Uses modern Python features including type hints (`typing` module)
- Compatible with Python 3.9+ (uses `list[int]` syntax instead of `List[int]`)

## Dependencies
- **Standard Library Only** - No external dependencies required
- Uses built-in modules: `typing`, `collections`, `heapq`, `bisect`, etc.
- Self-contained solutions that can run independently

## Development Tools
- Setup scripts provided for both Unix/Linux (`setup.sh`) and Windows (`setup.ps1`)
- No build system required - Python files can be executed directly

## Common Commands

### Setup
```bash
# Unix/Linux/macOS
chmod +x setup.sh
./setup.sh

# Windows PowerShell
.\setup.ps1
```

### Running Solutions
```bash
# Execute individual solution
python "0001.Two Sum.py"

# Run with Python interpreter
python3 -c "from solution_file import Solution; print(Solution().method_name(test_input))"
```

### Testing
- No formal test framework - solutions include inline examples in docstrings
- Manual testing through Python REPL or by modifying the solution files
- Each solution can be imported as a module for testing

## Code Execution
- Solutions are designed to work with LeetCode's online judge system
- Each file contains a `Solution` class with the required method signature
- No main execution block needed - focus on algorithm implementation