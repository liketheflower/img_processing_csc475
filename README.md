# img_processing_csc475
This is the code for the CSC475.


# How to install anconda on mac

# Go to home directory
cd ~

# approach 1

# You can change what anaconda version you want at 
# https://repo.continuum.io/archive/
curl -Ok https://repo.continuum.io/archive/Anaconda3-4.1.1-MacOSX-x86_64.sh
bash Anaconda3-4.1.1-MacOSX-x86_64.sh -b -p ~/anaconda
rm Anaconda3-4.1.1-MacOSX-x86_64.sh
echo 'export PATH="~/anaconda/bin:$PATH"' >> ~/.bash_profile 

# Refresh basically
source .bash_profile

conda update conda


# approach 2

# You can change what anaconda version you want at 
wget https://repo.continuum.io/archive/Anaconda3-5.1.0-MacOSX-x86_64.sh
bash Anaconda3-5.1.0-MacOSX-x86_64.sh -b -p ~/anaconda
rm Anaconda3-5.1.0-MacOSX-x86_64.sh
echo 'export PATH="~/anaconda/bin:$PATH"' >> ~/.bash_profile 

# Refresh basically
source .bash_profile

conda update conda


# How to install pytorch on mac

conda install pytorch torchvision -c pytorch 
# macOS Binaries dont support CUDA, install from source if CUDA is needed


# install tensorflow

conda install -c anaconda tensorflow

gpu:
conda install -c anaconda tensorflow-gpu

# install keras

conda install -c conda-forge keras
