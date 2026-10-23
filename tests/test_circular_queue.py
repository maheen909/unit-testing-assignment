"""Unit tests for data_structures/queues/circular_queue.py (CircularQueue).

Run from the repository root:
    python -m pytest tests/test_circular_queue.py
"""

import csv
from pathlib import Path

import pytest

from data_structures.queues.circular_queue import CircularQueue

DATA_FILE = Path(__file__).parent / "data" / "circular_queue_data.csv"


def make_queue(capacity, items=()):
    cq = CircularQueue(capacity)
    for item in items:
        cq.enqueue(item)
    return cq


# --------------------------------------------------------------------------
# Function level: __init__
# --------------------------------------------------------------------------
@pytest.mark.function
@pytest.mark.init
@pytest.mark.order(1)
class TestInit:
    @pytest.mark.parametrize("capacity", [1, 2, 5, 100])
    def test_valid_capacity_creates_empty_queue(self, capacity):
        cq = CircularQueue(capacity)
        assert cq.n == capacity
        assert len(cq) == 0

    def test_array_is_preallocated_with_none(self):
        assert CircularQueue(3).array == [None, None, None]

    def test_front_and_rear_start_at_zero(self):
        cq = CircularQueue(4)
        assert (cq.front, cq.rear, cq.size) == (0, 0, 0)

    def test_zero_capacity_is_allowed_but_unusable(self):
        cq = CircularQueue(0)
        assert cq.array == []
        with pytest.raises(Exception, match="QUEUE IS FULL"):
            cq.enqueue("A")

    def test_non_integer_capacity_raises_type_error(self):
        with pytest.raises(TypeError):
            CircularQueue("5")


# --------------------------------------------------------------------------
# Function level: enqueue
# --------------------------------------------------------------------------
@pytest.mark.function
@pytest.mark.enqueue
@pytest.mark.order(2)
class TestEnqueue:
    def test_enqueue_returns_self_for_chaining(self):
        cq = CircularQueue(3)
        assert cq.enqueue("A") is cq

    def test_enqueue_increases_size(self):
        cq = make_queue(5, ["A", "B"])
        assert len(cq) == 2

    def test_first_element_stays_at_front(self):
        cq = make_queue(5, ["A", "B", "C"])
        assert cq.first() == "A"

    @pytest.mark.boundary
    def test_enqueue_until_exactly_full_is_allowed(self):
        cq = make_queue(3, ["A", "B", "C"])
        assert len(cq) == 3

    @pytest.mark.boundary
    def test_enqueue_beyond_capacity_raises(self):
        cq = make_queue(2, ["A", "B"])
        with pytest.raises(Exception, match="QUEUE IS FULL"):
            cq.enqueue("C")

    def test_failed_enqueue_does_not_change_size(self):
        cq = make_queue(1, ["A"])
        with pytest.raises(Exception):
            cq.enqueue("B")
        assert len(cq) == 1 and cq.first() == "A"

    @pytest.mark.parametrize("value", [0, -1, 3.14, "text", None, [1, 2], (1,), {"k": 1}])
    def test_enqueue_accepts_different_data_types(self, value):
        cq = CircularQueue(2).enqueue(value)
        assert len(cq) == 1


# --------------------------------------------------------------------------
# Function level: dequeue
# --------------------------------------------------------------------------
@pytest.mark.function
@pytest.mark.dequeue
@pytest.mark.order(3)
class TestDequeue:
    def test_dequeue_returns_oldest_element(self):
        assert make_queue(3, ["A", "B"]).dequeue() == "A"

    def test_dequeue_decreases_size(self):
        cq = make_queue(3, ["A", "B"])
        cq.dequeue()
        assert len(cq) == 1

    def test_fifo_order(self):
        cq = make_queue(4, [1, 2, 3, 4])
        assert [cq.dequeue() for _ in range(4)] == [1, 2, 3, 4]

    @pytest.mark.boundary
    def test_dequeue_on_empty_raises_underflow(self):
        with pytest.raises(Exception, match="UNDERFLOW"):
            CircularQueue(3).dequeue()

    @pytest.mark.boundary
    def test_dequeue_last_element_makes_queue_empty(self):
        cq = make_queue(3, ["A"])
        assert cq.dequeue() == "A"
        assert cq.is_empty()

    def test_dequeue_clears_slot(self):
        cq = make_queue(3, ["A", "B"])
        cq.dequeue()
        assert cq.array[0] is None

    def test_dequeue_after_emptying_raises_again(self):
        cq = make_queue(2, ["A"])
        cq.dequeue()
        with pytest.raises(Exception, match="UNDERFLOW"):
            cq.dequeue()


