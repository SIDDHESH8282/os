#include <stdio.h>
#include <limits.h> // For INT_MAX

// Structure to store process information
struct Process {
    int id;             // Process ID
    int arrivalTime;     // Arrival time of the process
    int burstTime;       // Burst time (total)
    int remainingTime;   // Remaining time (for preemption)
    int completionTime;  // Completion time
    int waitingTime;     // Waiting time
    int turnaroundTime;  // Turnaround time
};

// Function to find the process with the shortest remaining time at the current time
int find_shortest_remaining_time(struct Process processes[], int n, int current_time) {
    int min_remaining_time = INT_MAX;
    int shortest_process_index = -1;

    for (int i = 0; i < n; i++) {
        if (processes[i].arrivalTime <= current_time && processes[i].remainingTime > 0) {
            if (processes[i].remainingTime < min_remaining_time) {
                min_remaining_time = processes[i].remainingTime;
                shortest_process_index = i;
            }
        }
    }

    return shortest_process_index;
}

void preemptive_sjf(struct Process processes[], int n) {
    int completed = 0, current_time = 0;
    int total_waiting_time = 0, total_turnaround_time = 0;
    
    // Variables for Gantt Chart
    int gantt_chart[100], gantt_time[100], gantt_counter = 0;

    // Until all processes are completed
    while (completed < n) {
        int shortest_process_index = find_shortest_remaining_time(processes, n, current_time);

        // If no process is available at the current time, move the time forward
        if (shortest_process_index == -1) {
            current_time++;
            continue;
        }

        // Store the process in Gantt chart sequence
        gantt_chart[gantt_counter] = processes[shortest_process_index].id;
        gantt_time[gantt_counter] = current_time;
        gantt_counter++;

        // Reduce remaining time of the selected process
        processes[shortest_process_index].remainingTime--;

        // If the process finishes execution
        if (processes[shortest_process_index].remainingTime == 0) {
            completed++;
            processes[shortest_process_index].completionTime = current_time + 1;
            processes[shortest_process_index].turnaroundTime = processes[shortest_process_index].completionTime - processes[shortest_process_index].arrivalTime;
            processes[shortest_process_index].waitingTime = processes[shortest_process_index].turnaroundTime - processes[shortest_process_index].burstTime;

            total_waiting_time += processes[shortest_process_index].waitingTime;
            total_turnaround_time += processes[shortest_process_index].turnaroundTime;
        }

        current_time++;
    }

    // Adding the final time for Gantt chart
    gantt_time[gantt_counter] = current_time;

    // Print process results
    printf("\nPID\tA.T\tB.T\tC.T\tTAT\tWT\n");
    for (int i = 0; i < n; i++) {
        printf("%d\t%d\t%d\t%d\t%d\t%d\n", processes[i].id, processes[i].arrivalTime, processes[i].burstTime,
               processes[i].completionTime, processes[i].turnaroundTime, processes[i].waitingTime);
    }

    // Calculate and display average turnaround time and waiting time
    float average_tat = (float)total_turnaround_time / n;
    float average_wt = (float)total_waiting_time / n;

    printf("\nAverage Turnaround Time: %.2f", average_tat);
    printf("\nAverage Waiting Time: %.2f\n", average_wt);

    // Print Gantt Chart
    printf("\nGantt Chart:\n");
    printf(" ");
    for (int i = 0; i < gantt_counter; i++) {
        printf("----");
    }
    printf("\n|");
    for (int i = 0; i < gantt_counter; i++) {
        printf(" P%d |", gantt_chart[i]);
    }
    printf("\n ");
    for (int i = 0; i < gantt_counter; i++) {
        printf("----");
    }
    printf("\n");
    for (int i = 0; i <= gantt_counter; i++) {
        printf("%3d  ", gantt_time[i]);
    }
    printf("\n");
}

int main() {
    int n;

    // Input number of processes
    printf("Enter the number of processes: ");
    scanf("%d", &n);

    struct Process processes[n];

    // Input process details
    for (int i = 0; i < n; i++) {
        printf("\nEnter details for Process %d\n", i + 1);
        processes[i].id = i + 1;
        printf("Arrival Time: ");
        scanf("%d", &processes[i].arrivalTime);
        printf("Burst Time: ");
        scanf("%d", &processes[i].burstTime);

        // Initialize remaining time to burst time
        processes[i].remainingTime = processes[i].burstTime;
    }

    // Call the preemptive SJF scheduling function
    preemptive_sjf(processes, n);

    return 0;
}
