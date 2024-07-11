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
    
    def get_chat_gpt_embedding_response(self, promptList):
        tokens_used = 0
        embeds = []
        embedding_object = {}
        for prompt in promptList:
            response = openai.embeddings.create(input=prompt, model="text-embedding-ada-002")
            tokens_used += response.usage.total_tokens
            embeds.append(response.data[0].embedding)
        cos_sim = dot(embeds[0], embeds[1]) / (norm(embeds[0]) * norm(embeds[1]))
        embedding_object["similarity"] = cos_sim
        embedding_object["total_tokens"] = tokens_used
        return embedding_object

    def print_chat_gpt_response(self, response):
        print(f"Model: {response.model}")
        print(f"Finish reason: {response.choices[0].finish_reason}")
        print(f"ChatGPT's response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens}")