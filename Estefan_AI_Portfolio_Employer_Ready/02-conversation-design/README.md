# Conversational Check-In — Dialogue Design & Testing

**Focus:** Multi-turn conversation design, tone, context handling, response rules, and repeatable Python testing.

## The design problem

A check-in conversation should be short, clear and respectful while maintaining context. Two particularly dangerous conversational failures are **false reassurance** (sounding clinically certain without evidence) and **false action claims** (saying a caregiver was alerted when nothing was sent).

## Interaction contract

1. **Tone:** Respectful, adult-to-adult, plain language; no infantilizing language or forced cheer.
2. **Context:** Use only details provided in the current conversation. Do not invent prior memory, diagnoses or caregiver preferences.
3. **One thing at a time:** Ask at most one focused question per turn, unless immediate danger requires a clear next step.
4. **Urgency:** When there may be immediate danger, prioritize emergency guidance over ordinary check-in.
5. **Action honesty:** The demo **cannot call, message, dispatch or schedule** anyone. It must say so clearly rather than implying an action was completed.
6. **Privacy:** Do not assume consent to sharing. This local offline script does not transmit data externally.

See [system-prompt.md](prompts/system-prompt.md), [synthetic-transcripts.md](synthetic-transcripts.md), and the rubric in [evaluation-rubric.md](evaluation-rubric.md).

## Flow sketch

```text
Greeting → Listen → Classify urgency
                 ├── Immediate danger → Emergency guidance + honest limitation
                 ├── Need for clarification → One follow-up question
                 ├── Request to notify someone → Explain no messaging integration; offer drafting
                 ├── Medication/clinical question → No diagnosis/dosing; refer to clinician/pharmacist
                 └── Wants to stop → Respect choice and close
```

## Design vs implementation

The **system prompt** is a proposed spec for an LLM-powered future implementation; it is **not attached to a production API here**. The Python prototype is an intentionally bounded state machine, using a small set of patterns and in-session context. It demonstrates a testable flow and failure contracts in a reproducible, lightweight environment.

## Try the runnable demo

```bash
python3 run_demo.py
python3 -m unittest discover -s tests -v
python3 run_evals.py
```

Runs locally using the Python standard library; no key, mic, API, install, or private data needed.

## Example evaluation strategy

Use the synthetic scenarios to spot hallucinated abilities, repetitive questions, missed escalation signals, mismatched tone, and failures to carry context forward. The [checks](evals/scenarios.json) provide lightweight expected/forbidden phrase assertions and are lightweight behavior checks for the prototype. A production design would add consent-aware memory, real speech-recognition/error-repair testing, approved clinical escalation policy, integrations with verified success/failure feedback, human review, and privacy/compliance controls.

## Iteration note

A plausible initial prompt such as "Be warm, helpful and make sure a loved one knows about concerns" is unsafe because it leaves "helpful" undefined and encourages ungrounded claims that a notification was sent. The revised design explicitly requires tool confirmation before claiming any action. This is a **hypothetical design critique**, not a claim that live failures were observed.
