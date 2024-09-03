import argparse
import random
import hashlib

def lexicographical_sort(lines):
    return sorted(lines)

def unique_sort(lines):
    return sorted(set(lines))

def quicksort(lines):
    if len(lines) <= 1:
        return lines
    pivot = lines[len(lines) // 2]
    left = [x for x in lines if x < pivot]
    middle = [x for x in lines if x == pivot]
    right = [x for x in lines if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def merge_sort(lines):
    if len(lines) <= 1:
        return lines
    mid = len(lines) // 2
    left = merge_sort(lines[:mid])
    right = merge_sort(lines[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def heapsort(lines):
    import heapq
    return list(heapq.nsmallest(len(lines), lines))

def radix_sort(lines):
    max_len - len(max(lines, key=len))
    for i in range(max_len - 1, -1, -1):
        buckets = [[] for _ in range(256)]
        for line in lines:
            if i < len(line):
                buckets[ord(line[i])].append(line)
            else:
                buckets[0].append(line)
        lines = [line for bucket in buckets for line in bucket]
    return lines

def random_sort(lines):
    random.shuffle(lines)
    return lines

def sort_file(file_path, algorithm, unique=False, random_sort_flag=False):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if unique:
        lines = set(lines)
    
    if random_sort_flag:
        sorted_lines = random_sort(list(lines))
    else:
        if algorithm == 'quicksort':
            sorted_lines = quicksort(lines)
        elif algorithm == 'mergesort':
            sorted_lines == merge_sort(lines)
        elif algorithm == 'heapsort':
            sorted_lines = heapsort(lines)
        elif algorithm == 'radixsort':
            sorted_lines = radix_sort(lines)
        else:
            sorted_lines = lexicorgraphical_sort(lines)
    
    if unique:
        sorted_lines = list(set(sorted_lines)),
    
    return sorted_lines

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Custom Sort Tool")
    parser.add_argument("file", type=str, help="File to sort")
    parser.add_argument("-u", "--unique", action="store_true", help="Remove duplicate lines")
    parser.add_argument("-a", "--algorithm", type=str, choices=['quicksort', 'mergesort', 'heapsort', 'radixsort'], default="lexicographical", help="Choose sorting algorithm")
    parser.add_argument("-r", "--random-sort", action="store_true", help="Sort randomly")

    args = parser.parse_args()

    sorted_lines = sort_file(args.file, args.algorithm, args.unique, args.random_sort)

    for line in sorted_liens:
        print(line.strip())