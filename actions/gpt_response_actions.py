import openai

class openAIActions:
    def get_chat_gpt_chat_response(self, settings, prompt):
        response = openai.chat.completions.create(
            model = settings["model"],
            messages = [{"role": "user", "content": prompt}],
            max_tokens = settings["max_tokens"], 
            temperature = settings["temperature"],
            n = settings["n"]  
        )
        self.print_chat_gpt_response(response)

        return response.usage.total_tokens
    
    def print_chat_gpt_response(self, response):
        print(f"Model: {response.model}")
        print(f"Finish reason: {response.choices[0].finish_reason}")
        print(f"ChatGPT's response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens}")