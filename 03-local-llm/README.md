# Local models & agent workflow exploration

**Scope:** Hands-on exploration; not a deployed autonomous system or quantitative research paper.

## What I explored

- Ran **Ollama** locally with **Qwen3 8B**, comparing responsiveness and instruction-following for practical tasks with expectations formed from cloud assistants.
- Explored role-based, multi-agent workflows in **StarNet**, including the idea of separate research, design and oversight roles for ecommerce work.
- Considered when faster hosted models are more appropriate than CPU-bound local inference on a personal Mac.

## Friction I encountered

Local inference was slow enough to disrupt normal iteration. That made it important to distinguish tasks that need a highly capable model from simpler tasks that can be prepared offline. This was a qualitative working observation, **not a benchmark with timed results**.

## Prompt artifact: product research reviewer

See [commerce-research-prompt.md](commerce-research-prompt.md) for a sample reusable task prompt. It requires evidence, an explicit unknowns section, and a human approval step before publication—appropriate constraints for systems that can otherwise confidently invent market data.

## Next steps I'd test

1. Record prompts and sample outputs with model/version and a stopwatch-based latency log.
2. Use the same small set of ecommerce questions across models and rate factual grounding, cost and edit effort.
3. Gate agent recommendations behind human review; never let an agent assume it has verified a sales trend without a dated source.
4. Add API-based execution only after clear tool permissions, usage limits, secret handling and evaluation checks are in place.

No results or improvements are claimed until measured.
