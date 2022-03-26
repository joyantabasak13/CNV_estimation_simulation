# f_in = '/home/joyanta/Documents/Projects/CNV/Debug_demo/reference.fa'
# f_out = '/home/joyanta/Documents/Projects/CNV/Debug_demo/demo_ref.fa'

f_in = '/home/joyanta/Documents/Projects/CNV/demo_breakpoint_study_5M_length/demo_ref/reference.fa'
f_out = '/home/joyanta/Documents/Projects/CNV/demo_breakpoint_study_5M_length/demo_ref/demo_ref.fa'

with open(f_in, 'r') as fin, open(f_out, 'w') as fout:
    for lineno, line in enumerate(fin, 1):
        if lineno == 1:
            fout.write(line)
        elif 10000 < lineno <= 110000:
            fout.write(line)
        elif lineno > 110000:
            break

