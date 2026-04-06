# to be implemented
from src.runner import run_benchmark
from src.utils import load_yaml, load_behaviors, load_openai_client


def main():

    model_config = load_yaml("configs/models.yaml")
    attack_config = load_yaml("configs/attacks.yaml")
    settings = load_yaml("configs/settings.yaml")

    model_name = model_config["model"]["name"]
    attacks = attack_config["attacks"]
    max_samples = settings["run"]["max_samples"]
    output_file = settings["run"]["output_file"]

    behaviors = load_behaviors("data/behaviors.csv", max_samples)

    client = load_openai_client()

    results = run_benchmark(
        client,
        model_name,
        behaviors,
        attacks,
        output_file
    )

    print("\nDONE")
    print(f"Saved to: {output_file}")
    print(f"Rows: {len(results)}")


if __name__ == "__main__":
    main()
