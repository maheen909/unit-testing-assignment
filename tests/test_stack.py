import pytest
from data_structures.stacks.stack import (
    Stack,
    StackOverflowError,
    StackUnderflowError,
)


# ---------- push() ----------
def test_push_adds_element():
    s = Stack(3)
    s.push(10)
    assert s.size() == 1
    assert s.peek() == 10


def test_push_until_full_boundary():
    s = Stack(3)
    for i in range(3):
        s.push(i)
    assert s.is_full()


def test_push_beyond_limit_raises_overflow():
    s = Stack(2)
    s.push(1)
    s.push(2)
    with pytest.raises(StackOverflowError):
        s.push(3)


def test_push_limit_one_boundary():
    s = Stack(1)
    s.push("a")
    with pytest.raises(StackOverflowError):
        s.push("b")


def test_push_limit_zero_always_overflow():
    s = Stack(0)
    with pytest.raises(StackOverflowError):
        s.push(1)


@pytest.mark.parametrize("value", [1, "text", None, [1, 2], 3.5])
def test_push_accepts_different_types(value):
    s = Stack(5)
    s.push(value)
    assert s.peek() == value


# ---------- pop() ----------
def test_pop_returns_top_element():
    s = Stack()
    s.push(-5)
    s.push(10)
    assert s.pop() == 10


def test_pop_follows_lifo_order():
    s = Stack()
    for i in [1, 2, 3]:
        s.push(i)
    assert [s.pop(), s.pop(), s.pop()] == [3, 2, 1]


def test_pop_single_element_makes_stack_empty():
    s = Stack()
    s.push(1)
    s.pop()
    assert s.is_empty()


def test_pop_empty_raises_underflow():
    with pytest.raises(StackUnderflowError):
        Stack().pop()


def test_pop_decreases_size():
    s = Stack()
    s.push(1)
    s.push(2)
    s.pop()
    assert s.size() == 1


# ---------- peek() ----------
def test_peek_returns_top_without_removing():
    s = Stack()
    s.push(7)
    assert s.peek() == 7
    assert s.size() == 1


def test_peek_empty_raises_underflow():
    with pytest.raises(StackUnderflowError):
        Stack().peek()


def test_peek_on_full_stack():
    s = Stack(2)
    s.push(1)
    s.push(2)
    assert s.peek() == 2


# ---------- class-level ----------
def test_new_stack_state():
    s = Stack()
    assert bool(s) is False
    assert s.is_empty() is True
    assert s.is_full() is False
    assert str(s) == "[]"


def test_stack_state_after_pushes():
    s = Stack(3)
    s.push(1)
    s.push(2)
    assert bool(s) is True
    assert str(s) == "[1, 2]"
    assert 2 in s
    assert 99 not in s


def test_full_workflow_fill_and_empty():
    s = Stack(3)
    for i in range(3):
        s.push(i)
    with pytest.raises(StackOverflowError):
        s.push(99)
    for _ in range(3):
        s.pop()
    assert s.is_empty()
    with pytest.raises(StackUnderflowError):
        s.pop()
        # ---------- is_empty() ----------
def test_is_empty_on_new_stack():
    assert Stack().is_empty() is True


def test_is_empty_after_push():
    s = Stack()
    s.push(1)
    assert s.is_empty() is False


def test_is_empty_after_push_and_pop():
    s = Stack()
    s.push(1)
    s.pop()
    assert s.is_empty() is True


# ---------- is_full() ----------
def test_is_full_on_new_stack():
    assert Stack(3).is_full() is False


def test_is_full_one_below_limit():
    s = Stack(3)
    s.push(1)
    s.push(2)
    assert s.is_full() is False   # limit-1 boundary


def test_is_full_at_limit():
    s = Stack(3)
    for i in range(3):
        s.push(i)
    assert s.is_full() is True    # limit boundary


# ---------- size() ----------
@pytest.mark.parametrize("count", [0, 1, 5, 10])
def test_size_after_n_pushes(count):
    s = Stack(10)
    for i in range(count):
        s.push(i)
    assert s.size() == count


def test_size_after_pop():
    s = Stack()
    s.push(1)
    s.push(2)
    s.pop()
    assert s.size() == 1


# ---------- __contains__ ----------
def test_contains_existing_item():
    s = Stack()
    s.push(10)
    assert 10 in s


def test_contains_missing_item():
    s = Stack()
    s.push(10)
    assert 20 not in s


def test_contains_on_empty_stack():
    assert 1 not in Stack()


def test_contains_bottom_and_top_elements():
    s = Stack()
    for i in [1, 2, 3]:
        s.push(i)
    assert 1 in s    # bottom
    assert 3 in s    # top
    # ---------- extra tests (apne likhe hue) ----------

# is_full(): limit 0 par stack shuru se hi full hai (0 == 0)
def test_is_full_with_zero_limit():
    assert Stack(0).is_full() is True


# is_full(): pop karne ke baad full stack dobara full nahi rehta
def test_is_full_false_after_pop_from_full_stack():
    s = Stack(2)
    s.push(1)
    s.push(2)
    s.pop()
    assert s.is_full() is False


# size(): overflow ke baad size nahi badhti
def test_size_unchanged_after_failed_push():
    s = Stack(1)
    s.push(1)
    with pytest.raises(StackOverflowError):
        s.push(2)
    assert s.size() == 1


# size(): khali stack par pop fail ho to size 0 hi rehti hai
def test_size_zero_after_failed_pop():
    s = Stack()
    with pytest.raises(StackUnderflowError):
        s.pop()
    assert s.size() == 0


# __contains__(): string search
def test_contains_string_item():
    s = Stack()
    s.push("hello")
    assert "hello" in s
    assert "world" not in s


# __contains__(): None bhi ek valid item hai
def test_contains_none_item():
    s = Stack()
    s.push(None)
    assert None in s