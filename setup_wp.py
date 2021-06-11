import os
from shutil import copy
from PIL import Image
from glob import glob

# All mkdir via shell script
wp_dataset_directory = 'WiderPerson/'
wp_dataset_imgs_directory = 'WiderPerson/Images/'
wp_dataset_labels_directory = 'WiderPerson/Annotations/'
wp_training_dataset_directory = 'data/WiderPerson/'
train_txt_path = 'WiderPerson/train.txt'
validation_txt_path = 'WiderPerson/val.txt'
wp_training_train_images_path = 'data/WiderPerson/images/train/'
wp_training_validation_images_path = 'data/WiderPerson/images/validation/'
wp_training_train_labels_path = 'data/WiderPerson/labels/train/'
wp_training_validation_labels_path = 'data/WiderPerson/labels/validation/'

# Training Data

# Structuring Logic
train_imgs_list = []
with open(train_txt_path, 'r') as f:
    train_imgs_list = f.readlines()
train_imgs_list = [x[:-1] if x[-1] == '\n' else x for x in train_imgs_list]
train_imgs_path_list = [os.path.join(
    wp_dataset_imgs_directory, x + '.jpg') for x in train_imgs_list]
for img_path in train_imgs_path_list:
    copy(img_path, os.path.join(
        wp_training_train_images_path, os.path.basename(img_path)))

# Labels Logic
train_labels_path_list = [os.path.join(wp_dataset_labels_directory,
                                       os.path.basename(x) + '.jpg.txt') for x in train_imgs_list]
for train_label_path in train_labels_path_list:
    img_path = os.path.join(wp_dataset_imgs_directory,
                            os.path.basename(train_label_path)[:-4])
    w, h = Image.open(img_path).size
    train_label_lines = []
    with open(train_label_path, 'r') as f:
        train_label_lines = f.readlines()
    train_label_lines = train_label_lines[1:]

    training_train_label_lines = []

    for line in train_label_lines:
        wp_label, x1, y1, x2, y2 = line.split()
        wp_label = int(wp_label)
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        yolo_label = str(wp_label-1)
        xc = str((x2+x1)/(2*w))
        yc = str((y2+y1)/(2*h))
        yolo_width = str((x2-x1)/w)
        yolo_height = str((y2-y1)/h)
        yolo_line = " ".join(
            [yolo_label, xc, yc, yolo_width, yolo_height, '\n'])
        training_train_label_lines.append(yolo_line)
    with open(os.path.join(wp_training_train_labels_path,
                           os.path.basename(train_label_path)[:-8] + '.txt'), 'w') as f:
        f.writelines(training_train_label_lines)

# Validation Data

# Structuring Logic
validation_imgs_list = []
with open(validation_txt_path, 'r') as f:
    validation_imgs_list = f.readlines()
validation_imgs_list = [x[:-1] if x[-1] ==
                        '\n' else x for x in validation_imgs_list]
validation_imgs_path_list = [os.path.join(
    wp_dataset_imgs_directory, x + '.jpg') for x in validation_imgs_list]
for img_path in validation_imgs_path_list:
    copy(img_path, os.path.join(
        wp_training_validation_images_path, os.path.basename(img_path)))

# Labels Logic
validation_labels_path_list = [os.path.join(wp_dataset_labels_directory,
                                            os.path.basename(x) + '.jpg.txt') for x in validation_imgs_list]
for validation_label_path in validation_labels_path_list:
    img_path = os.path.join(wp_dataset_imgs_directory,
                            os.path.basename(validation_label_path)[:-4])
    w, h = Image.open(img_path).size
    validation_label_lines = []
    with open(validation_label_path, 'r') as f:
        validation_label_lines = f.readlines()
    validation_label_lines = validation_label_lines[1:]

    training_validation_label_lines = []

    for line in validation_label_lines:
        wp_label, x1, y1, x2, y2 = line.split()
        wp_label = int(wp_label)
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        yolo_label = str(wp_label-1)
        xc = str((x2+x1)/(2*w))
        yc = str((y2+y1)/(2*h))
        yolo_width = str((x2-x1)/w)
        yolo_height = str((y2-y1)/h)
        yolo_line = " ".join(
            [yolo_label, xc, yc, yolo_width, yolo_height, '\n'])
        training_validation_label_lines.append(yolo_line)
    with open(os.path.join(wp_training_validation_labels_path,
                           os.path.basename(validation_label_path)[:-8] + '.txt'), 'w') as f:
        f.writelines(training_validation_label_lines)
