#include <stdio.h>

// Function to print the Gantt chart
void print_gantt_chart(int p[], int bt[], int ct[], int n) {
    int i, j;

    // Print top bar
    printf(" ");
    for (i = 0; i < n; i++) {
        for (j = 0; j < bt[i]; j++) printf("--");
        printf(" ");
    }
    printf("\n|");

    // Print process IDs in the middle
    for (i = 0; i < n; i++) {
        for (j = 0; j < bt[i] - 1; j++) printf(" ");
        printf("P%d", p[i]);
        for (j = 0; j < bt[i] - 1; j++) printf(" ");
        printf("|");
    }
    printf("\n ");

    // Print bottom bar
    for (i = 0; i < n; i++) {
        for (j = 0; j < bt[i]; j++) printf("--");
        printf(" ");
    }
    printf("\n");

    // Print the timeline
    printf("0");
    for (i = 0; i < n; i++) {
        for (j = 0; j < bt[i]; j++) printf("  ");
        if (ct[i] > 9) printf("\b"); // Adjust for numbers > 9
        printf("%d", ct[i]);
    }
    printf("\n");
}

int main() { 
    int p[10], bt[10], wt[10], tat[10], ct[10], at[10];  
    int i, j, temp, n;
    float awt = 0, atat = 0;

    // Input number of processes
    printf("Enter number of processes: ");
    scanf("%d", &n);

    // Input process IDs
    printf("Enter %d process IDs: ", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &p[i]);
    }

    // Input arrival times
    printf("Enter %d arrival times: ", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &at[i]);
    }

    // Input burst times
    printf("Enter %d burst times: ", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &bt[i]);
    }

    // Sort processes based on Arrival Time (AT)
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (at[j] > at[j + 1]) {
                // Swap Arrival Time
                temp = at[j];
                at[j] = at[j + 1];
                at[j + 1] = temp;
                
                // Swap Burst Time
                temp = bt[j];
                bt[j] = bt[j + 1];
                bt[j + 1] = temp;
                
                // Swap Process ID
                temp = p[j];
                p[j] = p[j + 1];
                p[j + 1] = temp;
            }
        }
    }

    // Calculate Completion Times
    ct[0] = at[0] + bt[0];
    for (i = 1; i < n; i++) {
        int wait_time = (ct[i - 1] > at[i]) ? ct[i - 1] : at[i];
        ct[i] = wait_time + bt[i];
    }

    // Print the process table
    printf("\nPID\tA.T\tB.T\tC.T\tTAT\tWT");
    for (i = 0; i < n; i++) {
        tat[i] = ct[i] - at[i]; // Turnaround Time
        wt[i] = tat[i] - bt[i]; // Waiting Time
        atat += tat[i]; // Total Turnaround Time
        awt += wt[i];   // Total Waiting Time
        printf("\n%d\t%d\t%d\t%d\t%d\t%d", p[i], at[i], bt[i], ct[i], tat[i], wt[i]);
    }
    atat = atat / n; // Average Turnaround Time
    awt = awt / n;   // Average Waiting Time

    // Print Average Turnaround Time and Average Waiting Time
    printf("\n\nAverage Turnaround Time: %.2f", atat);
    printf("\nAverage Waiting Time: %.2f\n", awt);

    // Print the Gantt chart
    print_gantt_chart(p, bt, ct, n);

    return 0;
}
