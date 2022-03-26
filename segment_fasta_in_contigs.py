import csv
dir='/home/joyanta/Documents/CNV/DataProcessing/data/test_sample_gen/'
inp_file_name_ref = "reference"
segment_file_name = "S9_Label.txt"

file = open(dir+inp_file_name_ref+".fa", "r") #second level input file which was output in first step
file1 = open(dir+"segmented_demo_ref.fa", "w") #output file: reference.fa


seq = file.readline()
raw_seq = file.read()
print(len(raw_seq))
seq = raw_seq.replace("\n", "")
print(len(seq))
breakpoints = [0]

with open(dir+segment_file_name) as seg_csv_file:
    seg_reader = csv.reader(seg_csv_file, delimiter='\t')
    for row in seg_reader:
        row = row[0].split(",")
        print(row)
        if breakpoints[-1] != int(row[0]):
            breakpoints.append(int(row[0]))
        if breakpoints[-1] != int(row[1]):
            breakpoints.append(int(row[1]))
    if breakpoints[-1] != len(seq):
        breakpoints.append(len(seq))
    print(breakpoints)
    for i in range(1,len(breakpoints)):
        file1.write(">"+str(i)+"\n")
        seg_start = breakpoints[i-1]
        seg_end = breakpoints[i]
        temp_seq = seq[seg_start:seg_end]
        print(f"Copied reference from position {seg_start} to {seg_end}")
        temp_seq = "".join(temp_seq.split())
        count = 0
        for ch in temp_seq:
            file1.write(ch)
            count += 1
            if count % 50 == 0:
                file1.write("\n")
                count = 0

        if count != 0:
            file1.write("\n")

file.close()
file1.close()
