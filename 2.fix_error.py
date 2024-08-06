import os

with open('error_unpack.log') as f:
    for line in f.readlines():
        with open(line.strip()) as ff:
            # labels = ff.readline().split()
            # assert labels[0] == '0'
            B_C, D_K, weight, train_valid, images_labels, longname = line.strip().split('\\')
            name = longname.split('_jpg')[0]
            # with open(os.path.join(train_valid, 'labels', name+'.txt'), 'w') as fff:
            #     labels[0] = '21'
            #     fff.write(' '.join(labels))
            os.remove(os.path.join(train_valid, 'images', name+'.jpg'))
            os.remove(os.path.join(train_valid, 'labels', name+'.txt'))