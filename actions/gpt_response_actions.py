import openai
from ascii_magic import AsciiArt
from numpy import dot
from numpy.linalg import norm

class openAIActions:
    def chat_prompt(self, settings, prompt):
        response = openai.chat.completions.create(
            model = settings["model"],
            messages = [{"role": "system", "content": prompt["system"]},{"role": "user", "content": prompt["user"]}],
            max_tokens = settings["max_tokens"], 
            temperature = settings["temperature"],
            n = settings["n"]  
        )
        self.print_chat_gpt_response(response)

        return response.usage.total_tokens
    
    def image_prompt(self, settings, image_prompt):
        response = openai.images.generate(
            prompt = image_prompt,
            size = "1024x1024",
            n = settings["n"]  
        )
        image_url = response.data[0].url
        print(image_url)
        #my_art = AsciiArt.from_image(image_url)
        #my_art.to_terminal()
        return 600 #approximation of tokens based on gpt-3.5-turbo model. 1024x1024 resolution costs $0.06.
    
    def embed_prompt(self, promptList):
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
    
    def fine_tune(self, file):
        training_data = openai.files.create(file=open(f"{file}.json", "rb"), purpose='fine-tune')
        file_id = training_data.id
        fine_tune_job = openai.fine_tuning.jobs.createA(training_file=file_id, model="gpt-3.5-turbo")
        openai.fine_tuning.jobs.retrieve(fine_tune_job.id).status
        fine_tuned_model = openai.fine_tuning.jobs.retrieve(fine_tune_job.id).fine_tune_model
        return fine_tuned_model

    def print_chat_gpt_response(self, response):
        print(f"Model: {response.model}")
        print(f"Finish reason: {response.choices[0].finish_reason}")
        print(f"ChatGPT's response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens}")