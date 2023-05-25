import pytest
from linked_list_kth.linked_list_kth import Node , LinkedList

def test_one():
    node_A=Node(0)
    node_M=Node(1,node_A)
    node_I=Node(2,node_M)
    ll_ =LinkedList(node_I)
    actual = ll_.Kth(1)
    expected = 1
    assert actual == expected
def test_two():
    node_A=Node(0)
    node_M=Node(1,node_A)
    node_I=Node(2,node_M)
    ll_ =LinkedList(node_I)
    actual = ll_.Kth(0)
    expected = 0
    assert actual == expected   
def test_three():
    node_A=Node(0)
    node_M=Node(1,node_A)
    node_I=Node(2,node_M)
    ll_ =LinkedList(node_I)
    with pytest.raises(Exception)as error :
     ll_.Kth(-1)
    assert str(error.value) == "index is negatev"   
def test_four():
    node_A=Node(0)
    node_M=Node(1,node_A)
    node_I=Node(2,node_M)
    ll_ =LinkedList(node_I)
    with pytest.raises(Exception)as error :
     ll_.Kth(6)
    assert str(error.value) == "index out of rang"       
def test_five():
    node_A=Node(0)
    # node_M=Node(1,node_A)
    # node_I=Node(2,node_M)
    ll_ =LinkedList(node_A)
    actual = ll_.Kth(0)
    expected = 0
    assert actual == expected     