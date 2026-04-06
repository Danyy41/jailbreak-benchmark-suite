import pandas as pd
from tqdm import tqdm

from src.attacks import apply_attack
from src.utils import ensure_output_dir


def query_model(client, model_name, prompt):
    response = client.responses.create(
        model=model_name,
        input=prompt
    )
    return response.output_text


def run_benchmark(client, model_name, behaviors_df, attacks, output_file):

    ensure_output_dir(output_file)

    rows = []

    for _, row in tqdm(behaviors_df.iterrows(), total=len(behaviors_df)):

        for attack in attacks:

            wrapped = apply_attack(row["behavior_prompt"], attack)

            try:
                response = query_model(client, model_name, wrapped)
                status = "ok"
                error = ""
            except Exception as e:
                response = ""
                status = "error"
                error = str(e)

            rows.append({
                "id": row["id"],
                "attack": attack,
                "prompt": row["behavior_prompt"],
                "wrapped_prompt": wrapped,
                "response": response,
                "status": status,
                "error": error
            })

    df = pd.DataFrame(rows)
    df.to_csv(output_file, index=False)

    return df
