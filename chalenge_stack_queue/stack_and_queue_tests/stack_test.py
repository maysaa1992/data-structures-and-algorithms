import pytest
from stack_and_queue.stack import Stack,Node


def test_one():
    stack_01= Stack()
    actual_value = stack_01.push(1)
    expected_value = 1
    assert actual_value == expected_value
def test_two():
    stack_01= Stack()
    stack_01.push(1)
    stack_01.push(2)
    stack_01.push(3)
    stack_01.push(4)
    actual_value=stack_01.__str__()
    expected_value = "4 -> 3 -> 2 -> 1 -> None"
    assert actual_value == expected_value   
     
def test_three():
    stack_01= Stack()
    stack_01.push(1)
    stack_01.push(2)
    stack_01.push(3)
    stack_01.push(4)
    actual_value = stack_01.pop()
    expected_value = 4
    assert actual_value == expected_value 
def test_four():
    stack_01= Stack()
    stack_01.push(1)
    stack_01.push(2)
    stack_01.push(3)
    stack_01.push(4)
    stack_01.pop()
    stack_01.pop()
    stack_01.pop()
    stack_01.pop()
    actual_value = stack_01.isEmpty()
    expected_value = True
    assert actual_value == expected_value    
    
def test_five():
    stack_01= Stack()
    actual_value = stack_01.isEmpty()
    expected_value = True
    assert actual_value == expected_value   

def test_six():
    stack_01= Stack()
    actual_value = stack_01.pop()
    expected_value = "This is an empty stack"
    assert actual_value == expected_value 
         
def test_seven():
    stack_01= Stack()
    stack_01.push(1)
    stack_01.push(2)
    stack_01.push(3)
    stack_01.push(4)
    stack_01.pop()
    actual_value = stack_01.peek() 
    expected_value = 3
    assert actual_value == expected_value 