file_name = "S0"
dir='/home/joyanta/Documents/CNV/demo_G1_simulation_test/generated_data/'
file = open(dir+file_name+"/"+file_name+".fa", "r")
raw_seq = file.read()
seq = raw_seq.replace("\n", "")
print(f"{file_name} len {len(seq)} 30x reads {len(seq)*30 // 202}")

print(51304566*30//202)
# copy_numbers = [2, 3, 4, 5, 6, 7, 8]
# for i in range(len(copy_numbers)+1):
#     size = (5000+(188*i)) * 1000
#     number_reads = size * 45 / 202
#     print(f"Size for copy {i+1} is {size} and number of reads are {number_reads}")

# reference_file1 = '/home/joyanta/Documents/Projects/CNV/DataProcessing/data/demo_ref.fa'
# reference_file2 = '/home/joyanta/Documents/Projects/CNV/DataProcessing/data/C2.fa'
# reference_file3 = '/home/joyanta/Documents/Projects/CNV/DataProcessing/data/C3.fa'
#
# reference_file = open(reference_file1, "r")
# seq = reference_file.read()
# print(len(seq))
# reference_file.close()
# reference_file = open(reference_file2, "r")
# seq = reference_file.read()
# print(len(seq))
# reference_file.close()
# reference_file = open(reference_file3, "r")
# seq = reference_file.read()
# print(len(seq))
# reference_file.close()
