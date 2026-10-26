"""Small offline conversation state machine for a *synthetic* design demo.

This is NOT an LLM, medical advice system, voice assistant, or deployable service.
No network access, storage, notifications, or speech capabilities.
"""
from dataclasses import dataclass


@dataclass
class Session:
    last_concern: str = ""
    offered_draft: bool = False
    ended: bool = False


def respond(session: Session, user_text: str) -> str:
    """Return one bounded demo reply while retaining minimal in-session context."""
    if session.ended:
        return "This check-in has ended."

    message = user_text.lower().strip()
    if not message:
        return "I didn't catch that. Could you say it another way?"

    # Emergency routing before normal flow. In a real product, this would need
    # clinically approved policy, better classifiers, localized numbers, and QA.
    emergency = (
        "can't breathe" in message or "cannot breathe" in message
        or "chest pain" in message or "stroke" in message
        or (any(x in message for x in ("fell", "fallen", "fall"))
            and any(x in message for x in ("can't get up", "cannot get up", "hit my head")))
    )
    if emergency:
        return ("This could be an emergency. Please call your local emergency number "
                "now, or ask someone nearby to call. I can't place calls or send alerts.")

    if message in {"stop", "goodbye", "bye", "leave me alone", "i don't want to talk"}:
        session.ended = True
        return "Of course. I'll end our check-in now."

    if any(x in message for x in ("don't tell", "do not tell", "keep this from")):
        return ("I understand. This demo cannot contact or notify anyone, "
                "and it won't send a message about what you said.")

    if any(x in message for x in ("what dose", "how many pills", "increase my medicine", "stop my medicine")):
        return ("I can't advise on medication doses or changes. Please check with "
                "your pharmacist or healthcare professional.")

    if any(x in message for x in ("tell my daughter", "tell my son", "notify my", "call my", "text my")):
        session.offered_draft = True
        return ("I can help you draft a message, but I can't send or call anyone "
                "from this demo. Would you like to draft it together?")

    if session.offered_draft and message in {"yes", "yes please", "sure", "okay", "ok"}:
        session.offered_draft = False
        return "What would you like the message to say?"

    if "dizzy" in message or "dizziness" in message:
        session.last_concern = "dizziness"
        return "I'm sorry you've felt dizzy. Are you feeling dizzy right now?"

    if session.last_concern == "dizziness" and any(x in message for x in ("not right now", "not anymore", "it passed", "no")):
        return ("Thanks for clarifying. You mentioned dizziness earlier. "
                "A healthcare professional can help you evaluate it. "
                "Would you like help drafting a note to someone you trust?")

    if any(x in message for x in ("i'm fine", "im fine", "i'm okay", "im okay", "doing well")):
        return "I'm glad you shared that. Is there anything you'd like to talk about?"

    return "Thanks for telling me. Could you tell me a little more?"
