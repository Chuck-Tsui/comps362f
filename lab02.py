import multiprocessing
import random, time
import timeit
# File: lab02.py

# Replace the following by your full name and 8-digit student number
student_name = "Xu Xiaochi"
student_id = "12556828"

def partition(n, p):
    """Partition 0 to n, both inclusive, to p partitions.
       Return a list of (start, stop) values of the partitions,
       where start is inclusive and stop is exclusive."""
    size = n // p  # partition size, except for last partition
    starts = list(range(0, n+1, size))[0:p]         # p start values
    stops = list(range(0, n+1, size))[1:p] + [n+1]  # p stop values
    return list(zip(starts, stops))

# Add any necessary function(s) and class(es)
class MyProcess(multiprocessing.Process):
    def __init__(self, word):
        self.word = word
        super().__init__()

    def run(self):
        for i in range(10):
            time.sleep(0.1 * random.random())
            print(self.word, end=" ", flush=True)

def str_processes(*words):
    processes = [MyProcess(word) for word in words]

    for process in processes:
        process.start()
    for process in processes:
        process.join()

def sum_partition(p, my_list, results):
    """Sum the integers in my_list and append the sum to results."""
    results.put(sum(range(my_list[0], my_list[1])))

def sum_processes_queue(n, p):
    start_time = timeit.default_timer()
    MyList = partition(n, p)
    results = multiprocessing.Queue()
    processes = []
    for i in range(p):
        process = multiprocessing.Process(target=sum_partition, args=[i, MyList[i], results])
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    final_sum = 0
    
    while not results.empty():
        final_sum += results.get()
    end_time = timeit.default_timer()
    return final_sum,end_time-start_time


if __name__ == "__main__":
    str_processes("a", "b", "c", "d")
    print()
    print("-----------------------------------")
    str_processes("H", "K", "M", "U")
    print()
    for i in range(1, 11):
        print(i, sum_processes_queue(int(1e8), i))
    print("-----------------------------------")
    for i in range(1, 11):
        print(i, sum_processes_queue(int(100), i))
