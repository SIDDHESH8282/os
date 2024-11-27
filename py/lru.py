def check_hit(incoming_page, queue):
    return incoming_page in queue

def print_frame(queue):
    print("\t".join(str(page) for page in queue))

def optimal_page_replacement(incoming_stream, frames):
    queue = []
    page_faults = 0

    print("Page\t Frame1 \t Frame2 \t Frame3 \t Frame4")

    for i, page in enumerate(incoming_stream):
        print(f"{page}:  \t\t", end="")

        if check_hit(page, queue):  # Page hit, no replacement
            print_frame(queue)
        elif len(queue) < frames:  # Frame has space, just add the page
            queue.append(page)
            page_faults += 1
            print_frame(queue)
        else:  # Page fault, need to replace a page
            # Calculate the distance to the next occurrence of each page
            distances = [float('inf')] * len(queue)
            for j in range(len(queue)):
                for k in range(i + 1, len(incoming_stream)):
                    if queue[j] == incoming_stream[k]:
                        distances[j] = k - i
                        break
            
            # Find the page that will be used furthest in the future or never used
            index_to_replace = distances.index(max(distances))
            queue[index_to_replace] = page
            page_faults += 1
            print_frame(queue)
        
        print()

    print(f"Total Page Faults: {page_faults}")

# Test the function with the example incoming stream and frame count
incoming_stream = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
frames = 4
optimal_page_replacement(incoming_stream, frames)
