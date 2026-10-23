# Test Design Notes - Module 3: Singly Linked List

File tested: data_structures/linked_list/singly_linked_list.py
Test file: tests/test_singly_linked_list.py

## Equivalence Class Partitioning (ECP) & Boundary Value Analysis (BVA)

### 1. Operations on Empty List
- ECP Valid: Operations like is_empty() returning True.
- ECP Invalid / BVA: Calling delete_head() or delete_tail() on an empty list.

### 2. Insert Head / Insert Tail
- ECP Valid: Insertion into an empty list, single-element list, and multi-element list.
- BVA: Inserting at boundary positions (index 0, last index, out-of-bound index).

### 3. Deletion & Search
- ECP Valid: Deleting existing nodes, searching for elements present in the list.
- ECP Invalid: Deleting non-existent values, searching for items not in the list.