import unittest
from nltk.chat.util import Chat
from chatbot import pairs

class TestChatBot(unittest.TestCase):
    def setUp(self):
        self.chatbot = Chat(pairs)

    def test_greeting_with_name(self):
        response = self.chatbot.respond("my name is John")
        possible_responses = [
            "Hello John, nice to meet you!",
            "Hi John, how are you today?"
        ]
        self.assertIn(response, possible_responses)

    def test_asking_name(self):
        response = self.chatbot.respond("what is your name?")
        possible_responses = [
            "My name is ChatBot!",
            "I'm ChatBot, nice to meet you!"
        ]
        self.assertIn(response, possible_responses)

    def test_how_are_you(self):
        response = self.chatbot.respond("how are you ?")
        possible_responses = [
            "I'm doing good, thanks for asking!",
            "I'm fine, thank you!"
        ]
        self.assertIn(response, possible_responses)

    def test_sorry(self):
        response = self.chatbot.respond("sorry about that")
        possible_responses = [
            "Its alright",
            "It's OK, never mind"
        ]
        self.assertIn(response, possible_responses)

    def test_unknown_input(self):
        response = self.chatbot.respond("xyzabc123")
        possible_responses = [
            "I'm not sure how to respond to that. Could you rephrase?",
            "Tell me more about that."
        ]
        self.assertIn(response, possible_responses)

if __name__ == '__main__':
    unittest.main()