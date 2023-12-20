#!/usr/bin/python3
"""This module contains a class definition for
representing a node in linked list.
"""


class Node:
    """A class representing a node of linked list.

    This class is serving a functionality related to linked lists.

    Attributes:
    __data (int): the data of the node
    __next_node (Node): a link to next node
    """
    def __init__(self, data, next_node=None):
        """Initialize a Node instance.

        Args:
            data (int): The node data
            next_node (Node): the link to the next node. Defaults to None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of a node

        Returns:
            the data of the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """sets the value of the data of the node

        Args:
            value (int): the node data

        Raises:
            TypeError: if value is not int
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the value of the next node

        Returns:
            the value of the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the value of the next node

            Args:
                value (Node): the value of the next node

            Raises:
                TypeError: if value is not a Node object
        """
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """A class representing a singly linked list"""
    def __init__(self):
        """ initialize the head of the list"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position
        in the list (increasing order)

        Args:
            value (int): the node data to be added to linked list
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while(temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """Prints the list

        Returns:
            the items in list
        """
        rlist = []
        temp = self.__head
        while (temp is not None):
            rlist.append(str(temp.data))
            temp = temp.next_node
        return "\n".join(rlist)
