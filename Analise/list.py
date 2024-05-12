class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define a classe LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

    # Método para adicionar um nó ao final da lista
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Método para remover um nó da lista com base na posição
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

    # Método para imprimir a lista
    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next
        print()

# Função para executar as ações conforme o arquivo
def execute_actions(file_name):
    with open(file_name, 'r') as file:
        data = file.readline().strip().split()
        linked_list = LinkedList()
        for item in data:
            linked_list.append(int(item))

        action_count = int(file.readline().strip())

        for _ in range(action_count):
            line = file.readline().strip().split()
            if len(line) < 1:
                continue
            if line[0] == 'A' and len(line) >= 3:  # Adiciona um elemento à lista
                number = int(line[1])
                position = int(line[2])
                if position == 0:
                    linked_list.head = Node(number)
                    linked_list.head.next = linked_list.head
                else:
                    node = linked_list.head
                    for _ in range(position - 1):
                        if node.next:
                            node = node.next
                        else:
                            return
                    new_node = Node(number)
                    new_node.next = node.next
                    node.next = new_node
            elif line[0] == 'R' and len(line) >= 2:  # Remove um elemento da lista
                position = int(line[1])
                linked_list.remove(position)
            elif line[0] == 'P':  # Imprime a lista
                linked_list.print_list()

# Executando as ações conforme o arquivo
execute_actions("D:/Faculdade/Analise/arq-novo.txt")
