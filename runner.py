import statistics as sts
import matplotlib.pyplot as plt
import Exercicio_1 as exe1
import time
import sys

# run ordering
# return duration
def run_order(number_list, k, size):
    threads = k
    start = time.time()
    while k >= 1:
        exe1.order_list(number_list,k,size)
        if(k == 1):
            k = 0
        else:
            k = k//2

    duration = time.time()-start
    print("Ordering complete for k = {}, time eleapsed: ".format(threads) + str(duration))
    return duration

def main(argv):
    size = 50000000

    means = []
    pstdevs = []

    ks = [1,2,4,8]
    for k in ks:
        durations = []
        for i in range(10):
            # create list
            number_list = list()
            exe1.create_list(number_list, 2, size) # time to create the list doesn't count, so we can use any number of threads
            # order list and get execution duration
            durations.append(run_order(number_list, k, size))
        # calculate mean and pstdev
        mean = sts.mean(durations)
        pstdev = sts.pstdev(durations)
        print("For k = {}, mean is {} and standard deviation is {}".format(k, mean, pstdev))
        means.append(mean)
        pstdevs.append(pstdev)

    # PLOT MEANS GRAPH
    plt.plot(ks, means)
    plt.xlabel('threads (k)')
    plt.ylabel('tempo (média)')
    plt.title('Gráfico de Médias')
    plt.show()

    # PLOT PSTDEV GRAPH
    plt.plot(ks, pstdevs)
    plt.xlabel('threads (k)')
    plt.ylabel('tempo (desvio padrão)')
    plt.title('Gráfico de Desvio Padrão')
    plt.show()

if __name__ == "__main__":
   main(sys.argv[1:])
        

    

        

