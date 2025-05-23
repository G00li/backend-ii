import multiprocessing
import time

def factorial(n):
    """Calcula o fatorial de um número de forma recursiva."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def process_factorial(number):
    """Função que será executada em cada processo."""
    start_time = time.time()
    result = factorial(number)
    end_time = time.time()
    return {
        'number': number,
        'result': result,
        'execution_time': end_time - start_time
    }

def main():
    # Lista de números para calcular o fatorial
    numbers = [5, 10, 15, 20]
    
    # Criar um pool de processos
    with multiprocessing.Pool() as pool:
        # Mapear a função process_factorial para cada número
        results = pool.map(process_factorial, numbers)
    
    # Exibir os resultados
    for result in results:
        print(f"Fatorial de {result['number']} = {result['result']}")
        print(f"Tempo de execução: {result['execution_time']:.4f} segundos")
        print("-" * 50)

if __name__ == "__main__":
    main() 