import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        executeActions("D:/Faculdade/Analise/arq.txt");
    }

    static void executeActions(String fileName) {
        try {
            File file = new File(fileName);
            Scanner scanner = new Scanner(file);
            String[] data = scanner.nextLine().strip().split(" ");
            LinkedList linkedList = new LinkedList();
            for (String item : data) {
                linkedList.append(Integer.parseInt(item));
            }

            int actionCount = Integer.parseInt(scanner.nextLine().strip());

            for (int i = 0; i < actionCount; i++) {
                String[] action = scanner.nextLine().strip().split(" ");
                if (action[0].equals("A")) {
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
                } else if (action[0].equals("R")) {
                    int position = Integer.parseInt(action[1]);
                    linkedList.remove(position);
                } else if (action[0].equals("P")) {
                    linkedList.printList();
                }
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}

class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    Node head;

    LinkedList() {
        this.head = null;
    }

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

    void printList() {
        Node node = this.head;
        while (node != null) {
            System.out.print(node.data + " ");
            node = node.next;
        }
        System.out.println();
    }
}

