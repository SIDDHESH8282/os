def page_replacement():
    incoming_stream = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0]
    page_faults = 0
    frames = 3
    pages = len(incoming_stream)

    print("Incoming \t Frame 1 \t Frame 2 \t Frame 3")
    temp = [-1] * frames

    for m in range(pages):
        s = 0

        for n in range(frames):
            if incoming_stream[m] == temp[n]:
                s += 1
                page_faults -= 1

        page_faults += 1

        if page_faults <= frames and s == 0:
            temp[m] = incoming_stream[m]
        elif s == 0:
            temp[(page_faults - 1) % frames] = incoming_stream[m]

        print(f"\n{incoming_stream[m]}\t", end="")
        for n in range(frames):
            if temp[n] != -1:
                print(f" {temp[n]}\t", end="")
            else:
                print(" - \t", end="")

    print(f"\nTotal Page Faults:\t{page_faults}")

if __name__ == "__main__":
    page_replacement()
