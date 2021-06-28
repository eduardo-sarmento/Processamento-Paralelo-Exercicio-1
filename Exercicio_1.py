# Exercicio_1.py
import sys
import random
import threading
import time

def sort_list(number_list,i,j):
    number_list[i:j] = sorted(number_list[i:j])

def list_append(count, id, out_list):
    """
    Creates an empty list and then appends a 
    random number to the list 'count' number
    of times. A CPU-heavy operation!
    """
    for i in range(count):
        out_list.append(random.random())

def order_list(number_list,k,size):
    threads = k   # Number of threads to create

    # Create a list of jobs and then iterate through
    # the number of threads appending each thread to
    # the job list 
    jobs = []

    for i in range(0, threads):
        if(k != 0):
            thread = threading.Thread(target=sort_list(number_list, (size//threads)*i,(size//threads)*(i+1)))
        else:
            thread = threading.Thread(target=sort_list(number_list, 0,len(number_list)-1))
        jobs.append(thread)

    # Start the threads (i.e. calculate the random number lists)
    for j in jobs:
        j.start()

    # Ensure all of the threads have finished
    for j in jobs:
        j.join()

def create_list(number_list,k,size):
    
    threads = k   # Number of threads to create

    # Create a list of jobs and then iterate through
    # the number of threads appending each thread to
    # the job list 

    jobs = []
    for i in range(0, threads):
        
        thread = threading.Thread(target=list_append(size//threads, i, number_list))
        jobs.append(thread)

    # Start the threads (i.e. calculate the random number lists)
    for j in jobs:
        j.start()

    # Ensure all of the threads have finished
    for j in jobs:
        j.join()
    
def is_sorted(lst, key=lambda x: x):
    for i, el in enumerate(lst[1:]):
        if key(el) < key(lst[i]): # i is the index of the previous element
            return False
    return True

def main(argv):
    number_list = list()
    size = 50000000
    i = int(argv[0])
    create_list(number_list,i,size)
    start = time.time()
    while i >= 1:
        order_list(number_list,i,size)
        if(i == 1):
            i = 0
        else:
            i = i//2
        print(i)
    
    print("List processing complete.")
    print("Time eleapsed: " + str(time.time()-start))
    #print(is_sorted(number_list))

if __name__ == "__main__":
   main(sys.argv[1:])
