# Test Design Notes - Module 1: Stack

File tested: data_structures/stacks/stack.py (class Stack, default limit 10)
Test file: tests/test_stack.py

## push(data)
- Valid class: stack has room (size < limit), element gets added.
- Invalid class: stack is full (size == limit), raises StackOverflowError.
- Data types: int, str, None, list, float all work since the stack is generic.
- Boundaries (limit = 3): push at size 0, at size 2 (becomes full), at size 3 (error). Also limit 1 and limit 0.

## pop()
- Valid class: non-empty stack returns top element, size goes down by 1.
- Invalid class: empty stack raises StackUnderflowError.
- Boundaries: size 1 (becomes empty), size 0 (error). Checked LIFO order with 3 elements.

## peek()
- Non-empty: returns top without removing it.
- Empty: raises StackUnderflowError.
- Boundaries: size 1, size 0, full stack.

## is_empty(), is_full(), size()
- Classes: empty, partly filled, full.
- Boundaries: size 0, 1, limit-1, limit.
- Extra checks: Stack(0).is_full() is True because 0 == 0. A full stack is not full after pop. A failed push or pop does not change the size.

## __contains__(item)
- Classes: item present, item missing, empty stack.
- Boundaries: item at the bottom, item at the top.
- Extra: searching for a string and for None.

## Whole class
- Fill the stack, try overflow, empty it, try underflow.
- limit = 0 edge case.
- __bool__ and __str__ match the stack state.