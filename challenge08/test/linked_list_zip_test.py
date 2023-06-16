import pytest
from linked_list_zip.linked_list_zip import LinkedList,Node

def test1_zip():
    node1=Node(1)
    node3=Node(3,node1)
    node5=Node(5,node3)
    ll1=LinkedList(node5)
    node2=Node(2)
    node4=Node(4,node2)
    node6=Node(6,node4)
    ll2=LinkedList(node6)
    ll_=LinkedList()
   
    actual =ll_.zip(ll1, ll2)
    expected = [5, 6, 3, 4, 1, 2]
    assert actual == expected
# def test2_zip():
#     node1=Node(1)
#     node3=Node(3,node1)
#     node5=Node(5,node3)
#     ll1=LinkedList(node5)
#     ll2=LinkedList()
#     ll_=LinkedList()
   
#     actual =ll_.zip(ll1, ll2)
#     expected = [5,3,1]
#     assert actual == expected    

    # ll1 = linked_list([1, 2, 3])
    # ll2 = linked_list([])

    # expected_output = linked_list([1, 2, 3])

    # output = zip(ll1, ll2)

    # assert output == expected_output

    # ll1 = linked_list([])
    # ll2 = linked_list([4, 5, 6])

    # expected_output = linked_list([4, 5, 6])

    # output = zip(ll1, ll2)

    # assert output == expected_output
