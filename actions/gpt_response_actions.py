import openai
from ascii_magic import AsciiArt
from numpy import dot
from numpy.linalg import norm

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
    
    def get_chat_gpt_image_response(self, settings, image_prompt, image_size):
        response = openai.images.generate(
            prompt = image_prompt,
            size = image_size,
            n = settings["n"]  
        )
        image_url = response.data[0].url
        print(image_url)
        #my_art = AsciiArt.from_image(image_url)
        #my_art.to_terminal()
        return 0
    
    def get_chat_gpt_embedding_response(self, prompt):
        embedding_object = {}
        response = openai.embeddings.create(input=prompt, model="text-embedding-ada-002")
        embedding_object["embed"] = response.data[0].embedding 
        embedding_object["total_tokens"] = response.usage.total_tokens
        return embedding_object

    def compare_two_embeddings(self, promptList):
        cos_sim = dot(promptList[0], promptList[1]) / (norm(promptList[0]) * norm(promptList[1]))
        return round(cos_sim, 2)

    def print_chat_gpt_response(self, response):
        print(f"Model: {response.model}")
        print(f"Finish reason: {response.choices[0].finish_reason}")
        print(f"ChatGPT's response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens}")