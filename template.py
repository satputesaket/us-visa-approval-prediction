import os 
from pathlib import Path

project_dir = "us_visa"


list_of_files = [

    f"{project_dir}/__init__.py",
    f"{project_dir}/components/__init__.py",
    f"{project_dir}/components/data_injestion.py",
    f"{project_dir}/components/data_validation.py",
    f"{project_dir}/components/data_transformation.py",
    f"{project_dir}/components/model_trainer.py",
    f"{project_dir}/components/model_evaluation.py",
    f"{project_dir}/components/model_pusher.py",
    
    f"{project_dir}/configuration/__init__.py",
    
    f"{project_dir}/constants/__init__.py",

    f"{project_dir}/entity/__init__.py",
    f"{project_dir}/entity/config_entity.py",
    f"{project_dir}/entity/artifact_entity.py",



    f"{project_dir}/exception/__init__.py",

    f"{project_dir}/logger/__init__.py",

    f"{project_dir}/pipeline/__init__.py",
    f"{project_dir}/pipeline/training_pipline.py",
    f"{project_dir}/pipeline/prediction_pipeline.py",

    f"{project_dir}/utils/__init__.py",
    f"{project_dir}/utils/main_utils.py"
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml"
]


for filepath in list_of_files:
    file_path = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
    else:
        print(f"File {filepath} already exists.")
    