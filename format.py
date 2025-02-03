import json 
import os
from utils.utils import indent_file, update_matched

# for file in os.listdir('./json/bics/'):
#     file_path = f'./json/bics/{file}'
#     indent_file(file_path)

# indent_file("./json/elasticsearch/issues.json")
indent_file("./json/ansible/apache.json")
indent_file("./json/ansible/apache_2.json")