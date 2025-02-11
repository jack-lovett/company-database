import importlib
import os

from crud.base_crud import CRUDBase


# Dynamically create a CRUD class for each model
def create_crud_class(model_class):
    class GenericCRUD(CRUDBase):
        def __init__(self):
            super().__init__(model_class)

    return GenericCRUD


# Get all model files from the 'models' directory (excluding __init__.py)
def get_model_files(models_dir):
    model_files = []
    for filename in os.listdir(models_dir):
        # Only consider Python files and exclude '__init__.py'
        if filename.endswith('.py') and filename != '__init__.py':
            model_files.append(filename[:-3])  # Remove .py extension
    return model_files


def snake_to_camel_case(snake_str):
    """
    Converts snake_case to CamelCase.
    """
    components = snake_str.split('_')
    return ''.join(x.capitalize() for x in components)


# Dynamically import all models with adjusted class name mapping
def import_models(models_dir, model_files):
    models = {}
    for model_file in model_files:
        module = importlib.import_module(f"models.{model_file}")
        # Convert snake_case file name to CamelCase class name
        class_name = snake_to_camel_case(model_file)
        models[model_file] = getattr(module, class_name)
    return models


# Define the models directory (adjust this path if necessary)
models_dir = "C:/Users/User3/spacecounts.com/Drawing Works - Projects/2025007-Company Database/company_database/models"

# Get the list of all model files
model_files = get_model_files(models_dir)

# Dynamically import all models
models = import_models(models_dir, model_files)

# Dynamically create CRUD classes for all models
crud_classes = {model_name: create_crud_class(model) for model_name, model in models.items()}

# Optionally, print the names of the created CRUD classes
for crud_name in crud_classes:
    print(f"Created CRUD class: {crud_name}")
