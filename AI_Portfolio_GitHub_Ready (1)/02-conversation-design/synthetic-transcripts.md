# Synthetic dialogue examples (not real conversations)

These are written hypothetical examples to explore flow, language and scope. They are not Sensi recordings, real personal histories, or transcripts sampled from a model.

## Example A — context and a missing integration

**Assistant:** Hello. How are you feeling today?

**User:** A little dizzy when I got up.

**Assistant:** I'm sorry you've felt dizzy. Are you feeling dizzy right now?

**User:** Not right now. It passed.

**Assistant:** Thanks for clarifying. You mentioned dizziness earlier. A healthcare professional can help you evaluate it. Would you like help drafting a note to someone you trust?

**User:** Tell my daughter about it.

**Assistant:** I can help you draft a message, but I can't send or call anyone from this demo. Would you like to draft it together?

## Example B — action integrity under pressure

**User:** I fell and can't get up.

**Assistant:** This could be an emergency. Please call your local emergency number now, or ask someone nearby to call. I can't place calls or send alerts.

**Design note:** The assistant must not say emergency services or family have been notified, because the demo has no communication tool.

## Example C — respecting a boundary

**User:** I don't want to talk.

**Assistant:** Of course. I'll end our check-in now.

**Design note:** Continuing to ask questions here would be an unhelpful conversational dead end.
