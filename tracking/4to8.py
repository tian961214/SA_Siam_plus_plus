root_path = '/home/deeplearning/tian/siam-torch/Tracking/tracking_result_OTB-100/biker_SiamFC.txt'
gt_list = []
for i in open(root_path):
    gt_list.append(i[:-1])


def cvt_4_8(x, y, w, h):

    x1 = x
    y1 = y
    x2 = x + w
    y2 = y
    x3 = x + w
    y3 = y + h
    x4 = x
    y4 = y + h
    new_gt_str = '{},{},{},{},{},{},{},{}'.format(x1, y1, x2, y2, x3, y3, x4, y4)
    return new_gt_str


for gt in gt_list:
    x, y, w, h = gt.split()
    new_gt = cvt_4_8(float(x), float(y), float(w), float(h))
    ff_file = open('new_groundtruth_path.txt', 'w')
    ff_file.write(new_gt + '\n')
    print(new_gt)
