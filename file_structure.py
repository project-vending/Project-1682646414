
import os

# Define folder names
folders = ['data', 'models', 'api']

# Create folders if they don't exist already
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Define file names
data_files = ['users.csv', 'ratings.csv', 'products.csv']
model_files = ['model.pkl', 'vocab.pkl']
api_files = ['main.py', 'utils.py']

# Create empty files in respective folders
for file in data_files:
    open(os.path.join('data', file), 'a').close()
for file in model_files:
    open(os.path.join('models', file), 'a').close()
for file in api_files:
    open(os.path.join('api', file), 'a').close()
