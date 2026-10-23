def pytest_configure(config):
    for marker in (
        "function: tests for a single method",
        "class_level: tests for the whole class behaviour",
        "init: __init__ tests",
        "enqueue: enqueue tests",
        "dequeue: dequeue tests",
        "first: first tests",
        "state: is_empty and __len__ tests",
        "tail: insert_tail and delete_tail tests",
        "boundary: boundary value analysis tests",
        "csv: data-driven tests that read a CSV file",
    ):
        config.addinivalue_line("markers", marker)