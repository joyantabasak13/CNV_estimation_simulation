import sys
from subprocess import call
import random
import math

random.seed(20)


def get_break_points(s_len, c_deletions, c_insertion, a_indel_lengths, a_copy):
    br_points_start = []
    br_points_end = []
    br_indel_size = []
    segment_points = []
    copy_between_br = []
    insert_base = 10
    total_indel = c_deletions + c_insertion
    each_region_len = int(s_len // total_indel)
    for i in range(total_indel):
        segment_points.append(int(each_region_len * i))
    segment_points.append(s_len)

    delete_regions = random.sample(range(0, len(segment_points) - 1), c_deletions)
    delete_regions.sort()
    insert_regions = []
    for i in range(len(segment_points) - 1):
        if i not in delete_regions:
            insert_regions.append(i)

    for i in range(len(segment_points) - 1):
        indel_size_class = random.choice(a_indel_lengths)
        indel_size = int(math.pow(10, indel_size_class))
        reg_start = int(segment_points[i])
        reg_end = int(segment_points[i + 1])
        while reg_end - indel_size < reg_start:
            indel_size = indel_size // 10
        indel_start_pos = random.sample(range(reg_start, reg_end - indel_size), 1)
        indel_end_pos = int(indel_start_pos[0] + indel_size)
        br_points_start.append(indel_start_pos[0])
        br_points_end.append(indel_end_pos)
        br_indel_size.append(indel_size)
        if i in delete_regions:
            copy_between_br.append(0)
        else:
            sampled_copy_number = random.choice(a_copy)
            copy_between_br.append(sampled_copy_number)

    print(f"Delete region indices {delete_regions}")
    print(f"Insert region indices {insert_regions}")
    print(f"Breakpoint starts {br_points_start}")
    print(f"Breakpoint ends   {br_points_end}")
    print(f"Breakpoint sizes  {br_indel_size}")
    print(f"Breakpoint copy no{copy_between_br}")

    return br_points_start, br_points_end, br_indel_size, copy_between_br


dir = "/home/joyanta/Documents/CNV/demo_G1_simulation_test/generated_data/"
reference_dir = "/home/joyanta/Documents/CNV/demo_G1_simulation_test/reference_data/reference.fa"

insert_lengths = [2, 3, 4, 5, 6]
copy_numbers = [3, 4, 5, 6, 7, 8]
reference_file = open(reference_dir, "r")
seq = reference_file.read()
seq = seq.replace("\n", "")
seq = seq[6:]
seq_len = len(seq)
number_of_deletions = 5
number_of_insertion = 10
number_of_simulations = 10

for i in range(number_of_simulations):
    file_name = ""
    file_name += str(i)
    test_file = open(dir + "S" + file_name + ".fa", "w")
    label_file = open(dir + "S" + file_name + "_Label.txt", "w")

    br_start, br_end, br_size, br_copy = get_break_points(seq_len, number_of_deletions, number_of_insertion,
                                                          insert_lengths,
                                                          copy_numbers)

    test_seq = ""
    len_increase = 0

    for j in range(len(br_start)):
        if j == 0:
            test_seq += seq[0: br_start[0]]  # initial region
        else:
            test_seq += seq[br_end[j-1]:br_start[j]]  # add preceding region
        start = br_start[j]
        end = br_end[j]
        size = br_size[j]
        for i in range(br_copy[j]):
            test_seq += seq[start: end]
        len_increase += size*(br_copy[j]-1)

        label_file.write(str(start) + "," + str(end) + "," + str(size) + "," + str(br_copy[j]) + "\n")

    test_seq += seq[br_end[-1]:]    # Add rest of the sequence
    print(f"Reference Length {seq_len}, Test length {len(test_seq)}")
    print(f"Test len should increase {len_increase}, Increased {len(test_seq) - seq_len}")
    test_file.write(">chr22\n")
    count = 0
    test_seq = "".join(test_seq.split())
    for ch in test_seq:
        test_file.write(ch)
        count += 1
        if count % 50 == 0:
            test_file.write("\n")
            count = 0
    if count != 0:
        test_file.write("\n")

    test_file.close()
    label_file.close()


reference_file.close()
