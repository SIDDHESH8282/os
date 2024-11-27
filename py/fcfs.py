import matplotlib.pyplot as plt

# FCFS Scheduling Algorithm
def fcfs_scheduling(arrival_times, burst_times):
    n = len(arrival_times)
    start_times = [0] * n
    finish_times = [0] * n
    waiting_times = [0] * n
    turnaround_times = [0] * n
    
    # First process starts at time 0
    start_times[0] = arrival_times[0]
    finish_times[0] = start_times[0] + burst_times[0]
    waiting_times[0] = start_times[0] - arrival_times[0]
    turnaround_times[0] = finish_times[0] - arrival_times[0]
    
    # Calculate for the remaining processes
    for i in range(1, n):
        start_times[i] = max(arrival_times[i], finish_times[i-1])
        finish_times[i] = start_times[i] + burst_times[i]
        waiting_times[i] = start_times[i] - arrival_times[i]
        turnaround_times[i] = finish_times[i] - arrival_times[i]
    
    return start_times, finish_times, waiting_times, turnaround_times

# Function to create Gantt chart
def plot_gantt_chart(processes, start_times, finish_times):
    fig, gnt = plt.subplots()
    gnt.set_xlabel('Time')
    gnt.set_ylabel('Processes')
    
    # Create Gantt chart by plotting the processes
    for i in range(len(processes)):
        gnt.broken_barh([(start_times[i], finish_times[i] - start_times[i])], (i - 0.4, 0.8), facecolor='orange')
    
    # Labeling the processes
    gnt.set_yticks(range(len(processes)))
    gnt.set_yticklabels(processes)
    plt.show()

# Main function
def main():
    processes = ['P1', 'P2', 'P3', 'P4']
    arrival_times = [0, 1, 2, 3]  # Arrival times of processes
    burst_times = [5, 3, 8, 6]    # Burst times (CPU time required) of processes
    
    # Perform FCFS scheduling
    start_times, finish_times, waiting_times, turnaround_times = fcfs_scheduling(arrival_times, burst_times)
    
    # Display results
    print("Process\tArrival Time\tBurst Time\tStart Time\tFinish Time\tWaiting Time\tTurnaround Time")
    for i in range(len(processes)):
        print(f"{processes[i]}\t{arrival_times[i]}\t\t{burst_times[i]}\t\t{start_times[i]}\t\t{finish_times[i]}\t\t{waiting_times[i]}\t\t{turnaround_times[i]}")
    
    # Create Gantt chart
    plot_gantt_chart(processes, start_times, finish_times)

if __name__ == "__main__":
    main()
