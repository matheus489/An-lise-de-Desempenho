import time
import tracemalloc

# Função para ordenar uma lista de números usando Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

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
    sorted_numbers = merge_sort(numbers)
    
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
