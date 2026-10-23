"""Registers the pytest markers used by test_circular_queue.py.

Markers are added here so they work with the repository's existing pytest
configuration and do not clash with the markers used for the stack tests.
"""


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
    ):
        config.addinivalue_line("markers", marker)
