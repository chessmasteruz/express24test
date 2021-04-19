import unittest
from LinkedList import LinkedList, Node
from solve import list_sum

class TestSolve(unittest.TestCase):

    def l2ll(self, l):
        ll = LinkedList()
        for i in l:
            ll.pushBack(Node(i))
        return ll

    def test_ok(self):
        l1 = self.l2ll([2,4,3])
        l2 = self.l2ll([5,6,4])
        self.assertEqual(str(list_sum(l1, l2)), str([7,0,8]))

        l1 = self.l2ll([0])
        l2 = self.l2ll([0])
        self.assertEqual(str(list_sum(l1, l2)), str([0]))

        l1 = self.l2ll([9,9,9,9,9,9,9])
        l2 = self.l2ll([9,9,9,9])
        self.assertEqual(str(list_sum(l1, l2)), str([8,9,9,9,0,0,0,1]))

