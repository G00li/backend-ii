import threading

def thread_job(number): 
    print(f"started thread for number {number}")

    for x in range(number):
        print(x)

    print(f"finished thread for number {number}")

    


if __name__  == "__main__":
    threads = [threading.Thread(target=thread_job, args=(index,)) for index in range(10)]
    for thread in threads:
        thread.start() 

    for thread in threads:
        thread.join() 
        