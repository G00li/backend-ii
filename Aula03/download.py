import threading 
import time 
import random 
def download(arquivo):
    print(f"Iniciando download do arquivo {arquivo}")
    time.sleep(random.randint(1,7))
    print(f"Download do arquivo {arquivo} finalizado")


    
if __name__=="__main__":
    arquivos = ["arq1.txt", "arq2.txt", "arq3.txt"]
    threads = [
        threading.Thread(target=download, args=(arquivo, )) for arquivo in arquivos
    ]

    for thread in threads: 
        thread.start()

    for thread in threads: 
        thread.join()

    print("Todas os downloads foram concluidos")