#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if (value is not None) and (not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            new_node.__next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            curent = self.__head
            while (curent.next_node is not None) and \
                  (curent.next_node.data < value):
                curent = curent.next_node
            new_node.next_node = curent.next_node
            curent.next_node = new_node

    def __str__(self):
        value = []
        current = self.__head
        while current is not None:
            value.append(str(current.data))
            current = current.next_node
        return '\n'.join(value)
