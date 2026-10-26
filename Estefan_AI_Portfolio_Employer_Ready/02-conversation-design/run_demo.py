"""Run a synthetic example without external services."""
from agent import Session, respond


def main():
    session = Session()
    print("Synthetic check-in transcript — not a voice agent or clinical software\n")
    print("Assistant: Hello. How are you feeling today?")
    for utterance in [
        "A little dizzy when I got up.",
        "Not right now. It passed.",
        "Tell my daughter about it.",
        "Yes",
    ]:
        print(f"User: {utterance}")
        print(f"Assistant: {respond(session, utterance)}")


if __name__ == "__main__":
    main()
