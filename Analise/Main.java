import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        executeActions("D:/Faculdade/Analise/arq-novo.txt");
    }

    // Método para executar as ações especificadas no arquivo
    static void executeActions(String fileName) {
        try {
            // Abre o arquivo
            File file = new File(fileName);
            Scanner scanner = new Scanner(file);

            // Lê a primeira linha do arquivo, que contém os dados iniciais para a lista encadeada
            String[] data = scanner.nextLine().strip().split(" ");
            LinkedList linkedList = new LinkedList();
            for (String item : data) {
                linkedList.append(Integer.parseInt(item)); // Adiciona os itens à lista encadeada
            }

            // Lê o número de ações a serem executadas
            int actionCount = Integer.parseInt(scanner.nextLine().strip());

            // Itera sobre cada ação especificada no arquivo
            for (int i = 0; i < actionCount; i++) {
                String line = scanner.nextLine().strip();
                if (line.isEmpty()) {
                    continue;  // Ignora linhas vazias
                }
                String[] action = line.split(" ");

                // Verifica e executa cada tipo de ação
                if (action.length < 3) {
                    continue;  // Ignora ações incompletas
                }
                if (action[0].equals("A")) { // Adiciona um elemento à lista
                    int number = Integer.parseInt(action[1]);
                    int position = Integer.parseInt(action[2]);
                    if (position == 0) {
                        Node newNode = new Node(number);
                        newNode.next = linkedList.head;
                        linkedList.head = newNode;
                    } else {
                        Node node = linkedList.head;
                        for (int j = 0; node != null && j < position - 1; j++) {
                            node = node.next;
                        }
                        if (node == null)
                            return;
                        Node newNode = new Node(number);
                        newNode.next = node.next;
                        node.next = newNode;
                    }
                } else if (action[0].equals("R")) { // Remove um elemento da lista
                    int position = Integer.parseInt(action[1]);
                    linkedList.remove(position);
                } else if (action[0].equals("P")) { // Imprime a lista
                    linkedList.printList();
                }
            }
            scanner.close(); // Fecha o scanner após o uso
        } catch (FileNotFoundException e) {
            e.printStackTrace(); // Trata exceção de arquivo não encontrado
        }
    }

    // Classe para representar um nó da lista encadeada
    static class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    // Classe para representar a lista encadeada
    static class LinkedList {
        Node head;

        LinkedList() {
            this.head = null;
        }

        // Método para adicionar um elemento ao final da lista
        void append(int data) {
            Node new_node = new Node(data);
            if (this.head == null) {
                this.head = new_node;
                return;
            }
            Node last_node = this.head;
            while (last_node.next != null) {
                last_node = last_node.next;
            }
            last_node.next = new_node;
        }

        // Método para remover um elemento da lista com base na posição
        void remove(int position) {
            if (this.head == null)
                return;
            if (position == 0) {
                this.head = this.head.next;
                return;
            }
            Node node = this.head;
            for (int i = 0; node != null && i < position - 1; i++) {
                node = node.next;
            }
            if (node == null || node.next == null)
                return;
            node.next = node.next.next;
        }

        // Método para imprimir a lista
        void printList() {
            Node node = this.head;
            while (node != null) {
                System.out.print(node.data + " ");
                node = node.next;
            }
            System.out.println();
        }
    }
}
