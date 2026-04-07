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

    results, metrics = run_benchmark(
        client,
        model_name,
        behaviors,
        attacks,
        output_file
    )

    print("\nDONE")
    print(f"Saved to: {output_file}")
    print(f"Rows: {len(results)}")
    print("\nMetrics:")
    print(f"Total samples: {metrics['total_samples']}")
    print(f"Refused: {metrics['refused']}")
    print(f"Not refused: {metrics['not_refused']}")
    print(f"Errors: {metrics['errors']}")
    print(f"Refusal rate: {metrics['refusal_rate']:.2%}")
    print(f"Attack success rate: {metrics['attack_success_rate']:.2%}")
    print(f"Error rate: {metrics['error_rate']:.2%}")


if __name__ == "__main__":
    main()
