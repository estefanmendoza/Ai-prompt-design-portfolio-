# Conversational Interface — Dialogue Design & Testing

**Focus:** Multi-turn conversation design, context handling, response consistency, and testing

## Overview

A conversation prototype exploring how an assistant can maintain context, recognize different user intents, ask focused follow-up questions, and respond consistently across sensitive scenarios.

## Design principles

- **Clear language:** Concise, respectful, context-aware responses
- **Intent recognition:** Different paths for clarification, urgent situations, help requests, and conversation closure
- **Context continuity:** Track relevant information during a session
- **Reliable actions:** Distinguish suggestions from actions confirmed by connected tools
- **Iteration:** Evaluate dialogue behavior against defined examples and revise rules accordingly

## Components

- [Prompt specification](prompts/system-prompt.md)
- [Synthetic conversation examples](synthetic-transcripts.md)
- [Python conversation prototype](agent.py)
- [Automated unit tests](tests/test_agent.py)
- [Scenario checks](evals/scenarios.json)

## Run the prototype

```bash
python3 run_demo.py
python3 -m unittest discover -s tests -v
python3 run_evals.py
```

The prototype is a local, rule-based implementation of the conversation flow; the prompt specification documents a potential LLM interaction design. Together they illustrate design reasoning, working code, and repeatable testing.

## Design takeaway

Well-defined conversational behavior requires more than a tone instruction. Context, action permissions, fallback language, and expected responses should be explicit and testable.
