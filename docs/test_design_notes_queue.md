# Test Design Notes: CircularQueue (Queue module)

Module under test: `data_structures/queues/circular_queue.py`
Test file: `tests/test_circular_queue.py`
Test data: `tests/data/circular_queue_data.csv`

## Functions and their behaviour

| Function | Input | Output / Behaviour |
|---|---|---|
| `__init__(n)` | capacity `n` (int) | creates empty queue, `array = [None]*n` |
| `enqueue(data)` | any value | adds at rear, returns `self`; raises `Exception("QUEUE IS FULL")` if size >= n |
| `dequeue()` | none | removes and returns front; raises `Exception("UNDERFLOW")` if empty |
| `first()` | none | returns front element, or `False` if empty |
| `is_empty()` | none | `True` if size == 0 |
| `__len__()` | none | current size |

## Equivalence Class Partitioning (ECP)

| Function | Valid classes | Invalid classes |
|---|---|---|
| `__init__` | n > 0 (1, 2, 5, 100) | n is a string (TypeError) |
| `enqueue` | queue not full; value of any type (int, str, None, list, dict...) | queue full |
| `dequeue` | queue has >= 1 element | queue empty |
| `first` | non-empty queue | empty queue (returns False) |
| `is_empty` | empty queue, non-empty queue, full queue | none |
| `__len__` | 0, partially filled, full | none |

## Boundary Value Analysis (BVA)

| Where | Boundary values tested |
|---|---|
| Capacity | 0, 1, 2 (minimum capacities) |
| Enqueue count | capacity - 1, capacity (exactly full), capacity + 1 (overflow) |
| Dequeue count | 0 elements (underflow), 1 element (becomes empty), last element |
| Index wrap | rear reaches n and wraps to 0, front reaches n and wraps to 0 |
| Size | 0, 1, n-1, n |

## State based / scenario testing

- Fill, empty, refill cycle
- Repeated enqueue/dequeue 10 times on capacity 2 (many wrap-arounds)
- Chained calls: `enqueue("A").enqueue("B").dequeue()`
- Failed enqueue must not change the queue state

## Observations (possible defects / design issues)

1. `first()` returns `False` on an empty queue instead of raising an error, so a queue that really stores `False` cannot be told apart from an empty one.
2. The class raises a generic `Exception`, not a specific exception type.
3. `CircularQueue(0)` is accepted but can never store anything.
4. `CircularQueue(-1)` is silently accepted because `[None] * -1` gives an empty list.

## Test groups (pytest markers) and execution order

| Order | Group / marker | Class | Tests |
|---|---|---|---|
| 1 | `init` | TestInit | 8 |
| 2 | `enqueue` | TestEnqueue | 14 |
| 3 | `dequeue` | TestDequeue | 7 |
| 4 | `first` | TestFirst | 5 |
| 5 | `state` | TestIsEmptyAndLen | 9 |
| 6 | `class_level` | TestCircularQueueClass | 7 |
| 7 | `csv` | test_circular_queue_from_csv | 8 |

Other markers: `function` (all method level tests), `boundary` (BVA tests).

## How to run

```
pip install pytest pytest-xdist pytest-order

# all tests, in defined order
python -m pytest tests/test_circular_queue.py

# in parallel
python -m pytest tests/test_circular_queue.py -n auto

# one suite
python -m pytest tests/test_circular_queue.py -m function
python -m pytest tests/test_circular_queue.py -m class_level
python -m pytest tests/test_circular_queue.py -m boundary
python -m pytest tests/test_circular_queue.py -m csv
```

Note: execution order is guaranteed when running on one process. With `-n`, tests are spread over workers, so the order is kept only inside each worker.
