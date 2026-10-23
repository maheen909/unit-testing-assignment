# Test Design Notes - Module 1: Stack
File: data_structures/stacks/stack.py | Class: Stack
Test file: tests/test_stack.py

## push(data)
ECP:
- Valid: stack me jagah hai (size < limit) -> element add hota hai
- Invalid: stack full (size == limit) -> StackOverflowError
- Data types: int, str, None, list, float (generic stack, sab valid)
BVA (limit = 3):
- size 0 (min): push OK
- size limit-1 (2): push OK, stack full ho jata hai
- size limit (3): push -> StackOverflowError
- limit = 1 aur limit = 0 (extreme boundary)

## pop()
ECP:
- Valid: non-empty stack -> top element wapas, size 1 kam
- Invalid: empty stack -> StackUnderflowError
BVA:
- size 1 par pop -> stack empty ho jata hai
- size 0 par pop -> StackUnderflowError
- LIFO order check

## peek()
ECP: non-empty -> top element (hataya nahi jata); empty -> StackUnderflowError
BVA: size 1, size 0, full stack (size == limit)

## is_empty() / is_full() / size()
ECP: empty, partially filled, full
BVA: size 0, 1, limit-1, limit
Extra: Stack(0).is_full() == True (0 == 0); pop ke baad full stack full nahi rehta;
failed push/pop se size change nahi hoti

## __contains__(item)
ECP: item maujood, item absent, empty stack me search
BVA: sirf top element, sirf bottom element
Extra: string aur None search

## Class-level tests
- Push/pop ka poora workflow, LIFO order
- limit=0 jaisi extreme configuration
- __bool__ aur __str__ ka state ke saath sahi hona