import os
from PIL import Image, ImageFilter
import time
import multiprocessing

class ImageProcessor:

    def __init__(self, input_dir, output_dir, num_processes):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.num_processes = num_processes
        self.image_queue = multiprocessing.Queue()

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def process_image(self):
        while True:
            image_file = self.image_queue.get()
            if image_file is None:
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
                print(f"Erro ao processar {image_file}: {e}")

    def run(self):
        start = time.perf_counter()
        images = [file for file in os.listdir(self.input_dir) if os.path.isfile(os.path.join(self.input_dir, file))]

        if not images:
            raise Exception("No images found")

        processes = []

        for _ in range(self.num_processes):
            p = multiprocessing.Process(target=self.process_image)
            p.start()
            processes.append(p)

        for image in images:
            self.image_queue.put(image)

        for _ in range(self.num_processes):
            self.image_queue.put(None)

        for p in processes:
            p.join()

        end = time.perf_counter() - start
        print(f"Tempo de execução: {end:.2f} segundos")


if __name__ == "__main__":
    processor = ImageProcessor(
        input_dir="../assets",
        output_dir="./output",
        num_processes=4
    )

    processor.run()
