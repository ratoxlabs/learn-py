# Todo List Applications

A collection of Python todo list applications demonstrating different programming concepts and file handling techniques.

## 📁 Project Structure

```
todo_list/
├── filebased_todo_list.py    # File-based persistent todo list
├── simple_todo_list.py       # In-memory todo list
├── my_tasks.txt             # Data file for file-based version
└── README.md                # This file
```

## 🚀 Applications

### 1. File-Based Todo List (`filebased_todo_list.py`)

A persistent todo list application that saves tasks to a text file, allowing data to persist between sessions.

#### Features
- ✅ Add new tasks
- 📋 Display all tasks with numbering
- 🗑️ Delete specific tasks by name
- 🧹 Clear all tasks
- 💾 Automatic file persistence
- 🔄 Load existing tasks on startup

#### Key Learning Concepts
- File I/O operations (`open()`, `read()`, `write()`)
- Context managers (`with` statement)
- Function definitions with parameters and return values
- List operations (`append()`, `remove()`)
- Error handling (`try/except` blocks)
- String manipulation (`strip()`, `splitlines()`)

#### Usage
```bash
python filebased_todo_list.py
```

#### File Format
Tasks are stored in `my_tasks.txt` with one task per line:
```
Learn Python basics
Complete project documentation
Review code for improvements
```

### 2. Simple Todo List (`simple_todo_list.py`)

An in-memory todo list application that demonstrates basic Python concepts without file persistence.

#### Features
- ✅ Add tasks to memory
- 📋 Display numbered task list
- 🗑️ Delete tasks by index number
- 🧹 Clear all tasks
- 🚪 Exit application

#### Key Learning Concepts
- Lists and list operations
- User input handling
- Control flow (`while`, `if/elif/else`)
- Type casting and validation
- Error handling for invalid inputs
- Menu-driven interfaces

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.x installed on your system
- No external dependencies required

### Running the Applications

1. **Clone or download** this repository
2. **Navigate** to the `todo_list` directory
3. **Run** either application:
   ```bash
   # File-based version (recommended)
   python filebased_todo_list.py
   
   # Simple in-memory version
   python simple_todo_list.py
   ```

## 📖 How to Use

### File-Based Todo List

1. **Start the application** - it will automatically load any existing tasks
2. **Choose from the menu:**
   - `1` - Add a new task
   - `2` - Display all current tasks
   - `3` - Delete a specific task (by name)
   - `4` - Clear all tasks
   - `5` - Exit the application

3. **Tasks are automatically saved** to `my_tasks.txt` after each operation

### Example Session
```
Welcome to your Todo List

1. Add Task
2. Display Tasks
3. Delete task
4. Clear All
5. Exit
Enter your choice: 1

Enter task title: Learn file handling in Python

1. Add Task
2. Display Tasks
3. Delete task
4. Clear All
5. Exit
Enter your choice: 2

Your tasks:
1. Learn file handling in Python
```

## 🔧 Technical Details

### File Operations
- **Reading**: Uses `open()` with read mode and `splitlines()` to parse tasks
- **Writing**: Uses `open()` with write mode and formatted strings
- **Error Handling**: Graceful handling of file not found scenarios

### Data Persistence
- Tasks are stored in plain text format
- One task per line for easy parsing
- Automatic creation of data file if it doesn't exist
- Empty lines are filtered out during read operations

### Code Structure
- **Modular functions** for read/write operations
- **Clear separation** of concerns
- **Consistent error handling** throughout
- **User-friendly** input validation

## 🎯 Learning Objectives

This project demonstrates:

### Python Fundamentals
- Variables and data types
- Lists and list methods
- String manipulation
- Input/output operations
- Control flow structures

### File Handling
- Opening files in different modes
- Reading and writing text files
- Using context managers (`with` statement)
- File path management
- Data persistence concepts

### Programming Best Practices
- Function decomposition
- Error handling
- User input validation
- Code organization
- Documentation and comments

### Advanced Concepts
- Type hints (in file-based version)
- List comprehensions
- Exception handling
- File I/O best practices

## 🐛 Error Handling

Both applications include robust error handling for:
- Invalid menu selections
- Non-numeric input when numbers are expected
- File I/O errors
- Empty or invalid task inputs
- Index out of range errors

## 📝 Future Enhancements

Potential improvements could include:
- Task priorities or categories
- Due dates for tasks
- Task completion status
- Search functionality
- Data export/import features
- GUI interface
- Database integration

## 🤝 Contributing

Feel free to fork this project and submit improvements or additional features!

## 📄 License

This project is open source and available under the MIT License.

---

**Happy coding!** 🐍✨