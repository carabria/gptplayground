from actions.gpt_response_actions import openAIActions

class Console:
    ai_actions = openAIActions()
    fine_tuned_model = {}
    def display_menu(self):
        tokens_used_this_session = 0
        settings = {"model": "gpt-3.5-turbo", "max_tokens": 1020, "temperature": 1, "n": 1}
        while (True):
            choice = 0
            print("1: Change prompt settings")
            print("2: Create a text prompt")
            print("3: Create an image prompt")
            print("4: Create an audio prompt")
            print("5: Create embeddings")
            print("6: Fine tune model")
            print("Enter: Exit program")
            choice_input = input("Enter your choice: ")
            try:
                choice = int(choice_input)
                print("\n")
            except ValueError:
                if (choice_input == ""):
                    break
                else:
                    print("Please enter a whole number.")
                    print("\n")
            match choice:
                case 1: 
                    settings = self.settings_menu(settings)
                    continue
                case 2:
                    tokens_used = self.text_prompt_menu(settings)
                    tokens_used_this_session += tokens_used
                    continue
                case 3:
                    prompt = input("Enter your prompt here (Press enter to go back): ")
                    if (prompt == ""):
                        continue
                    #size = input("Enter your image's dimensions here (Press enter to go back): ")
                    #if (size == ""):
                        #break
                    tokens_used = self.ai_actions.image_prompt(settings, prompt)
                    tokens_used_this_session += tokens_used
                    continue
                case 4:
                    audio_file = input("Enter the path to your audio file, including the extension (Press enter to go back): ")
                    if (audio_file == ""):
                        break
                    audio_file = audio_file.lower().strip()
                    self.ai_actions.speech_to_text(audio_file)
                case 5:
                    tokens_used = self.embeddings_menu()
                    tokens_used_this_session += tokens_used
                    continue
                case 6:
                    training_data = input("Enter the path to your training data (Press enter to go back): ")
                    if (training_data == ""):
                        break
                    training_data = training_data.lower().strip()
                    trained_model = self.ai_actions.fine_tune(training_data)
                    settings["model"] = trained_model
                    
                case _:
                    print ("Please enter a whole number between 1 and 4")
                    continue
        return tokens_used_this_session
    
    def embeddings_menu(self):
        total_tokens_used_this_session = 0
        embeddingList = []
        embeddingObject = {}
        while(True):
            embedding = ""
            embedding_input = input(f"Enter {2-len(embeddingList)} prompts to compare (Press enter to go back): ")
            if (embedding_input == ""):
                break
            embeddingList.append(embedding_input)
            if len(embeddingList) == 2:
                embeddingObject = self.ai_actions.embed_prompt(embeddingList)
                print(f"Similarity: {embeddingObject["similarity"]}")
                print(f"Total tokens used: {embeddingObject["total_tokens"]}")
                total_tokens_used_this_session += embeddingObject["total_tokens"]
                embeddingList = []
        return total_tokens_used_this_session

    def settings_menu(self, settings):
        while(True):
            settings_choice = 0
            print(f"1: Model (Current: {settings["model"]})")
            print(f"2: Temperature (Current: {settings["temperature"]})")
            print(f"3: Amount of responses (Current: {settings["n"]})")
            print(f"4: Max tokens (Current: {settings["max_tokens"]})")
            print("5: Display current settings")
            print("Enter: Previous Menu")
            settings_input = input("Enter your choice: ")
            try:
                settings_choice = int(settings_input)
                print("\n")
            except ValueError:
                if (settings_input == ""):
                    break
                else:
                    print("Please enter a whole number between 1 and 4")

            match settings_choice:
                case 1:
                    while(True):
                        model = 0
                        print("1: gpt-3.5-turbo")
                        print("2: gpt-4")
                        print("3: Most recent fine tuned model")
                        print("4: Other fine tunbed model")
                        model_input = input("Enter which model you would like to use (enter to go back): ")
                        try:
                            model = int(model_input)
                            print("\n")
                        except ValueError:
                            if (model_input == ""):
                                break
                            else:
                                print("Please enter a whole number, either 1 or 2")
                        match model:
                            case 1:
                                settings["model"] = "gpt-3.5-turbo"
                                break
                            case 2:
                                settings["model"] = "gpt-4"
                                break
                            case 3:
                                settings["model"] = self.fine_tuned_model
                            case 4:
                                settings["model"] = input("Please enter a model: ")
                            case _:
                                print("Please enter a whole number, either 1 or 2")
                                continue

                case 2:
                    while(True):
                        temperature = 0
                        print("Input a number for temperature (from 0.0 to 2.0)")
                        print("Enter: Previous Menu")
                        temperature_input = input("Input temperature: ")
                        try:
                            temperature = float(temperature_input)
                            print("\n")
                        except ValueError:
                            if (temperature_input == ""):
                                break
                            else:
                                print("Please enter a number between 0.0 and 2.0")
                        if temperature >= 0.0 and temperature <= 2.0:
                            settings["temperature"] = temperature
                            break;
                        print("Please insert a number between 0.0 and 2.0")

                case 3:
                    while(True):
                        n = 0
                        print("Input a number for amount of responses (from 1 to 10)")
                        print("Enter: Previous Menu")
                        n_input = input("Enter responses: ")
                        try:
                            n = int(n_input)
                            print("\n")
                        except ValueError:
                            if (n == ""):
                                break
                            else:
                                print("Please enter a whole number between 1 and 10")
                        if n.is_integer() and n >= 1 and n <= 10:
                            settings["n"] = n
                            break
                        print("Please insert a whole number between 1 and 10")

                case 4:
                    while(True):
                        max_tokens = 0
                        print("Input the max amount of tokens you would like to use")
                        print("Enter: Previous Menu")
                        max_tokens_input = input("Enter tokens: ")
                        try:
                            max_tokens = int(max_tokens_input)
                            print("\n")
                        except ValueError:
                            if (max_tokens_input == ""):
                                break
                            else:
                                print("Please insert a whole number")
                        if max_tokens.is_integer():
                            settings["max_tokens"] = max_tokens
                            break
                        print("Please insert a whole number")
                case 5:
                    for item in settings:
                        print(f"{item}: {settings[item]}")
                    print("\n")
                case _:
                    print("Please insert a whole number between 1 and 4")
                    continue
        return settings
    
    def text_prompt_menu(self, settings):
        prompt_dictionary = {}
        prompt = input("Enter your system prompt here (Press enter to go back, enter 'default' for default): ")
        if (prompt == ""):
            return 0
        if (prompt.lower().strip() == "default"):
            prompt_dictionary["system"] = "Default"
        else:
            prompt_dictionary["system"] = prompt
        prompt = input("Enter your user prompt here (Press enter to go back): ")
        if (prompt == ""):
            return 0
        prompt_dictionary["user"] = prompt
        tokens_used = self.ai_actions.chat_prompt(settings, prompt_dictionary)
        return tokens_used