#include<stdio.h>

int main() {
    int max[10][10], allocation[10][10], need[10][10], available[10], work[10], finish[10];
    int m, n, i, j, flag, count = 0, done = 1;
    
    printf("\nEnter the number of resources: ");
    scanf("%d", &m);
    printf("\nEnter the number of processes: ");
    scanf("%d", &n);
    
    for(i = 0; i < n; i++) {
        finish[i] = -1; // Initially, no process is finished
    }
    
    printf("\nEnter the resources allocated:\n");
    for(i = 0; i < m; i++) {
        printf("   r%d  ", i + 1);
    }
    for(i = 0; i < n; i++) {
        printf("\n P%d\t", i);
        for(j = 0; j < m; j++) {
            scanf("%d", &allocation[i][j]);
        }
    }

    printf("\nEnter the maximum need:\n");
    for(i = 0; i < m; i++) {
        printf("   r[%d]  ", i + 1);		
    }
    for(i = 0; i < n; i++) {
        printf("\n P%d\t", i);
        for(j = 0; j < m; j++) {
            scanf("%d", &max[i][j]);
        }
    }

    printf("\nEnter the available resources:\n");
    for(i = 0; i < m; i++) {
        printf("  r%d", i + 1);
    }
    printf("\n");
    for(i = 0; i < m; i++) {
        scanf("%d", &available[i]);
    }

    // Initialize work and need matrices
    for(i = 0; i < m; i++) {
        work[i] = available[i];
    }
    
    for(i = 0; i < n; i++) {
        for(j = 0; j < m; j++) {
            need[i][j] = max[i][j] - allocation[i][j];
        }
    }
    
    printf("\nThe need matrix is:\n");
    for(i = 0; i < n; i++) {
        for(j = 0; j < m; j++) {
            printf("%d\t", need[i][j]);
        }
        printf("\n");
    }

    // Check for safe state
    printf("\nThe sequence is: ");
    while(count < n) { // loop till number of processes
        flag = 0; // reset flag to track if any process was executed
        
        for(i = 0; i < n; i++) {
            if(finish[i] == -1) { // if the process is not finished yet
                int can_execute = 1;
                
                // Check if process needs can be met with the current work (resources available)
                for(int k = 0; k < m; k++) {
                    if(need[i][k] > work[k]) {
                        can_execute = 0;
                        break;
                    }
                }
                
                if(can_execute == 1) { // process can execute
                    for(j = 0; j < m; j++) {
                        work[j] = work[j] + allocation[i][j]; // resources are released by the process
                    }
                    finish[i] = 0; // process is finished
                    printf("P%d  ", i); // print the sequence in which process executes
                    flag = 1;
                    count++;
                    break; // Exit the inner loop to check the next process
                }
            }
        }

        // If no process could execute in this cycle, then system is in unsafe state
        if(flag == 0) {
            done = 0;
            break;
        }
    }

    // After completing the cycle, check if all processes are finished
    if(done == 0)
        printf("\nThe system is not in safe state!!\n");
    else
        printf("\nThe system is in safe state\n");

    return 0;
}
