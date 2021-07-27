mkdir kitty
wget https://s3.eu-central-1.amazonaws.com/avg-kitti/data_object_image_2.zip
wget https://s3.eu-central-1.amazonaws.com/avg-kitti/data_object_label_2.zip
unzip data_object_image_2.zip -d kitty
unzip data_object_label_2.zip -d kitty

mkdir -p kitty/training/modified_labeldir
mkdir -p data/kitty/images/train
mkdir -p data/kitty/images/validation
mkdir -p data/kitty/labels/train
mkdir -p data/kitty/labels/validation

python setup_kitty.py