def search(key, frame_items, frame_occupied):
    return key in frame_items[:frame_occupied]

def print_outer_structure(max_frames):
    print("Stream ", end="")
    for i in range(max_frames):
        print(f"Frame{i+1}", end=" ")

def print_curr_frames(item, frame_items, frame_occupied, max_frames):
    print(f"\n{item} \t\t", end="")
    for i in range(max_frames):
        if i < frame_occupied:
            print(f"{frame_items[i]}\t\t", end="")
        else:
            print("-\t\t", end="")

def predict(ref_str, frame_items, ref_str_len, index, frame_occupied):
    farthest = index
    result = -1
    for i in range(frame_occupied):
        j = index  # Initialize j here to ensure it's defined for the inner loop
        for j in range(index, ref_str_len):
            if frame_items[i] == ref_str[j]:
                if j > farthest:
                    farthest = j
                    result = i
                break
        # If j reaches ref_str_len and no match was found, this means the frame is not used again
        if j == ref_str_len:
            return i
    return 0 if result == -1 else result


def optimal_page(ref_str, ref_str_len, frame_items, max_frames):
    frame_occupied = 0
    print_outer_structure(max_frames)
    
    hits = 0
    for i in range(ref_str_len):
        if search(ref_str[i], frame_items, frame_occupied):
            hits += 1
            print_curr_frames(ref_str[i], frame_items, frame_occupied, max_frames)
            continue
        
        if frame_occupied < max_frames:
            frame_items[frame_occupied] = ref_str[i]
            frame_occupied += 1
            print_curr_frames(ref_str[i], frame_items, frame_occupied, max_frames)
        else:
            pos = predict(ref_str, frame_items, ref_str_len, i + 1, frame_occupied)
            frame_items[pos] = ref_str[i]
            print_curr_frames(ref_str[i], frame_items, frame_occupied, max_frames)

    print(f"\n\nHits: {hits}")
    print(f"Misses: {ref_str_len - hits}")

# Test the function with the example incoming stream and frame count
ref_str = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
ref_str_len = len(ref_str)
max_frames = 4
frame_items = [None] * max_frames

optimal_page(ref_str, ref_str_len, frame_items, max_frames)
