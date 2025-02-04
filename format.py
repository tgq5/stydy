import json 
import os
from utils.utils import indent_file, update_matched

for file in os.listdir('./json/bics/'):
    file_path = f'./json/bics/{file}'
    indent_file(file_path)
