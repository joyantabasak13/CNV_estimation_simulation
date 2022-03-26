from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


class Label:
    def __init__(self, start, end, copy):
        self.start = start
        self.end = end
        self.copy = copy

    def print_me(self):
        print("%d %d %d" % (self.start, self.end, self.copy))


def get_copy_num(dir_in_copyno):
    f_path = []
    contig_copyno = {}
    sample_copy_info = []
    for x in range(2,9):
        f_name = f"{dir_in_copyno}ContigVsCopyNo_{x}.txt"
        f_path.append(f_name)
    for file in f_path:
        with open(file, 'r') as fin:
            for line_no, line in enumerate(fin, 1):
                words = line.split()
                if len(words) > 0:
                    contig_copyno[int(words[2])] = int(words[5])
            sorted_contig_copyNo = [contig_copyno[k] for k in sorted(contig_copyno)]
            selected_contigs = []
            for i in range(1,len(sorted_contig_copyNo)):
                if i%2==1:
                    selected_contigs.append(sorted_contig_copyNo[i])
            sample_copy_info.append(selected_contigs)
    return sample_copy_info


def print_copy_info(sample_copy_info):
    print("\nPrinting Sample copy info")
    for i, x in enumerate(sample_copy_info):
        print(f"In sample with copy {i+2} estimated region copies {x}")
    # print(sample_copy_info)


def compare_dist_info(dist1, dist2):
    print("\nComparing Distance values")
    total_pos = len(dist1) * len(dist1[0])
    tot_pos = [total_pos, 0, 0]
    for i, x in enumerate(dist1):
        better_pos = []
        worse_pos = []
        for j, y in enumerate(x):
            if abs(dist1[i][j]) < abs(dist2[i][j]):
                better_pos.append(j)
            elif abs(dist1[i][j]) > abs(dist2[i][j]):
                worse_pos.append(j)
        if len(better_pos) + len(worse_pos) > 0:
            print(f"Copy {i+2}: Dist1 better at : {better_pos}")
            print(f"Copy {i+2}: Dist1 worse at  : {worse_pos}")
            tot_pos[1] += len(better_pos)
            tot_pos[2] += len(worse_pos)

    print(f"Dist1 is better than Dist2 in {tot_pos[1]} positions and worse in {tot_pos[2]} positions out of total {tot_pos[0]} positions")


def get_copy_info_distance_from_reference(sample_copy_info):
    dist_all_sample = []
    for i, x in enumerate(sample_copy_info):
        dist_single_sample = []
        for j, y in enumerate(x):
            ref_copy_no = i + 2
            dist_single_sample.append(abs(ref_copy_no - y))
        dist_all_sample.append(dist_single_sample)
    return dist_all_sample


def plot_copy_info(sample_copy_info, save_image_name):
    fig = plt.figure()
    # syntax for 3-D projection
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlim3d(1, 7)
    ax.set_ylim3d(0, 50)
    ax.set_zlim3d(1, 8)

    # defining all 3 axes
    x_test = [1, 2, 3, 4, 5, 6, 7]
    y_test = [1, 2, 3, 5, 8, 12, 19]
    z_test = [2, 3, 4, 5, 6, 7, 8]

    x_pred = x_test
    y_pred = y_test
    z_pred = sample_copy_info

    count = 0
    for x in range(len(x_test)):
        for y in range(len(y_test)):
            for z in z_pred:
                test_x = [x_test[x], x_test[x]]
                test_y = [y_test[y], y_test[y]]
                test_z = [z_test[x], 0]
                if count == 0:
                    ax.plot3D(test_x, test_y, test_z, 'red', alpha=.4, label="Test")
                else:
                    ax.plot3D(test_x, test_y, test_z, 'red', alpha=.4)
                ax.scatter(test_x[0], test_y[0], test_z[0], color='red', marker='^')
                pred_x = [x_pred[x], x_pred[x]]
                pred_y = [y_pred[y], y_pred[y]]
                pred_z = [z_pred[x][y], 0]
                if count == 0:
                    ax.plot3D(pred_x, pred_y, pred_z, 'blue', alpha=.4, label="Estimated")
                else:
                    ax.plot3D(pred_x, pred_y, pred_z, 'blue', alpha=.4)
                ax.scatter(pred_x[0], pred_y[0], pred_z[0], color='blue', marker='o')
                count += 1

    plt.xlabel("Sample No")
    plt.ylabel("Insert points along the genome length (*1000000)")
    ax.set_zlabel("Copy Number")

    plt.legend()
    save_image_name = save_image_name + ".png"
    plt.savefig(save_image_name)
    plt.show()


# File paths
dir_in_copyno1 = '/home/joyanta/Documents/Projects/CNV/DataProcessing/data/copyContigs_len_2M/'
dir_in_copyno2 = '/home/joyanta/Documents/Projects/CNV/DataProcessing/data/copyContigs_len_5M/'
# f_in_label = '/home/joyanta/Documents/Projects/CNV/DataProcessing/data/label_with_del_400_1.txt'
# f_in_segments = '/home/joyanta/Documents/Projects/CNV/DataProcessing/data/segmented_result_Win_50_RCutoff_1000_LR_Alpha=0.0005.csv'

sample_copy_info1 = get_copy_num(dir_in_copyno1)
sample_copy_info2 = get_copy_num(dir_in_copyno2)

print_copy_info(sample_copy_info1)
print_copy_info(sample_copy_info2)

dist_sample_1 = get_copy_info_distance_from_reference(sample_copy_info1)
dist_sample_2 = get_copy_info_distance_from_reference(sample_copy_info2)

print(dist_sample_1)
print(dist_sample_2)
compare_dist_info(dist_sample_1, dist_sample_2)


