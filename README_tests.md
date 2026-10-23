# How to run the tests

Setup:

    python -m venv venv
    venv\Scripts\activate
    pip install pytest pytest-xdist pytest-order

Run all Stack tests:

    pytest tests/test_stack.py tests/test_stack_csv.py -v

Run by group:

    pytest tests/test_stack.py -m smoke
    pytest tests/test_stack.py -m boundary
    pytest tests/test_stack_csv.py -m csv

Run in parallel:

    pytest tests/test_stack.py tests/test_stack_csv.py -n 2

Execution order:

    Some tests use @pytest.mark.order(n), so they run first in the given order.