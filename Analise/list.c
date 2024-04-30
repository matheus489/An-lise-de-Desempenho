#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct LinkedList {
    struct Node* head;
};

void append(struct LinkedList* list, int data) {
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = data;
    new_node->next = NULL;
    if (list->head == NULL) {
        list->head = new_node;
        return;
    }
    struct Node* last_node = list->head;
    while (last_node->next != NULL) {
        last_node = last_node->next;
    }
    last_node->next = new_node;
}

void remove_node(struct LinkedList* list, int position) {
    if (list->head == NULL)
        return;
    struct Node* temp = list->head;
    if (position == 0) {
        list->head = temp->next;
        free(temp);
        return;
    }
    for (int i = 0; temp != NULL && i < position - 1; i++) {
        temp = temp->next;
    }
    if (temp == NULL || temp->next == NULL)
        return;
    struct Node* next = temp->next->next;
    free(temp->next);
    temp->next = next;
}

void print_list(struct LinkedList* list) {
    struct Node* node = list->head;
    while (node != NULL) {
        printf("%d ", node->data);
        node = node->next;
    }
    printf("\n");
}

void execute_actions(const char* file_name) {
    FILE* file = fopen(file_name, "r");
    if (file == NULL) {
        perror("Erro ao abrir o arquivo");
        exit(EXIT_FAILURE);
    }

    struct LinkedList linked_list;
    linked_list.head = NULL;

    int data;
    while (fscanf(file, "%d", &data) != EOF) {
        append(&linked_list, data);
    }

    int action_count;
    fscanf(file, "%d", &action_count);

    char action[3];
    int number, position;
    for (int i = 0; i < action_count; i++) {
        fscanf(file, "%s", action);
        if (action[0] == 'A') {
            fscanf(file, "%d %d", &number, &position);
            if (position == 0) {
                struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
                new_node->data = number;
                new_node->next = linked_list.head;
                linked_list.head = new_node;
            } else {
                struct Node* node = linked_list.head;
                for (int j = 0; node != NULL && j < position - 1; j++) {
                    node = node->next;
                }
                if (node == NULL)
                    return;
                struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
                new_node->data = number;
                new_node->next = node->next;
                node->next = new_node;
            }
        } else if (action[0] == 'R') {
            fscanf(file, "%d", &position);
            remove_node(&linked_list, position);
        } else if (action[0] == 'P') {
            print_list(&linked_list);
        }
    }

    fclose(file);
}

int main() {
    execute_actions("D:/Faculdade/Analise/arq.txt");
    return 0;
}
