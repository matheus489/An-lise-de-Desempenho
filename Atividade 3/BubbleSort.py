import time
import tracemalloc

# Função para ordenar uma lista de números usando Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Função para ler números de um arquivo
def read_numbers(file_name):
    with open(file_name, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

# Função para escrever números em um arquivo
def write_numbers(file_name, numbers):
    with open(file_name, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")

def main():
    # Lê os números do arquivo de entrada
    numbers = read_numbers('D:/Faculdade/Analise/An-lise-de-Desempenho/Atividade 3/arq (1).txt')

    # Inicia a medição de memória
    tracemalloc.start()
    # Inicia a medição de tempo
    start_time = time.time()
    
    # Ordena os números
    sorted_numbers = bubble_sort(numbers)
    
    # Termina a medição de tempo
    end_time = time.time()
    # Termina a medição de memória
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    # Escreve os números ordenados no arquivo de saída
    write_numbers('arq-saida.txt', sorted_numbers)

    # Imprime o tempo de execução e a memória utilizada
    print(f"Tempo de execução: {(end_time - start_time) * 1000:.2f} ms")
    print(f"Memória utilizada: {peak / 1024:.2f} KB")

if __name__ == "__main__":
    main()
