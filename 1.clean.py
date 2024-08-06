import glob, os, shutil

def images():
    for jpg_file in glob.glob('*/*/*/*/images/*.jpg'):
        B_C, D_K, weight, train_valid, images_labels, longname = jpg_file.split('\\')
        if 'error' in weight:
            continue
        name = longname.split('_jpg')[0]
        new_file = os.path.join(train_valid, images_labels, name+'.jpg')
        print(new_file)
        shutil.copy(jpg_file, new_file)
        # break

def labels():
    class_labels = [
        'bench_dumbbell_base',
        'bench_dumbbell_2kg',
        'bench_dumbbell_4kg',
        'bench_dumbbell_6kg',
        'bench_dumbbell_8kg',
        'bench_dumbbell_10kg',
        'bench_dumbbell_12kg',
        'bench_dumbbell_14kg',
        'bench_dumbbell_16kg',
        'bench_dumbbell_18kg',
        'bench_dumbbell_20kg',
        'bench_kettlebell_6kg',
        'bench_kettlebell_8kg',
        'bench_kettlebell_10kg',
        'bench_kettlebell_12kg',
        'bench_kettlebell_14kg',
        'bench_kettlebell_16kg',
        'cube_dumbbell_base',
        'cube_dumbbell_5_5kg',
        'cube_dumbbell_6kg',
        'cube_dumbbell_7_5kg',
        'cube_dumbbell_8kg',
        'cube_dumbbell_9_5kg',
        'cube_dumbbell_10kg',
        'cube_dumbbell_12kg',
        'cube_kettlebell_base',
        'cube_kettlebell_4_5kg',
        'cube_kettlebell_4_75kg',
        'cube_kettlebell_5_5kg_2kgx1',
        'cube_kettlebell_5_5kg_1kgx2',
        'cube_kettlebell_5_75kg',
        'cube_kettlebell_6kg',
        'cube_kettlebell_6_5kg',
        'cube_kettlebell_6_75kg',
        'cube_kettlebell_7_5kg',
        'cube_kettlebell_7_75kg',
        ]

    def log(txt_file, error):
        with open(f'{error}.log', 'a') as f:
            f.write(f'{txt_file}\n')

    for txt_file in glob.glob('*/*/*/*/labels/*.txt'):
        B_C, D_K, weight, train_valid, images_labels, longname = txt_file.split('\\')
        if 'error' in weight:
            continue
        name = longname.split('_jpg')[0]
        class_label = name.split('_202')[0].replace('-', '_').replace('__', '_')
        with open(txt_file) as f:
            lines = []
            for line in f.readlines():
                try:
                    original_class_index, x, y, w, h = line.split()
                except:
                    log(txt_file, 'error_unpack')
                    continue
                i = int(original_class_index)
                if B_C == 'Bench' and D_K == 'Kettlebell':
                    i += 11
                if B_C == 'Cube' and D_K == 'Dumbbell':
                    i += 17
                if B_C == 'Cube' and D_K == 'Kettlebell':
                    i += 25
                if class_labels[i] not in class_label:
                    log(txt_file, 'error_mismatch')
                    continue
                line = f'{i} {x} {y} {w} {h}'
                lines.append(line)
        new_file = os.path.join(train_valid, images_labels, name+'.txt')
        with open(new_file, 'w') as f:
            f.write('\n'.join(lines))
        # break

# images()
labels()