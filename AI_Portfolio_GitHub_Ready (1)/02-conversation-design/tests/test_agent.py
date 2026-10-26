"""Regression smoke tests for deterministic demo behavior, not LLM evaluation."""
import unittest
from agent import Session, respond


class CheckInTests(unittest.TestCase):
    def test_new_dizziness_asks_one_question(self):
        answer = respond(Session(), "I'm dizzy.")
        self.assertIn("right now", answer.lower())
        self.assertEqual(answer.count("?"), 1)

    def test_context_is_carried_into_next_turn(self):
        state = Session()
        respond(state, "I felt dizzy this morning")
        answer = respond(state, "Not right now; it passed")
        self.assertIn("dizziness earlier", answer.lower())
        self.assertEqual(answer.count("?"), 1)

    def test_emergency_overrides_regular_check_in(self):
        answer = respond(Session(), "I fell, hit my head and can't get up")
        self.assertIn("emergency", answer.lower())
        self.assertIn("can't place calls", answer.lower())

    def test_contact_request_does_not_claim_message_sent(self):
        answer = respond(Session(), "Tell my daughter")
        self.assertIn("can't send", answer.lower())
        self.assertNotIn("i notified", answer.lower())
        self.assertEqual(answer.count("?"), 1)

    def test_drafting_state(self):
        state = Session()
        respond(state, "Tell my son")
        answer = respond(state, "Yes")
        self.assertIn("what would you like", answer.lower())

    def test_medication_dose_is_not_given(self):
        answer = respond(Session(), "What dose should I take?")
        self.assertIn("can't advise", answer.lower())

    def test_stop_respected(self):
        state = Session()
        answer = respond(state, "Stop")
        self.assertIn("end", answer.lower())
        self.assertEqual(respond(state, "Hello"), "This check-in has ended.")

    def test_privacy_no_fake_contact(self):
        answer = respond(Session(), "Don't tell my son")
        self.assertIn("cannot contact", answer.lower())


if __name__ == "__main__":
    unittest.main()
