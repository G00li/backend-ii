import threading 
import time 
import datetime

def relogio():
   for _ in range(10):
        agora = datetime.datetime.now()
        print(f"Hora atual --> {agora.strftime("%H:%M:%S")}")
        time.sleep(1)

def countUp():
    for x in range(10): 
        print(f"Contador --> {x}")
        time.sleep(1)

if __name__=="__main__":
    threads = [
        threading.Thread(target= relogio), 
        threading.Thread(target= countUp)
    ]

    for thread in threads: 
        thread.start()

    for thread in threads: 
        thread.join()

    print("Threads finalizadas")