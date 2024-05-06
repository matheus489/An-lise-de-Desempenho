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
        node = self.head
        for _ in range(position - 1):
            if node.next:
                node = node.next
            else:
                return
        if node.next:
            node.next = node.next.next

    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next
        print()

# Função para executar as ações conforme o 
def execute_actions(file_name):
    
    with open(file_name, 'r') as file:
        data = file.readline().strip().split()
        linked_list = LinkedList()
        for item in data:
            linked_list.append(int(item))

        Ação = int(file.readline().strip())

        for _ in range(Ação):
            Ação = file.readline().strip().split()
            if Ação[0] == 'A':
                number = int(Ação[1])
                Posição = int(Ação[2])
                if Posição == 0:
                    linked_list.head = Node(number)
                    linked_list.head.next = linked_list.head
                else:
                    node = linked_list.head
                    for _ in range(Posição - 1):
                        if node.next:
                            node = node.next
                        else:
                            return
                    new_node = Node(number)
                    new_node.next = node.next
                    node.next = new_node
            elif Ação[0] == 'R':
                Posição = int(Ação[1])
                linked_list.remove(Posição)
            elif Ação[0] == 'P':
                linked_list.print_list()
                

# Executando as ações conforme o arquivo arq.txt
execute_actions("D:/Faculdade/Analise/arq.txt")
