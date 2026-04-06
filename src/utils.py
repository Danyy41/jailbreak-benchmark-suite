import os
from pathlib import Path

import pandas as pd
import yaml
from dotenv import load_dotenv
from openai import OpenAI


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_behaviors(path, max_samples=None):
    df = pd.read_csv(path)
    if max_samples:
        df = df.head(max_samples)
    return df


def ensure_output_dir(output_file):
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)


def load_openai_client():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("Missing OPENAI_API_KEY")

    return OpenAI(api_key=api_key)
