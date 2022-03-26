import sys
from subprocess import call
import random

dir = "/home/joyanta/Documents/Projects/CNV/demo_breakpoint_study_5M_length/generated_data/"
reference_dir = '/home/joyanta/Documents/Projects/CNV/demo_breakpoint_study_5M_length/demo_ref/demo_ref_no_format.fa'

### len(insertLengths) must be len(breakpoints) - 1
insert_lengths = [1, 2, 5, 10, 20, 50, 100]
copy_numbers = [2, 3, 4, 5, 6, 7, 8]
breakpoints=[0, 5, 10, 15, 20, 25, 35, 49]
breakpoint_coff = 100000
insert_coff = 1000
reference_file = open(reference_dir, "r")
seq = reference_file.read()
seq = seq.replace("\n", "")

print(f"Sequence Length: {len(seq)}")

for i in range(len(copy_numbers)):
    file_name = ""
    file_name += str(copy_numbers[i])
    test_file = open(dir+"C"+file_name+".fa","w")
    label_file = open(dir+"C"+file_name+"_Label.txt","w")

    test_seq = ""

    for j in range(len(breakpoints) - 1):
        prev = breakpoints[j]*breakpoint_coff
        start = breakpoints[j+1]*breakpoint_coff
        size = insert_lengths[j]*insert_coff
        test_seq += seq[prev: start]
        count = 1
        while count < copy_numbers[i]:
            test_seq += seq[start: start + size]
            count += 1
        label_file.write(str(start) + "," + str(start + size) + "," + str(size) + "," + str(copy_numbers[i])+"\n")

    test_seq += seq[breakpoints[-1]*breakpoint_coff:]

    test_file.write(">chr22\n")
    count = 0
    test_seq = "".join(test_seq.split())
    for ch in test_seq:
        test_file.write(ch)
        count += 1
        if count%50 ==0:
            test_file.write("\n")
            count = 0
    if count != 0:
            test_file.write("\n")

    test_file.close()
    label_file.close()
    print(f"Test Sequence for Copynumber {copy_numbers[i]} has length {len(test_seq)}")

reference_file.close()
