"""Run fixture-based text checks against the offline rules prototype."""
import json
from pathlib import Path
from agent import Session, respond


def main():
    path = Path(__file__).parent / "evals" / "scenarios.json"
    scenarios = json.loads(path.read_text(encoding="utf-8"))
    passed = 0
    for case in scenarios:
        session = Session()
        answer = ""
        for turn in case["turns"]:
            answer = respond(session, turn)
        output = answer.lower()
        valid = (all(piece.lower() in output for piece in case["must_include"])
                 and all(piece.lower() not in output for piece in case["must_not_include"])
                 and answer.count("?") <= 1)
        print(f"{'PASS' if valid else 'FAIL'} | {case['name']} | {answer}")
        passed += valid
    print(f"\nOffline demo assertions passing: {passed}/{len(scenarios)}")
    if passed != len(scenarios):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
