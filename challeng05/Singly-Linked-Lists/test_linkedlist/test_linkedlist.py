import pytest
from linkedlist.linkedlist import LinkedList,Node

# import fizz_buzz.factorial

def test_one():
    node_c=Node("{ c }")
    actual_value = node_c.value
    expected_value = "{ c }"
    #actual_next=node._next
    except_next=None
    assert actual_value == expected_value
    #assert actual_next == except_next
    
def test_two(node_c):
    node_b=Node("{ b }",node_c)
    actual_value = node_b.value
    expected_value = "{ b }"
    # actual_next=node_b._next
    except_next=node_c
    assert actual_value == expected_value
    # assert actual_next == except_next
    
def test_two(node_b):
    node_a=Node("{ a }",node_b)
    actual_value = node_a.value
    expected_value = "{ a }"
    # actual_next=node_b._next
    except_next=node_b
    assert actual_value == expected_value
    # assert actual_next == except_next
    
def test_three(node_a,node_b):
    head=LinkedList(node_a)
    actual_value = node_a.value
    expected_value = "{ a }"
    #actual_next=node._next
    except_next=node_b
    assert actual_value == expected_value
    #assert actual_next == except_next
    
def test_four():
    li_=LinkedList()
    actual_value=li_.traverse_return("{ k }")
    expected_value = False
    assert actual_value == expected_value
    
def test_five():
    li_=LinkedList()
    actual_value=li_.traverse_return("{ b }")
    expected_value = True
    assert actual_value == expected_value   
    
def test_six():
    li_=LinkedList()
    actual_value=li_.traverse_print()
    expected_value = "{ a } -> { b } -> { c } -> None"
    assert actual_value == expected_value      
    
