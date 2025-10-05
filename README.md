# Python Todo List

A simple command-line todo list application written in Python to demonstrate basic programming concepts.

## Features

- Add new tasks to your list
- Display all current tasks
- Delete specific tasks by number
- Clear all tasks at once
- Interactive menu-driven interface

## Learning Objectives

This project demonstrates the following Python concepts:
- Lists and list operations (`append`, `pop`, `clear`)
- User input handling with `input()`
- String formatting with f-strings
- Error handling with `try/except` blocks
- Type casting (`int()`)
- Chained comparisons
- Control flow with `while` loops and `if/elif/else` statements

## How to Run

1. Make sure you have Python installed on your system
2. Navigate to the project directory
3. Run the application:
   ```bash
   python todo-list.py
   ```

## Usage

When you run the application, you'll see a menu with the following options:

1. **Add Task** - Enter a new task to add to your list
2. **Display Tasks** - Show all current tasks with numbers
3. **Delete Task** - Remove a specific task by entering its number
4. **Clear All** - Remove all tasks from the list
5. **Exit** - Quit the application

## Error Handling

The application includes robust error handling for:
- Invalid menu selections
- Non-numeric input when numbers are expected
- Task numbers that don't exist
- Empty input fields

## Example Session

```
Welcome to your Todo List

1. Add Task
2. Display Tasks
3. Delete task
4. Clear All
5. Exit

Select option: 1

Enter Task Title: Learn Python basics
Current tasks: ['Learn Python basics']

Select option: 2

Current Tasks:
1. Learn Python basics
```

## Requirements

- Python 3.x
- No external dependencies required
