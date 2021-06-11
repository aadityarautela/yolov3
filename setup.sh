gdown --id 1I7OjhaomWqd8Quf7o5suwLloRlY0THbp
mkdir WiderPerson/
unzip WiderPerson.zip -d WiderPerson
rm WiderPerson.zip
mkdir data/WiderPerson
mkdir data/WiderPerson/images
mkdir data/WiderPerson/images/validation
mkdir data/WiderPerson/images/train
mkdir data/WiderPerson/labels
mkdir data/WiderPerson/labels/validation
mkdir data/WiderPerson/labels/train
python setup_wp.py
rm -r WiderPerson/
