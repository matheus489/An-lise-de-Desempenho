class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def remove(self, position):
        if not self.head:
            return
        if position == 0:
            self.head = self.head.next
            return
        current_node = self.head
        for _ in range(position - 1):
            if current_node.next:
                current_node = current_node.next
            else:
                return
        if current_node.next:
            current_node.next = current_node.next.next

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()

# Função para executar as ações conforme o arquivo
def execute_actions(file_name):
    with open(file_name, 'r') as file:
        data = file.readline().strip().split()
        linked_list = LinkedList()
        for item in data:
            linked_list.append(int(item))

        num_actions = int(file.readline().strip())

        for _ in range(num_actions):
            action = file.readline().strip().split()
            if action[0] == 'A':
                number = int(action[1])
                position = int(action[2])
                if position == 0:
                    linked_list.head = Node(number)
                    linked_list.head.next = linked_list.head
                else:
                    current_node = linked_list.head
                    for _ in range(position - 1):
                        if current_node.next:
                            current_node = current_node.next
                        else:
                            return
                    new_node = Node(number)
                    new_node.next = current_node.next
                    current_node.next = new_node
            elif action[0] == 'R':
                position = int(action[1])
                linked_list.remove(position)
            elif action[0] == 'P':
                linked_list.print_list()

# Executando as ações conforme o arquivo arq.txt
execute_actions("D:/Faculdade/Analise/arq.txt")
