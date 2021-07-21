pip install scikit-learn
pip install kaggle
kaggle datasets download andrewmvd/face-mask-detection
mkdir -p Dataset/FaceMask/Images/train
mkdir -p Dataset/FaceMask/Images/validation
mkdir -p Dataset/FaceMask/Labels/train
mkdir -p Dataset/FaceMask/Labels/validation
mkdir face-mask-detection
unzip face-mask-detection.zip -d face-mask-detection
python setup_mask.py