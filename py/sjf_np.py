def swap(x, y):
    return y, x

def sort_at(p, at, bt, n):
    for i in range(n):
        for j in range(i + 1, n):
            if at[i] > at[j]:
                p[i], p[j] = swap(p[i], p[j])
                at[i], at[j] = swap(at[i], at[j])
                bt[i], bt[j] = swap(bt[i], bt[j])
            elif at[i] == at[j]:
                if bt[i] > bt[j]:
                    p[i], p[j] = swap(p[i], p[j])
                    at[i], at[j] = swap(at[i], at[j])
                    bt[i], bt[j] = swap(bt[i], bt[j])

def tatwt(ct, at, bt, tat, wt, n):
    for i in range(n):
        tat[i] = ct[i] - at[i]
        wt[i] = tat[i] - bt[i]

def print_gantt_chart(p, bt, ct, n):
    print(" ", end="")
    for i in range(n):
        for _ in range(bt[i]):
            print("--", end="")
        print(" ", end="")
    print()
    
    print("|", end="")
    for i in range(n):
        for _ in range(bt[i] - 1):
            print(" ", end="")
        print(f"P{p[i]}", end="")
        for _ in range(bt[i] - 1):
            print(" ", end="")
        print("|", end="")
    print()
    
    print(" ", end="")
    for i in range(n):
        for _ in range(bt[i]):
            print("--", end="")
        print(" ", end="")
    print()
    
    print("0", end="")
    for i in range(n):
        for _ in range(bt[i]):
            print("  ", end="")
        if ct[i] > 9:
            print("\b", end="")  # Adjust for numbers > 9
        print(f"{ct[i]}", end="")
    print()

def sjf_non_preemptive():
    n = int(input("Enter the number of processes: "))
    p = [0] * n
    at = [0] * n
    bt = [0] * n
    ct = [0] * n
    wt = [0] * n
    tat = [0] * n
    
    print("Enter the process IDs:")
    for i in range(n):
        p[i] = int(input(f"Process {i+1}: "))
    
    print("Enter the arrival times:")
    for i in range(n):
        at[i] = int(input(f"Arrival Time for Process {i+1}: "))
    
    print("Enter the burst times:")
    for i in range(n):
        bt[i] = int(input(f"Burst Time for Process {i+1}: "))
    
    sort_at(p, at, bt, n)
    
    ct[0] = at[0] + bt[0]
    
    for i in range(1, n):
        min_bt = float('inf')
        pos = -1
        for j in range(i, n):
            if at[j] <= ct[i-1] and bt[j] < min_bt:
                min_bt = bt[j]
                pos = j
        
        p[i], p[pos] = swap(p[i], p[pos])
        at[i], at[pos] = swap(at[i], at[pos])
        bt[i], bt[pos] = swap(bt[i], bt[pos])
        
        ct[i] = ct[i-1] + bt[i]
    
    tatwt(ct, at, bt, tat, wt, n)
    
    print("\nProcess\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    for i in range(n):
        print(f"{p[i]}\t{at[i]}\t\t{bt[i]}\t\t{ct[i]}\t\t{tat[i]}\t\t{wt[i]}")
    
    avg_tat = sum(tat) / n
    avg_wt = sum(wt) / n
    
    print(f"\nAverage Turnaround Time = {avg_tat:.2f}")
    print(f"Average Waiting Time = {avg_wt:.2f}")
    
    print_gantt_chart(p, bt, ct, n)

# Run the Non-Preemptive SJF scheduling algorithm
sjf_non_preemptive()
