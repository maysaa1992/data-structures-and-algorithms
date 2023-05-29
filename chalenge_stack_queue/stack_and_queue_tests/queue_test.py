import pytest
from stack_and_queue.queue import Queue,Node


def test_one():
    queue_01= Queue()
    actual_value_back = queue_01.enqueue(1)
    expected_value_back = 1
    assert actual_value_back == expected_value_back
    
def test_two():
    queue_01= Queue()
    queue_01.enqueue(1)
    queue_01.enqueue(2)
    queue_01.enqueue(3)
    queue_01.enqueue(4)
    actual_value_back = queue_01.__str__()
    expected_value_back = "1 -> 2 -> 3 -> 4 -> None"
    assert actual_value_back == expected_value_back   
def test_three():
    queue_01= Queue()
    queue_01.enqueue(1)
    queue_01.enqueue(2)
    queue_01.enqueue(3)
    queue_01.enqueue(4)
    actual_value_back = queue_01.dequeue()
    expected_value_back = 1
    assert actual_value_back == expected_value_back 
def test_four():
    queue_01= Queue()
    queue_01.enqueue(1)
    queue_01.enqueue(2)
    queue_01.enqueue(3)
    queue_01.enqueue(4)
    actual_value_back = queue_01.peek()
    expected_value_back = 1
    assert actual_value_back == expected_value_back
def test_fiv():
    queue_01= Queue()
    queue_01.enqueue(1)
    queue_01.enqueue(2)
    queue_01.enqueue(3)
    queue_01.enqueue(4)
    queue_01.dequeue()
    queue_01.dequeue()
    queue_01.dequeue()
    queue_01.dequeue()
    actual_value_back = queue_01.is_empty()
    expected_value_back = True
    assert actual_value_back == expected_value_back     
def test_six():
    queue_01= Queue()
    actual_value_back = queue_01.is_empty()
    expected_value_back = True
    assert actual_value_back == expected_value_back 
def test_seven():
    queue_01= Queue()
    actual_value_back = queue_01.dequeue()
    expected_value_back = "This is an empty stack"
    assert actual_value_back == expected_value_back             
         
    