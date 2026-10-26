# Estefan Mendoza
### AI Prompt Design · Conversational Systems · Applied LLM Workflows

**Austin, Texas** · [LinkedIn](https://www.linkedin.com/in/estefan-mendoza/)

I approach prompting as product design: define what the system should do, make its constraints explicit, test its behavior, then revise when the output misses the intent. My background combines AI-assisted product building, extensive customer-facing communication, and published writing.

**This portfolio separates what I have built, what I have explored, and what is a prototype.** It does not represent any Sensi.AI product or access to Sensi recordings or customer data.

## Selected work

| Project | What it demonstrates | Scope |
| :-- | :-- | :-- |
| **[01 / SANCTVM — prompting an ecommerce experience](01-sanctvm/README.md)** | Requirements-to-prompt translation, design constraints, end-to-end review, and learning from generated-app security findings | Real AI-assisted site and documented retrospective; illustrative prompt reconstructions |
| **[02 / Senior check-in dialogue prototype](02-conversation-design/README.md)** | Multi-turn flow, tone and privacy rules, truthful action boundaries, example system prompt, and a runnable offline test harness | Independent concept + demo; synthetic scenarios; **not a voice agent or deployed healthcare tool** |
| **[03 / Local LLM and agent workflow exploration](03-local-llm/README.md)** | Ollama/Qwen3 experiments, practical latency constraints, roles and review gates for agentic work | Exploratory experiments; **not a shipped automation platform** |

## My design approach

**Specify → Observe → Identify the failure → Tighten constraints → Test again.**

A good prompt isn't just a clever sentence. It is an interface contract: objectives, inputs, constraints, failure behavior, acceptable outputs, and observable tests. I use that approach in design work, writing, and AI-assisted product experiments.

## Run the conversation prototype

The offline demonstration uses **Python's standard library only**. It does not call an LLM or any external services, and deliberately does not simulate pretending that a real caregiver has been contacted.

```bash
cd 02-conversation-design
python3 run_demo.py
python3 -m unittest discover -s tests -v
python3 run_evals.py
```

Read the [conversation-design project](02-conversation-design/README.md) for limitations, decisions, and next steps. See [portfolio transparency](SCOPE_AND_ATTRIBUTION.md) for what is real versus illustrative.

## Writing

Published author, *A New Way to Think About AI* (2026), listed on Amazon and Barnes & Noble. The book examines the gap between asking AI questions and using it to create results.

## Relevant background

Eight-plus years of consultative sales, customer communication and account management, including insurance experience in a regulated industry. I'm especially interested in AI systems where tone, factual precision, escalation and human trust are central to the experience.

---

**Contact:** [LinkedIn](https://www.linkedin.com/in/estefan-mendoza/) · Austin, TX
