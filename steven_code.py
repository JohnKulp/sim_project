from runsim import *

if __name__ == "__main__":
    steady_state_file = open("steady_state_res.txt", "w")
    steady_state_file.write("Iteration GradRate AvgGradTime")
    for i in range(1,1000):
        grad_stats = main_loop(i, 10, 0)
        steady_state_file.write("%d %.2f %.2f" % (i, grad_stats[0], grad_stats[1]))

    steady_state_file.close()