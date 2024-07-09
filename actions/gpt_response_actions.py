import openai

class openAIActions:

    def get_chat_gpt_response(prompt):
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1020, 
            temperature=1
        )
        openAIActions.print_chat_gpt_response(response)

        return response.usage.total_tokens
    
    def print_chat_gpt_response(response):
        print(f"Model: {response.model}")
        print(f"Finish reason: {response.choices[0].finish_reason}")
        print(f"ChatGPT's response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens}")