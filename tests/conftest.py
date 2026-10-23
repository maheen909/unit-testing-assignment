def pytest_configure(config):
    for marker in (
        "function: tests for a single method",
        "class_level: tests for the whole class behaviour",
        "init: __init__ tests",
        "enqueue: enqueue tests",
        "dequeue: dequeue tests",
        "first: first tests",
        "state: is_empty and __len__ tests",
        "boundary: boundary value analysis tests",
        "csv: data-driven tests that read a CSV file",
        "push: push tests",
        "pop: pop tests",
        "top: top tests",
        "tail: tail tests",
        "append: append tests",
        "prepend: prepend tests",
    ):
        config.addinivalue_line("markers", marker)