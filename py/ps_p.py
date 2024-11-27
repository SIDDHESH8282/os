# Preemptive Priority Scheduling with Boxed Gantt Chart
def preemptive_priority_scheduling(processes):
    # Sort processes based on arrival time
    processes.sort(key=lambda x: x[2])

    # Initialize
    time = 0
    completed = 0
    n = len(processes)
    waiting_time = [0] * n
    turn_around_time = [0] * n
    remaining_burst_time = [processes[i][1] for i in range(n)]
    completed_processes = []
    gantt_chart = []

    while completed < n:
        # Find the process with the highest priority that has arrived
        highest_priority = -1
        selected_process = -1
        for i in range(n):
            if processes[i][2] <= time and remaining_burst_time[i] > 0:
                if highest_priority == -1 or processes[i][3] < processes[highest_priority][3]:
                    highest_priority = i
                    selected_process = i

        if selected_process != -1:
            # Execute the selected process
            remaining_burst_time[selected_process] -= 1
            time += 1
            gantt_chart.append(processes[selected_process][0])  # Record the process in the Gantt chart

            # If the process finishes, update the waiting and turn around times
            if remaining_burst_time[selected_process] == 0:
                completed += 1
                completion_time = time
                waiting_time[selected_process] = completion_time - processes[selected_process][1] - processes[selected_process][2]
                turn_around_time[selected_process] = completion_time - processes[selected_process][2]
                completed_processes.append(processes[selected_process])
        else:
            time += 1

    # Display results
    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{completed_processes[i][0]}\t\t{completed_processes[i][2]}\t\t{completed_processes[i][1]}\t\t{waiting_time[i]}\t\t{turn_around_time[i]}")

    # Display Gantt Chart (boxed format)
    print("\nGantt Chart:")
    print("+", "-" * (len(gantt_chart) * 3), "+")
    print("|", end=" ")
    for process in gantt_chart:
        print(f"{process} ", end="| ")
    print("\n+", "-" * (len(gantt_chart) * 3), "+")


# Test with processes (Name, Burst Time, Arrival Time, Priority)
processes = [
    ("P1", 5, 0, 1),  # (Name, Burst Time, Arrival Time, Priority)
    ("P2", 3, 2, 2),
    ("P3", 8, 1, 4),
    ("P4", 6, 4, 3)
]

preemptive_priority_scheduling(processes)
