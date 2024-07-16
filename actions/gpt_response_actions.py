import openai
from ascii_magic import AsciiArt
from numpy import dot
from numpy.linalg import norm
import time
from pathlib import Path

class openAIActions:
    def chat_prompt(self, settings, prompt):
        if prompt["system"] == "Default":
            response = openai.chat.completions.create(
                model = settings["model"],
                messages = [{"role": "user", "content": prompt["user"]}],
                max_tokens = settings["max_tokens"], 
                temperature = settings["temperature"],
                n = settings["n"]  
        )
        else:
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
        fine_tune_job = openai.fine_tuning.jobs.create(training_file=file_id, model="gpt-3.5-turbo")
        seconds_elapsed = 0
        while openai.fine_tuning.jobs.retrieve(fine_tune_job.id).fine_tuned_model == None:
            print(f"Fine tuning in progress, current seconds elapsed: {seconds_elapsed}...")
            seconds_elapsed += 5
            time.sleep(5)
        fine_tuned_model = openai.fine_tuning.jobs.retrieve(fine_tune_job.id).fine_tuned_model
        with open("../bookkeeping/personal_models.txt", 'a') as file:
            file.write(str(fine_tuned_model))
        return fine_tuned_model

    def speech_to_text(self, file):
        audio_file = open(file, "rb")
        audio_text = openai.audio.transcriptions.create(
            file=audio_file,
            model="whisper-1",)
        #$.0006/minute cost
        print(audio_text.text)

    def text_to_speech(self, text, voice_model):
        speech_file_path = Path(__file__).parent / "speech.mp3"
        response = openai.audio.speech.create(
            model="tts-1",
            voice=voice_model,
            input=text
        )
        response.stream_to_file(speech_file_path)
        return speech_file_path
        

    def print_chat_gpt_response(self, response):
        print(f"Model: {response.model}")
        print(f"Finish reason: {response.choices[0].finish_reason}")
        #for i in response.choices[i].message.content:
        print(f"ChatGPT's response: {response.choices[0].message.content}")
        print(f"Prompt tokens used: {response.usage.prompt_tokens}")
        print(f"Completion tokens used: {response.usage.completion_tokens}")
        print(f"Total tokens used: {response.usage.total_tokens}")