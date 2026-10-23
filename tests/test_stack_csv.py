import csv
from pathlib import Path

import pytest
from data_structures.stacks.stack import Stack

DATA_FILE = Path(__file__).parent / "data" / "stack_data.csv"


def load_rows():
    with open(DATA_FILE, newline="") as f:
        rows = []
        for r in csv.DictReader(f):
            rows.append(
                (
                    int(r["limit"]),
                    int(r["pushes"]),
                    int(r["expected_size"]),
                    r["expected_full"] == "True",
                )
            )
    return rows


@pytest.mark.parametrize("limit,pushes,expected_size,expected_full", load_rows())
def test_stack_size_and_full_from_csv(limit, pushes, expected_size, expected_full):
    s = Stack(limit)
    for i in range(pushes):
        s.push(i)
    assert s.size() == expected_size
    assert s.is_full() is expected_full