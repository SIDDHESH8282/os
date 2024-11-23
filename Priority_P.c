#include <stdio.h>
#include <limits.h>

// Structure for storing process information
struct Process {
    int id;
    int burstTime;
    int remainingTime;
    int arrivalTime;
    int priority;
    int completionTime;
    int waitingTime;
    int turnaroundTime;
};

// Function to find the process with the highest priority (preemptive)
int find_highest_priority(struct Process processes[], int n, int current_time) {
    int highest_priority_index = -1;
    int highest_priority = INT_MAX;

    for (int i = 0; i < n; i++) {
        if (processes[i].arrivalTime <= current_time && processes[i].remainingTime > 0) {
            if (processes[i].priority < highest_priority || 
                (processes[i].priority == highest_priority && processes[i].arrivalTime < processes[highest_priority_index].arrivalTime)) {
                highest_priority = processes[i].priority;
                highest_priority_index = i;
            }
        }
    }

    return highest_priority_index;
}

// Function to implement preemptive priority scheduling
void preemptive_priority_scheduling(struct Process processes[], int n) {
    int completed = 0, current_time = 0;
    int total_turnaround_time = 0, total_waiting_time = 0;

    // Gantt chart timeline
    printf("\nGantt Chart:\n");

    // Until all processes are completed
    while (completed < n) {
        int highest_priority_index = find_highest_priority(processes, n, current_time);

        // If no process is available at the current time, move time forward
        if (highest_priority_index == -1) {
            current_time++;
            continue;
        }

        // Print process execution in Gantt Chart
        printf("| P%d ", processes[highest_priority_index].id);

        // Execute the process for 1 unit of time (preemption occurs every 1 unit)
        processes[highest_priority_index].remainingTime--;
        current_time++;

        // If the process is completed
        if (processes[highest_priority_index].remainingTime == 0) {
            completed++;
            processes[highest_priority_index].completionTime = current_time;
            processes[highest_priority_index].turnaroundTime = processes[highest_priority_index].completionTime - processes[highest_priority_index].arrivalTime;
            processes[highest_priority_index].waitingTime = processes[highest_priority_index].turnaroundTime - processes[highest_priority_index].burstTime;

            // Accumulate total turnaround and waiting times
            total_turnaround_time += processes[highest_priority_index].turnaroundTime;
            total_waiting_time += processes[highest_priority_index].waitingTime;
        }
    }
    
    printf("|\n");
    for(int j = 0 ; j < 17 ; j++)
    {
    printf("%d   ",j);
    }
    // Calculate and display the process table
    printf("\nPID\tA.T\tB.T\tPrio\tC.T\tTAT\tWT");
    for (int i = 0; i < n; i++) {
        printf("\n%d\t%d\t%d\t%d\t%d\t%d\t%d", processes[i].id, processes[i].arrivalTime, processes[i].burstTime, 
               processes[i].priority, processes[i].completionTime, processes[i].turnaroundTime, processes[i].waitingTime);
    }

    // Calculate average turnaround time and waiting time
    float average_tat = (float)total_turnaround_time / n;
    float average_wt = (float)total_waiting_time / n;

    printf("\n\nAverage Turnaround Time: %.2f", average_tat);
    printf("\nAverage Waiting Time: %.2f\n", average_wt);
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
        printf("Priority (lower number = higher priority): ");
        scanf("%d", &processes[i].priority);

        // Initialize remaining time and other parameters
        processes[i].remainingTime = processes[i].burstTime;
    }

    // Execute preemptive priority scheduling
    preemptive_priority_scheduling(processes, n);

    return 0;
}
