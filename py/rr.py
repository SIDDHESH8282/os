# Round Robin Scheduling Algorithm

def round_robin(processes, burst_time, quantum):
    n = len(processes)  # Number of processes
    remaining_bt = burst_time[:]  # Remaining burst time for each process
    time = 0  # Current time
    waiting_time = [0] * n  # Waiting time for each process
    turn_around_time = [0] * n  # Turnaround time for each process
    gantt_chart = []  # Gantt chart representation

    while True:
        done = True
        for i in range(n):
            if remaining_bt[i] > 0:  # If burst time is left for this process
                done = False  # At least one process is still not done
                if remaining_bt[i] > quantum:
                    # Execute for a time quantum
                    time += quantum
                    remaining_bt[i] -= quantum
                    gantt_chart.append((processes[i], quantum))
                else:
                    # Execute for the remaining burst time
                    time += remaining_bt[i]
                    gantt_chart.append((processes[i], remaining_bt[i]))
                    waiting_time[i] = time - burst_time[i]
                    remaining_bt[i] = 0
        if done:
            break

    # Calculate Turnaround Time
    for i in range(n):
        turn_around_time[i] = burst_time[i] + waiting_time[i]

    # Print Results
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turn_around_time[i]}")

    # Display Gantt Chart
    print("\nGantt Chart:")
    gantt_display = ""
    for process, exec_time in gantt_chart:
        gantt_display += f"| {process} " + "-" * exec_time
    gantt_display += "|"
    print(gantt_display)

# Example usage:
processes = ["P1", "P2", "P3", "P4"]
burst_time = [5, 8, 6, 4]  # Burst time for each process
quantum = 3  # Time quantum

round_robin(processes, burst_time, quantum)
