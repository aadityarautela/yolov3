from sklearn.model_selection import train_test_split
import os
import shutil
import numpy as np
from pathlib import Path
from shutil import copyfile
from glob import glob
from PIL import Image

kitty_names_dict = {
    'Car': 0,
    'Van': 1,
    'Truck': 2,
    'Pedestrian': 3,
    'Person_sitting': 4,
    'Cyclist': 5,
    'Tram': 6,
    'Misc': 7
}

kitty_basedir = 'kitty/training/'
kitty_imagedir = kitty_basedir + 'image_2/'
kitty_labeldir = kitty_basedir + 'label_2/'
kitty_modified_labeldir = kitty_basedir + 'modified_labeldir/'

kitty_ds_dir = 'data/kitty/'
kitty_ds_dir_images = kitty_ds_dir + 'images/'
kitty_ds_dir_labels = kitty_ds_dir + 'labels/'
kitty_ds_dir_images_train = kitty_ds_dir_images + 'train/'
kitty_ds_dir_images_validation = kitty_ds_dir_images + 'validation/'
kitty_ds_dir_labels_train = kitty_ds_dir_labels + 'train/'
kitty_ds_dir_labels_validation = kitty_ds_dir_labels + 'validation/'

kitty_imagedir_list = glob(kitty_imagedir + "*")
for img_path in kitty_imagedir_list:
    kitty_image_path_with_ext = img_path[-10:]
    kitty_id = kitty_image_path_with_ext[:-4]
    img = Image.open(img_path)
    w, h = (img.width, img.height)

    kitty_label_path_with_ext = kitty_labeldir + kitty_id + '.txt'
    lines_input = []
    lines_output = []
    with open(kitty_label_path_with_ext, 'r') as f:
        lines_input = f.readlines()
    for line in lines_input:
        line_split = line.split()
        if len(line_split) == 15:
            if line_split[0] != 'DontCare':
                x1 = int(line_split[4])
                y1 = int(line_split[5])
                x2 = int(line_split[6])
                y2 = int(line_split[7])
                xc = str((x1+x2)/(2*w))
                yc = str((y1+y2)/(2*h))
                yolo_width = str((x2-x1)/w)
                yolo_height = str((y2-y1)/h)
                yolo_class = kitty_names_dict[line_split[0]]
                line_output = " ".join(
                    [yolo_class, xc, yc, yolo_width, yolo_height, '\n'])
                lines_output.append(line_output)

    with open(kitty_modified_labeldir + kitty_id + '.txt', 'w') as f:
        f.writelines(lines_output)

kitty_id_list = [x[-10:] for x in kitty_imagedir_list]
kitty_id_list = [x[:-4] for x in kitty_imagedir_list]
train_id_list, validation_id_list = train_test_split(
    kitty_id_list, test_size=0.2, random_state=1)

for id in train_id_list:
    shutil.copy(kitty_imagedir + id + '.png',
                kitty_ds_dir_images_train + id + '.png')
    shutil.copy(kitty_modified_labeldir + id + '.txt',
                kitty_ds_dir_labels_train + id + '.png')

for id in validation_id_list:
    shutil.copy(kitty_imagedir + id + '.png',
                kitty_ds_dir_images_validation + id + '.png')
    shutil.copy(kitty_modified_labeldir + id + '.txt',
                kitty_ds_dir_labels_validation + id + '.png')
