# Jailbreak Benchmark Suite

A small benchmark suite for evaluating how an LLM responds to potentially unsafe prompts under different prompt wrappers.

## V1 Goals
- Load a dataset of prompts
- Apply multiple attack wrappers
- Query one model
- Save outputs to CSV
- Score simple refusal behavior
- Compute basic metrics

## V1 Scope
- 1 model
- 3 wrappers
- 1 rule-based judge
- CSV results
## Example Results

Model: gpt-4o-mini

- Total samples: 9  
- Refusal rate: 100%  
- Attack success rate: 0%

Observation:
Baseline prompt transformations (direct, roleplay, transform) were insufficient to bypass safety mechanisms.
