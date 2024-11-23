#include <stdio.h>

int bt[100], rt[100], at[100];  // Burst Time, Remaining Time, Arrival Time
float wait_time = 0, turn_time = 0;

int main() {
    int n, time, r, time_q, flag = 0, wt;
    
    printf("Enter number of processes: ");
    scanf("%d", &n);   // Number of processes
    r = n;

    // Input burst times and arrival times
    for (int c = 0; c < n; c++) {
        printf("Enter arrival time of P%d: ", c + 1);
        scanf("%d", &at[c]);  // Arrival time
        printf("Enter burst time of P%d: ", c + 1);
        scanf("%d", &bt[c]);  // Burst time
        rt[c] = bt[c];  // Initialize remaining time
    }

    printf("Enter time quantum: ");
    scanf("%d", &time_q);    // Quantum time
    printf("\n\tProcess\tAT\tTAT\tWT\n");

    // Round Robin scheduling logic
    for (time = 0; r > 0;) {
        int found = 0;
        for (int c = 0; c < n; c++) {
            if (rt[c] > 0 && at[c] <= time) {
                found = 1;  // Process is available to run
                if (rt[c] <= time_q) {
                    time += rt[c];
                    rt[c] = 0;
                    flag = 1;
                } else {
                    rt[c] -= time_q;
                    time += time_q;
                }

                if (rt[c] == 0 && flag == 1) {
                    wt = time - at[c] - bt[c];
                    r--;
                    printf("\tP%d\t%d\t%d\t%d\n", c + 1, at[c], time - at[c], wt);
                    wait_time += wt;
                    turn_time += time - at[c];
                    flag = 0;
                }
            }
        }
        
        // If no process was found, increment time
        if (!found) {
            time++;
        }
    }

    // Final calculations
    printf("\nAverage Waiting Time = %.2f\n", wait_time / n);
    printf("Average Turnaround Time = %.2f\n", turn_time / n);
    
    return 0;
}
