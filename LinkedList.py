class Node:
    _value = None
    _next = None

    def __init__(self, value):
        self._setValue(value)

    def _setValue(self, new_val):
        self._value = new_val

    def getValue(self):
        return self._value

    def _setNext(self, new_next):
        self._next = new_next

    def getNext(self):
        return self._next

    def __iter__(self):
        return NodeIterator(self)

    def __str__(self):
        return str((self.getValue(),self.getNext()))



class NodeIterator:
    _cur = None

    def __init__(self, node):
        self._cur = node

    def __next__(self):
        if not self._cur:
            raise StopIteration
        value = self._cur
        self._cur = self._cur.getNext()
        return value


class LinkedList:
    _first = None
    _last = None
    _count = 0

    def __init__(self, first: Node=None):
        if first:
            self._first = first
            l = list(first)
            self._last = l[-1]
            self._count = len(l)

    def __len__(self):
        return self._count

    #Если в списке есть хотя бы одна нода, пользуемся итератором ноды
    #иначе выдаем собственный next cо StopIteration
    def __iter__(self):
        if self._count > 0:
            return NodeIterator(self._first)
        return self

    def __next__(self):
        raise StopIteration

    def __str__(self):
        if self._count > 0:
            return str([a.getValue() for a in self])
        return str([])


    def insert(self, new_node: Node, elem: Node = None):
        if self._count == 0:
            self.__init__(new_node)
        elif elem:
            new_node._setNext(elem.getNext())
            elem._setNext(new_node)
            if elem == self._last:
                self._last = new_node
            self._count += 1
        else:
            new_node._setNext(self._first)
            self._first = new_node
            self._count += 1


    def pushBack(self, new_node: Node):
        self.insert(new_node, self._last)

    def pushFront(self, new_node: Node):
        self.insert(new_node)


    def remove(self, elem:Node):
        if self._count == 0:
            raise Exception('List is empty')

        if self._count == 1 and elem == self._first:
            self._first = None
            self._last = None

        elif elem == self._first:
            self._first = self._first.getNext()
        elif elem == self._last:
            l = list(self)
            self._last = l[-2]
            self._last._setNext(None)
        else:
            flag = False
            for el in self:
                if el.getNext() == elem:
                    flag = True
                    el._setNext(elem.getNext())
                    break
            if not flag:
                raise Exception('this element is not exist in LinkedList')
        self._count -=1

    def popBack(self):
        self.remove(self._last)

    def popFront(self):
        self.remove(self._first)

    def getFront(self):
        return self._first

    def getBack(self):
        return self._last

    def reverse(self):
        new_list = LinkedList()
        for l in self:
            new_list.pushFront(Node(l.getValue()))
        return new_list

