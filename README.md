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
