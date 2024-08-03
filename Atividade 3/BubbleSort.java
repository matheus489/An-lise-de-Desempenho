import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.nio.file.Files;
import java.nio.file.Paths;

public class BubbleSort {
    public static void main(String[] args) throws IOException {
        // Lê os números do arquivo de entrada
        List<Integer> numbers = readNumbers("D:/Faculdade/Analise/An-lise-de-Desempenho/Atividade 3/arq (1).txt");

        // Inicia a medição de tempo e memória
        long startTime = System.currentTimeMillis();
        long startMemory = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();

        // Ordena os números
        List<Integer> sortedNumbers = bubbleSort(numbers);

        // Termina a medição de tempo e memória
        long endTime = System.currentTimeMillis();
        long endMemory = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();

        // Escreve os números ordenados no arquivo de saída
        writeNumbers("arq-saidaBubbleSort_Java.txt", sortedNumbers);

        // Imprime o tempo de execução e a memória utilizada
        System.out.printf("Tempo de execução: %d ms\n", (endTime - startTime));
        System.out.printf("Memória utilizada: %d KB\n", (endMemory - startMemory) / 1024);
    }

    // Função para ordenar uma lista de números usando Bubble Sort
    public static List<Integer> bubbleSort(List<Integer> arr) {
        int n = arr.size();
        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < n-i-1; j++) {
                if (arr.get(j) > arr.get(j+1)) {
                    int temp = arr.get(j);
                    arr.set(j, arr.get(j+1));
                    arr.set(j+1, temp);
                }
            }
        }
        return arr;
    }

    // Função para ler números de um arquivo
    public static List<Integer> readNumbers(String fileName) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get(fileName));
        List<Integer> numbers = new ArrayList<>();
        for (String line : lines) {
            numbers.add(Integer.parseInt(line.trim()));
        }
        return numbers;
    }

    // Função para escrever números em um arquivo
    public static void writeNumbers(String fileName, List<Integer> numbers) throws IOException {
        BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));
        for (Integer number : numbers) {
            writer.write(number + "\n");
        }
        writer.close();
    }
}
