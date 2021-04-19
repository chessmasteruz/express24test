import unittest
from LinkedList import LinkedList, Node

class TestNode(unittest.TestCase):

    def setUp(self):
        self.node = Node(0)
        self.node2 = Node(1)

    def test_value(self):
        for i in range(5):
            self.node._setValue(i)
            self.assertEqual(self.node.getValue(), i)

    def test_next(self):

        self.node._setNext(self.node2)

        for i in range(5):
            self.node2._setValue(i)
            self.assertEqual(self.node.getNext().getValue(), i)

        self.assertEqual(self.node2.getNext(), None)


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.mylist = LinkedList()
        self.mylist2 = LinkedList(Node(5))

    def test_init(self):
        self.assertEqual(self.mylist.getFront(), None)
        self.assertEqual(self.mylist.getBack(), None)
        self.assertEqual(len(self.mylist), 0)

        self.assertEqual(self.mylist2.getFront().getValue(), 5)
        self.assertEqual(self.mylist2.getBack().getValue(), 5)
        self.assertEqual(len(self.mylist2), 1)

    def test_iter(self):
        self.assertEqual(len(list(self.mylist)), 0)

        l2 = list(self.mylist2)
        self.assertEqual(len(l2), 1)
        self.assertEqual(l2[0].getValue(), 5)

    def test_insert_delete(self):


        self.mylist.pushBack(Node(1))
        self.assertEqual(self.mylist.getFront().getValue(), 1)
        self.assertEqual(self.mylist.getBack().getValue(), 1)
        self.assertEqual(len(self.mylist), 1)

        self.mylist.popBack()
        self.assertEqual(self.mylist.getFront(), None)
        self.assertEqual(self.mylist.getBack(), None)
        self.assertEqual(len(self.mylist), 0)

        self.mylist.pushFront(Node(1))
        self.assertEqual(self.mylist.getFront().getValue(), 1)
        self.assertEqual(self.mylist.getBack().getValue(), 1)
        self.assertEqual(len(self.mylist), 1)

        self.mylist.popFront()
        self.assertEqual(self.mylist.getFront(), None)
        self.assertEqual(self.mylist.getBack(), None)
        self.assertEqual(len(self.mylist), 0)

        for i in range(3):
            self.mylist.insert(Node(i))
        self.assertEqual(len(self.mylist), 3)

        e3 = self.mylist.getBack()
        self.assertEqual(e3.getValue(), 0)

        for i in range(3):
            self.mylist.insert(Node(i), e3)
        self.assertEqual(len(self.mylist), 6)

        self.mylist.remove(e3)
        self.assertEqual(len(self.mylist), 5)
        self.assertEqual(str(self.mylist), str([2,1,2,1,0]))


    def test_reverse(self):
        for i in range(3):
            self.mylist.pushBack(Node(i))

        print(self.mylist)
        self.assertEqual(len(self.mylist), 3)
        rev = self.mylist.reverse()
        self.assertEqual(str(rev), str([2,1,0]))


if __name__ == "__main__":
  unittest.main()