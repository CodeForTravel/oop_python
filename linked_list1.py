class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # will return the length of the list
    def get_length(self):
        current_node = self.head
        length = 0
        while current_node is not None:
            length += 1
            current_node = current_node.next
        return length

    # check if list is empty
    def is_empty(self):
        if self.head is None:
            return True
        return False

    # inserting a node at the end of the list
    def insert_at_end(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next
            last_node.next = new_node

    # inserting a node at the beginning of the list
    def insert_at_beginning(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp
            del temp

    # insert a node on a specific index position
    def insert_at(self, new_node, index):
        if index < 0 or index > self.get_length():
            print("Invalid Position")
            return
        if index == 0:
            self.insert_at_beginning(new_node)
            return

        current_node = self.head
        current_position = 0
        previous_node = None
        while True:
            if current_position == index:
                previous_node.next = new_node
                new_node.next = current_node
                break
            previous_node = current_node
            current_position += 1
            current_node = current_node.next

    # delete the last node of the list
    def delete_end_node(self):
        last_node = self.head
        while last_node.next is not None:
            # if last_node.next is None:
            #     previous_node.next = None
            previous_node = last_node
            last_node = last_node.next
        previous_node.next = None

    # delete the first node of the list
    def delete_first_node(self):
        if self.is_empty() is False:
            previous_head = self.head
            self.head = self.head.next
            previous_head.next = None
            del previous_head
        else:
            print("List is empty, Deletion failed")

    # delete a node at a specific position
    def delete_at(self, index):
        if index < 0 or index >= self.get_length():
            print("Invalid index position, Deletion failed")
            return
        if self.is_empty() is False:
            if index == 0:
                self.delete_first_node()
            elif index == self.get_length()-1:
                self.delete_end_node()
            else:
                current_position = 0
                current_node = self.head
                while True:
                    if current_position == index:
                        previous_node.next = current_node.next
                        current_node.next = None
                        break
                    previous_node = current_node
                    current_node = current_node.next
                    current_position += 1

    def print_nodes(self):
        if self.is_empty() is True:
            print("list is empty")
            return
        current_node = self.head
        node_string = ""
        while True:
            if current_node is None:
                print(node_string)
                break
            # print(current_node.data)
            node_string = f"{node_string}{current_node.data} --> " if current_node.next else f"{node_string}{current_node.data}"
            current_node = current_node.next


first_node = Node("First Node")
linked_list = LinkedList()
linked_list.insert_at_end(first_node)
second_node = Node("Second Node")
linked_list.insert_at_end(second_node)
third_node = Node("Third Node")
linked_list.insert_at_end(third_node)
fourth_node = Node("Fourth Node")
linked_list.insert_at_beginning(fourth_node)
linked_list.print_nodes()
print("=======================")
fourth_node = Node("Fifth Node")
linked_list.insert_at(fourth_node, 2)
linked_list.print_nodes()
print("=======================")
linked_list.delete_end_node()
linked_list.print_nodes()
print("=======================")
linked_list.delete_first_node()
linked_list.print_nodes()
print("=======================")
linked_list.delete_at(1)
linked_list.print_nodes()