# --------------------------------------------------------------------------
# Function level: first
# --------------------------------------------------------------------------
@pytest.mark.function
@pytest.mark.first
@pytest.mark.order(4)
class TestFirst:
    def test_first_on_empty_returns_false(self):
        assert CircularQueue(3).first() is False

    def test_first_returns_front_without_removing(self):
        cq = make_queue(3, ["A", "B"])
        assert cq.first() == "A"
        assert len(cq) == 2

    def test_first_updates_after_dequeue(self):
        cq = make_queue(3, ["A", "B"])
        cq.dequeue()
        assert cq.first() == "B"

    def test_first_after_all_dequeued_returns_false(self):
        cq = make_queue(2, ["A"])
        cq.dequeue()
        assert cq.first() is False

    def test_first_is_stable_on_repeated_calls(self):
        cq = make_queue(3, ["A"])
        assert cq.first() == cq.first() == "A"


# --------------------------------------------------------------------------
# Function level: is_empty and __len__
# --------------------------------------------------------------------------
@pytest.mark.function
@pytest.mark.state
@pytest.mark.order(5)
class TestIsEmptyAndLen:
    def test_new_queue_is_empty(self):
        assert CircularQueue(3).is_empty() is True

    def test_queue_with_one_item_is_not_empty(self):
        assert make_queue(3, ["A"]).is_empty() is False

    def test_full_queue_is_not_empty(self):
        assert make_queue(2, ["A", "B"]).is_empty() is False

    def test_empty_again_after_dequeue(self):
        cq = make_queue(2, ["A"])
        cq.dequeue()
        assert cq.is_empty() is True

    @pytest.mark.parametrize("count", [0, 1, 2, 3])
    def test_len_matches_number_of_items(self, count):
        assert len(make_queue(3, range(count))) == count

    def test_len_after_mixed_operations(self):
        cq = make_queue(3, ["A", "B", "C"])
        cq.dequeue()
        cq.enqueue("D")
        assert len(cq) == 3


# --------------------------------------------------------------------------
# Class level: behaviour of the whole CircularQueue
# --------------------------------------------------------------------------
@pytest.mark.class_level
@pytest.mark.order(6)
class TestCircularQueueClass:
    def test_wrap_around_keeps_fifo_order(self):
        cq = make_queue(3, ["A", "B", "C"])
        assert cq.dequeue() == "A"
        cq.enqueue("D")
        assert [cq.dequeue() for _ in range(3)] == ["B", "C", "D"]

    def test_rear_wraps_to_zero(self):
        cq = make_queue(3, ["A", "B", "C"])
        assert cq.rear == 0

    def test_front_wraps_to_zero(self):
        cq = make_queue(2, ["A", "B"])
        cq.dequeue()
        cq.dequeue()
        assert cq.front == 0

    def test_fill_empty_refill_cycle(self):
        cq = make_queue(2, ["A", "B"])
        cq.dequeue()
        cq.dequeue()
        cq.enqueue("C").enqueue("D")
        assert (cq.dequeue(), cq.dequeue()) == ("C", "D")

    def test_capacity_one_queue(self):
        cq = CircularQueue(1).enqueue("A")
        with pytest.raises(Exception, match="QUEUE IS FULL"):
            cq.enqueue("B")
        assert cq.dequeue() == "A"
        assert cq.is_empty()

    def test_chained_enqueue_then_dequeue(self):
        assert CircularQueue(3).enqueue("A").enqueue("B").dequeue() == "A"

    def test_multiple_wrap_arounds(self):
        cq = CircularQueue(2)
        for i in range(10):
            cq.enqueue(i)
            assert cq.dequeue() == i
        assert cq.is_empty()


# --------------------------------------------------------------------------
# Data driven: test data comes from an external CSV file (Task 3)
# --------------------------------------------------------------------------
def load_csv_cases():
    with open(DATA_FILE, newline="") as f:
        return [
            pytest.param(row, id=row["tc_id"]) for row in csv.DictReader(f)
        ]


def run_operations(capacity, operations):
    """Run 'enq:X;deq;first' style operations and return the last output."""
    cq = CircularQueue(capacity)
    output = ""
    try:
        for op in operations.split(";"):
            if op.startswith("enq:"):
                cq.enqueue(op.split(":", 1)[1])
                output = ""
            elif op == "deq":
                output = str(cq.dequeue())
            elif op == "first":
                output = str(cq.first())
    except Exception as exc:
        output = f"ERR:{exc}"
    return cq, output


@pytest.mark.csv
@pytest.mark.order(7)
@pytest.mark.parametrize("row", load_csv_cases())
def test_circular_queue_from_csv(row):
    cq, output = run_operations(int(row["capacity"]), row["operations"])
    assert output == row["expected_output"]
    assert len(cq) == int(row["expected_size"])
