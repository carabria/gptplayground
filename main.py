import openai
import os
from tokentracker import tokenTracker
from actions.gpt_response_actions import openAIActions

class Shazbot:
    def main(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        ai_actions = openAIActions()
        token_tracker = tokenTracker()

        prompt = input("Enter your prompt here: ")
        tokens_used = ai_actions.get_chat_gpt_response(prompt)
        token_tracker.write_tokens_to_file(tokens_used)

if __name__ == "__main__":
    shazbot = Shazbot()
    shazbot.main()
