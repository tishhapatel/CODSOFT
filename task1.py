import random
import re


class RuleBot:
    ##response
    negative_res = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

    random_question = (
        "What products are you looking for today?",
        "Are you shopping for yourself or someone else?",
        "What type of deals are you interested in?",
        "Do you prefer online shopping or in-store shopping?",
        "What is your preferred method of payment?"
    )

    def __init__(self):
        self.shopping_babble = {
            'product_inquiry_intent': r'.*\s*products.*',
            'deal_inquiry_intent': r'.*\s*deals.*',
            'payment_inquiry_intent': r'.*\s*payment.*'
        }

    def greet(self):
        self.name = input("What is your name?\n")
        will_help = input(
            f"Hi {self.name}, I am ShopBot. Can I assist you with your shopping today?\n").lower()
        if will_help in self.negative_res:
            print("Have a great day!")
            return
        else:
            self.chat()

    def make_exit(self, reply):
        if reply in self.exit_commands:
            print("Have a great shopping day!")
            return True
        return False

    def chat(self):
        reply = input(random.choice(self.random_question) + "\n").lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply) + "\n").lower()

    def match_reply(self, reply):
        for intent, regex_pattern in self.shopping_babble.items():
            if re.search(regex_pattern, reply):  # Changed re.match to re.search for flexibility
                if intent == 'product_inquiry_intent':
                    return self.product_inquiry_intent()
                elif intent == 'deal_inquiry_intent':
                    return self.deal_inquiry_intent()
                elif intent == 'payment_inquiry_intent':
                    return self.payment_inquiry_intent()

        return self.no_match_intent()  # No match found, use fallback response

    def product_inquiry_intent(self):
        responses = (
            "We have a wide range of products including electronics, clothing, and home goods.",
            "Are you looking for any specific brand or type of product?"
        )
        return random.choice(responses)

    def deal_inquiry_intent(self):
        responses = (
            "We have great deals on electronics and home appliances this week.",
            "You can find amazing discounts in our clearance section.",
            "Our members get exclusive deals and early access to sales."
        )
        return random.choice(responses)

    def payment_inquiry_intent(self):
        responses = (
            "We accept all major credit cards, debit cards, and mobile payments.",
            "You can also use gift cards or store credit for your purchases.",
            "We offer flexible payment options including installment plans."
        )
        return random.choice(responses)

    def no_match_intent(self):
        responses = (
            "Can you please provide more details?",
            "I'm here to help, tell me more!",
            "Interesting. Can you tell me more about what you need?",
            "I see. How can I assist you further?",
            "How do you feel about our current offers?"
        )
        return random.choice(responses)


# Running the bot
bot = RuleBot()
bot.greet()
