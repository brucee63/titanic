import os

# Install kaggle package
os.system('pip -q install kaggle')

import kaggle

# This assumes linux operating environment, only create if the dir doesn't exist
os.system('mkdir -p /root/.kaggle')

#assume your Kaggle API key (kaggle.json file) is present in the git root directory. Not checked into git via
# .gitignore
os.system('cp ../kaggle.json /root/.kaggle/')
os.system('chmod 600 /root/.kaggle/kaggle.json')

# download the titatic dataset
os.system('kaggle competitions download -c titanic -p ../data/raw/ --force')

# silently install unzip if not present
os.system('apt-get install unzip -y')
os.system('unzip -o ../data/raw/titanic.zip -d ../data/raw')
os.system('rm ../data/raw/titanic.zip')