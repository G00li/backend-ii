# Challenge:
# Problem: Optimise a bubble sort algorithm so that it stops early if the list is already sorted.

from time import perf_counter

def bubble_sort(arr):
    start = perf_counter()
    n = len(arr)
    for i in range(n):
        troca_realizada = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                troca_realizada = True
        if not troca_realizada:
            break
    end = perf_counter()
    print(f"Execution time: {end - start:.6f} seconds")
    return arr


print(bubble_sort([5, 3, 8, 4, 2]))


# def test():
#     start = perf_counter()
#     for i in range(1000000):
#         pass
#     end = perf_counter()

#     print(f"Execution time: {end - start:.6f} seconds")

# if __name__ == "__main__":
#     test()