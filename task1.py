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
            f"Hi {self.name}, I am ShopBot. Can I assist you with your shopping today?\n")
        if will_help.lower() in self.negative_res:
            print("Have a great day!")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Have a great shopping day!")
                return True

    def chat(self):
        reply = input(random.choice(self.random_question)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for intent, regex_pattern in self.shopping_babble.items():
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'product_inquiry_intent':
                return self.product_inquiry_intent()
            elif found_match and intent == 'deal_inquiry_intent':
                return self.deal_inquiry_intent()
            elif found_match and intent == 'payment_inquiry_intent':
                return self.payment_inquiry_intent()

        if not found_match:
            return self.no_match_intent()

    def product_inquiry_intent(self):
        responses = ("We have a wide range of products including electronics, clothing, and home goods.\n",
                     "Are you looking for any specific brand or type of product?\n")
        return random.choice(responses)

    def deal_inquiry_intent(self):
        responses = ("We have great deals on electronics and home appliances this week.\n",
                     "You can find amazing discounts in our clearance section.\n",
                     "Our members get exclusive deals and early access to sales.\n")
        return random.choice(responses)

    def payment_inquiry_intent(self):
        responses = ("We accept all major credit cards, debit cards, and mobile payments.\n",
                     "You can also use gift cards or store credit for your purchases.\n",
                     "We offer flexible payment options including installment plans.\n")
        return random.choice(responses)

    def no_match_intent(self):
        responses = ("Can you please provide more details?\n", "I'm here to help, tell me more!\n",
                     "Interesting. Can you tell me more about what you need?\n",
                     "I see. How can I assist you further?\n",
                     "How do you feel about our current offers?\n")
        return random.choice(responses)


bot = RuleBot()
bot.greet()
