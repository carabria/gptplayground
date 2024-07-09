import openai
import os

class Shazbot:
    def main():
        openai.api_key = os.getenv("OPENAI_API_KEY")
        ai_actions = openAIActions()
        token_tracker = tokenTracker()
        
        prompt = input("Enter your prompt here: ")
        tokens_used = ai_actions.get_chat_gpt_response(prompt)
        token_tracker.write_tokens_to_file(tokens_used)

if __name__ == "__main__":
    #to be run when main.py is used as entry point for the program
    main()
