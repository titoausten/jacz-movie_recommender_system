import os
import pandas as pd
import sys
import yaml
import joblib
import base64
import streamlit as st
from src import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from src.exceptions import CustomException


@ensure_annotations
def load_data(path_to_file):
    print(f"Loading source data file...")
    df = pd.read_csv(path_to_file)
    logger.info(f"Data file ({path_to_file}) loaded")
    return df


@ensure_annotations
def save_data_to_csv(data: pd.DataFrame, file_path):
    data.to_csv(file_path)
    logger.info(f"Preprocessed file location: {file_path}")


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        CustomException

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        raise CustomException(e, sys)
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_bin(data, path: str):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(data, open(str(path),'wb'))

    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: str):
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(open(str(path),'rb'))
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


@ensure_annotations
def set_background(image_file: str):
    """
    Set the background image for a Streamlit app.

    Args:
        image_file (str): The file path of the image to be used as the background.

    Returns:
        None
    """
    with open(image_file, "rb") as f:
        image_data = f.read()
    b64_encoded = base64.b64encode(image_data).decode()
    style = f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(0, 0, 0, 0.9),
            rgba(0, 0, 0, 0.9)), url(data:image/png;base64,{b64_encoded});
            background-size: cover;
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)

