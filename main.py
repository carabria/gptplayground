import openai
import os
from console import Console
from tokentracker import tokenTracker

class Shazbot:
    def main(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        token_tracker = tokenTracker()
        console = Console()

        prompt = input("Enter your prompt here: ")
        total_tokens_used = console.display_menu()
        token_tracker.write_tokens_to_file(total_tokens_used)

if __name__ == "__main__":
    shazbot = Shazbot()
    shazbot.main()
