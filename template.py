import os
from pathlib import Path
import logging

#basic Logging for project
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s')

project_name = "NLP_Project"

#create project folder      

list_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for file_path in list_files:
    file_path = Path(file_path)
    fdir,fname = os.path.split(file_path)

    if fdir != "":
        os.makedirs(fdir,exist_ok=True)
        logging.info(f"creating director : {fdir}")

    if (not os.path.exists(file_path)) or  (os.path.getsize(file_path) == 0):
        
        with open(file_path, "w") as f:
            pass
            logging.info(f"creating file : {file_path}")
    else:
        logging.info(f"file already exists : {file_path}")