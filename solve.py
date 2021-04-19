from LinkedList import LinkedList, Node

def list_sum(l1, l2):
    l1 = l1.reverse().getFront()
    l2 = l2.reverse().getFront()
    tmp = 0
    res = LinkedList()

    while l1 or l2 or tmp > 0:
        a = l1.getValue() if l1 else 0
        b = l2.getValue() if l2 else 0
        sum = a+b+tmp
        tmp = sum // 10
        sum %= 10
        res.pushBack(Node(sum))
        if l1:
            l1 = l1.getNext()
        if l2:
            l2 = l2.getNext()
    return res

if __name__ == '__main__':

    print("Input first list digits in one line:\n")
    a = input().split()

    print("Input second list digits in one line:\n")
    b = input().split()

    l1 = LinkedList()
    for i in a:
        l1.pushBack(Node(int(i)))

    l2 = LinkedList()
    for i in b:
        l2.pushBack(Node(int(i)))

    print("l1=", l1)
    print("l2=", l2)

    print("l1+l2=", list_sum(l1, l2))


