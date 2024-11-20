import ply.lex as lex
import ply.yacc as yacc
from datetime import datetime

class Node:
    def __init__(self, data, date=None):
        self.data = data
        self.date = date
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, date):
        new_node = Node(data, date)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def pick_last(self):
        if not self.head:
            return None
        current = self.head
        while current.next:
            current = current.next
        return current.data

    def pick_range(self, start_date, end_date):
        results = []
        current = self.head
        while current:
            if start_date <= current.date <= end_date:
                results.append(current.data)
            current = current.next
        return results


# LinkedList instance
linked_list = LinkedList()

# Tokens
tokens = (
    'PICK', 'RANGE', 'LAST', 'INSERT', 'DATE', 'DATA', 'SEMICOLON'
)

# Token rules
t_PICK = r'pick'
t_RANGE = r'range'
t_LAST = r'last'
t_INSERT = r'insert'
t_SEMICOLON = r';'

# Define a regex for DATE and DATA
def t_DATE(t):
    r'\d{4}-\d{2}-\d{2}'  # e.g., "2024-11-01"
    try:
        t.value = datetime.strptime(t.value, "%Y-%m-%d")
    except ValueError:
        print(f"Invalid date format: {t.value}")
        t.value = None
    return t

def t_DATA(t):
    r'\"[a-zA-Z0-9\s]+\"'  # quoted string for data
    t.value = t.value.strip("\"")
    return t

# Ignored characters (whitespace)
t_ignore = ' \t'

# Error handling for lexer
def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Parsing rules
def p_statement_insert(p):
    'statement : INSERT DATA SEMICOLON'
    data = p[2]
    date = datetime.now()  # Current date for inserted data
    linked_list.insert(data, date)
    print(f"Inserted data '{data}' with date {date.strftime('%Y-%m-%d')}")

def p_statement_pick_last(p):
    'statement : PICK LAST SEMICOLON'
    result = linked_list.pick_last()
    if result:
        print(f"Last entry: {result}")
    else:
        print("List is empty")

def p_statement_pick_range(p):
    'statement : PICK RANGE DATE DATE SEMICOLON'
    start_date = p[3]
    end_date = p[4]
    results = linked_list.pick_range(start_date, end_date)
    if results:
        print("Entries between the given dates:")
        for result in results:
            print(result)
    else:
        print("No entries found in the given date range")

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()
# Insert a few entries
parser.parse('insert "First Entry";')
parser.parse('insert "Second Entry";')

# Pick the last entry
parser.parse('pick last;')

# Insert more entries with specific dates
linked_list.insert("Entry on Jan 1", datetime(2024, 1, 1))
linked_list.insert("Entry on Feb 1", datetime(2024, 2, 1))
linked_list.insert("Entry on Jan 5", datetime(2024, 1, 5))
linked_list.insert("Entry on Mar 1", datetime(2024, 3, 1))
linked_list.insert("Entry on Mar 2", datetime(2024, 3, 2))

# Pick range between two dates
parser.parse('pick range 2024-01-01 2024-02-15;')
