# DDSQL : Query Processor with Linked List and Query Processor with B+ Tree

## Overview

This project implements a system combining three key components:
1. **Linked List with Date Filtering** - A Python implementation of a linked list with date-based operations.
2. **PLY-Based Parser** - A lexical analyzer and parser for custom commands (e.g., `insert`, `pick last`, `pick range`).
3. **B+ Tree Query Processor** - A basic query executor with support for simple SQL-like commands, backed by a B+ Tree data structure for storage and search operations.

## Features

### Linked List
- **Insertion with Timestamps:** Add data nodes with current or custom timestamps.
- **Retrieve Last Entry:** Fetch the last data entry.
- **Date Range Queries:** Retrieve all entries within a specified date range.

### PLY Parser
- **Custom Commands:**
  - `insert "data";` - Adds data to the linked list with the current date.
  - `pick last;` - Fetches the most recent data entry.
  - `pick range YYYY-MM-DD YYYY-MM-DD;` - Retrieves entries within a date range.

### B+ Tree Query Processor
- **Table Creation:** Dynamically create tables backed by a B+ Tree.
- **Data Insertion:** Insert key-value pairs into tables.
- **Query Execution:** Process SQL-like commands to fetch results based on conditions.
  - Supported syntax: `SELECT field FROM table WHERE field = value`.

---

## Setup

1. **Install Dependencies**  
   Install `ply` for lexical analysis and parsing:
   ```bash
   pip install ply
   ```

2. **Run the Program**
   The project includes a `main()` function for demonstrating the query processor:
   ```bash
   python script_name.py
   ```

---

## Usage

### Linked List Commands
```python
# Insert data
parser.parse('insert "Sample Data";')

# Pick last entry
parser.parse('pick last;')

# Pick entries in a date range
parser.parse('pick range 2024-01-01 2024-02-15;')
```

### Query Processor
```python
executor = QueryExecutor()

# Create a table
users_table = executor.create_table('users')

# Insert data
users_table.insert(1, {'id': 1, 'name': 'Alice', 'age': 25})
users_table.insert(2, {'id': 2, 'name': 'Bob', 'age': 30})

# Execute queries
result = executor.execute_query("SELECT name FROM users WHERE id = 2")
print(result)  # Output: {'name': 'Bob'}
```

---

## Examples

### Linked List Example
```python
parser.parse('insert "Hello World";')
parser.parse('pick last;')  # Output: Last entry: Hello World
parser.parse('pick range 2023-12-01 2024-01-01;')  # Output: No entries found in the given date range
```

### Query Processor Example
```python
executor = QueryExecutor()
users_table = executor.create_table('users')
users_table.insert(1, {'id': 1, 'name': 'Alice'})
result = executor.execute_query("SELECT name FROM users WHERE id = 1")
print(result)  # Output: {'name': 'Alice'}
```

---

## Code Structure

1. **`LinkedList` Class**
   - Manages the linked list operations (`insert`, `pick_last`, `pick_range`).
   
2. **PLY Lexer and Parser**
   - Processes custom commands for interacting with the linked list.

3. **`BPlusTree` and QueryExecutor**
   - Implements a simple B+ Tree for storage and retrieval.
   - Parses and executes SQL-like queries.

---

## License
This project is open-source and available under the MIT License.