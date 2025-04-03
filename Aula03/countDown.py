import threading 
import time

# Crie duas threads que realizam contagens regressivas simultaneamente, cada uma começando de um número diferente.

def countDown(number): 
    for x in range(number, 0, -1):
        print(f"Counting down {x} from thread {threading.current_thread().name}")
        time.sleep(1)


if __name__=="__main__":
    threads = [
        threading.Thread(target=countDown, args=(10,)),
        threading.Thread(target=countDown, args=(10,))
    ]
    
    for thread in threads: 
        thread.start()
    
    
    for thread in threads: 
        thread.join()

    print("Todas as threads finalizaram")