#!/usr/bin/python3
"""This is a module that implements a linked list"""


class Node:
    """
    This is an implementation of a list node

    Attributes:
        data(int): data to be inserted in list
        next_node: reference to a linked list node
    """

    def __init__(self, data, next_node=None):
        """
        Initializes an instance of a node class

        Args:
            data(int): int value to insert in node
            next_node: reference to a next node

        Raises:
            TypeError: if `data` is not an integer or
            next_node is not a Node object
        """
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """
            Gets the node data

            Returns:
            data(int): the int value
            """
            return self.__data

        @data.setter
        def data(self, value):
            """
            Sets the value for data

            Args:
                value(int): the node data to be inserted

            Raises:
                TypeError: if `value` is not an integer or
                next_node is not a Node object
            """
            if not isinstance(value, int):
                raise TypeError("data must be an integer")

            self.__data = value

        @property
        def next_node(self):
            """
            Gets the next_node of the Node object

            Returns:
                next_node: the reference to the next node
            """
            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            """
            Sets the next node of a give Node object

            Args:
                value(Node): sets a reference to a Node object

            Raises:
                TypeError: if `value` is not a Node object
            """
            if value is not None or not isinstance(value, Node):
                raise TypeError("next_node must be a Node object")

            self.__next_node = value


class SinglyLinkedList:
    """This is an implementation for a linked list

    Attributes:
        sorted_insert: a public method that inserts a node

    """

    def __init__(self):
        """
        Initializes an instance of a singly linked list

        Args:
            head: reference for the start of a linked list
        """
        self.head = None

    def sorted_insert(self, value):
        """
        method that inserts a node in a linked list in a sorted manner

        Args:
            value(int): node value to be inserted in list
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node

        else:
            temp = self.head
            while temp.next_node is not None and value > temp.next_node.data:
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """
        Prints all nodes of a linked list
        """
        if self.head is None:
            return "Empty list"

        temp = self.head
        list_str = ""
        while temp is not None:
            list_str += str(temp.data) + "\n"
            temp = temp.next_node

        return list_str.strip()
