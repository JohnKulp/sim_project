from runsim import *

if __name__ == "__main__":
	steady_state_file = open("steady_state_res.txt", "w")
	steady_state_file.write("Iteration GradRate AvgGradTime\n")
	for i in range(150, 500):
		print("checking steady state at iter {}".format(i))
		grad_stats = main_loop(i, 1, 0)
		steady_state_file.write("%d %.2f %.2f\n" % (i, grad_stats[0], grad_stats[1]))

	steady_state_file.close()