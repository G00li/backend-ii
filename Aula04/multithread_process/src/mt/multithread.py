

import os
from queue import Queue
from PIL import Image, ImageFilter
import time
import threading 

class ImageProcessor: 

    def __init__(self, input_dir, output_dir, num_threads): 
        self.input_dir = input_dir
        self.output_dir = output_dir 
        self.num_threads = num_threads
        self.image_queue = Queue()

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
    def process_image(self): 
        while True: 
            image_file = self.image_queue.get()
            if image_file is None: 
                self.image_queue.task_done()
                break
            try: 
                input_path = os.path.join(self.input_dir, image_file)
                output_path = os.path.join(self.output_dir, image_file)
                with Image.open(input_path) as image:
                    processed = image.convert("L")
                    processed = processed.filter(ImageFilter.GaussianBlur(2))
                    processed = processed.filter(ImageFilter.EDGE_ENHANCE)

                    processed.save(output_path)

            except Exception as e:
                raise
            finally:
                self.image_queue.task_done()


    def run(self):
        start = time.perf_counter()
        images= [
            file for file in os.listdir(self.input_dir)
        ]

        if not images: 
            raise Exception("No images found")
        
        threads = []

        for _ in range(self.num_threads): 
            thread = threading.Thread(target=self.process_image)
            thread.daemon = True
            thread.start()
            threads.append(thread)

        for image in images:
            self.image_queue.put(image)

        for _ in range(self.num_threads):
            self.image_queue.put(None)
        
        self.image_queue.join()

        for thread in threads:
            thread.join()

        end = time.perf_counter() - start
        print(f"Tempo de execução: {end} segundos")



if __name__ =="__main__":
    processor = ImageProcessor(
        input_dir="../assets",
        output_dir="./output",
        num_threads=4
    )


    processor.run()
        