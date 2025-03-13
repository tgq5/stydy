import json 
import os
from utils.utils import indent_file, update_matched

# indent_file(filename='./json/bics/bics_ss.json')
for file in os.listdir('./json/bics'):
    indent_file(f"./json/bics/{file}")
# indent_file("./json/raw_data/issues.json")