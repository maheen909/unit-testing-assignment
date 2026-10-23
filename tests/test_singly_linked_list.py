import csv
from pathlib import Path

import pytest

from data_structures.linked_list.singly_linked_list import SinglyLinkedList

DATA_FILE = Path(__file__).parent / "data" / "singly_linked_list_data.csv"


# --------------------------------------------------------------------------
# AAPKA PORTION: __init__, insert_head, delete_head
# --------------------------------------------------------------------------
@pytest.mark.function
@pytest.mark.init
@pytest.mark.order(1)
class TestInitAndHeadOps:
    def test_init_creates_empty_list(self):
        sll = SinglyLinkedList()
        assert sll.is_empty() is True
        assert len(sll) == 0

    def test_insert_head_single_element(self):
        sll = SinglyLinkedList()
        sll.insert_head(10)
        assert sll.head.data == 10
        assert len(sll) == 1

    def test_insert_head_multiple_elements(self):
        sll = SinglyLinkedList()
        sll.insert_head(10)
        sll.insert_head(20)
        assert sll.head.data == 20
        assert len(sll) == 2

    @pytest.mark.boundary
    def test_delete_head_empty_raises_error(self):
        sll = SinglyLinkedList()
        with pytest.raises(IndexError, match="List is empty"):
            sll.delete_head()

    def test_delete_head_single_element(self):
        sll = SinglyLinkedList()
        sll.insert_head(5)
        val = sll.delete_head()
        assert val == 5
        assert sll.is_empty() is True


# --------------------------------------------------------------------------
# PARTNER KA PORTION: insert_tail, delete_tail, state
# --------------------------------------------------------------------------
@pytest.mark.function
@pytest.mark.tail
@pytest.mark.order(2)
class TestTailOpsAndState:
    def test_insert_tail_empty_list(self):
        sll = SinglyLinkedList()
        sll.insert_tail("A")
        assert sll.head.data == "A"
        assert len(sll) == 1

    def test_insert_tail_multiple_elements(self):
        sll = SinglyLinkedList()
        sll.insert_tail("A")
        sll.insert_tail("B")
        assert sll.head.next.data == "B"
        assert len(sll) == 2

    @pytest.mark.boundary
    def test_delete_tail_empty_raises_error(self):
        sll = SinglyLinkedList()
        with pytest.raises(IndexError, match="List is empty"):
            sll.delete_tail()

    def test_delete_tail_multi_element(self):
        sll = SinglyLinkedList()
        sll.insert_tail(1)
        sll.insert_tail(2)
        val = sll.delete_tail()
        assert val == 2
        assert len(sll) == 1

    @pytest.mark.parametrize("items", [[], [1], [1, 2, 3]])
    def test_len_matches_items_count(self, items):
        sll = SinglyLinkedList()
        for item in items:
            sll.insert_tail(item)
        assert len(sll) == len(items)


# --------------------------------------------------------------------------
# CSV Data Driven Tests (Task 3)
# --------------------------------------------------------------------------
def load_csv_cases():
    with open(DATA_FILE, newline="") as f:
        return [pytest.param(row, id=row["tc_id"]) for row in csv.DictReader(f)]


@pytest.mark.csv
@pytest.mark.order(3)
@pytest.mark.parametrize("row", load_csv_cases())
def test_singly_linked_list_from_csv(row):
    sll = SinglyLinkedList()
    ops = row["operations"].split(";")
    output = ""
    try:
        for op in ops:
            if op.startswith("in_h:"):
                sll.insert_head(op.split(":")[1])
            elif op.startswith("in_t:"):
                sll.insert_tail(op.split(":")[1])
            elif op == "del_h":
                output = str(sll.delete_head())
            elif op == "del_t":
                output = str(sll.delete_tail())
    except Exception as exc:
        output = f"ERR:{exc}"

    assert output == row["expected_output"]
    assert len(sll) == int(row["expected_size"])