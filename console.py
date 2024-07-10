from actions.gpt_response_actions import openAIActions

class Console:
    def display_menu(self):
        ai_actions = openAIActions()
        tokens_used_this_session = 0
        settings = {"model": "gpt-3.5-turbo", "max_tokens": 1020, "temperature": 1, "n": 1}
        while (True):
            choice = 0
            print("1: Change prompt settings")
            print("2: Create a text prompt")
            print("3: Create an image prompt")
            print("4: Create an audio prompt")
            print("Enter: Go back")
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
                    prompt = input("Enter your prompt here: ")
                    tokens_used = ai_actions.get_chat_gpt_chat_response(settings, prompt)
                    tokens_used_this_session += tokens_used
                    continue
                case 3:
                    prompt = input("Enter your prompt here: ")
                    size = input("Enter your image's dimensions here: ")
                    tokens_used = ai_actions.get_chat_gpt_image_response(setings, prompt, size)
                    tokens_used_this_session += tokens_used
                    continue
                case 4:
                    pass
                case _:
                    print ("Please enter a whole number between 1 and 4")
                    continue
        return tokens_used_this_session

    def settings_menu(self, settings):
        while(True):
            settings_choice = 0
            print(f"1: Model (Current: {settings["model"]}")
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
                        print("1: gpt-3.5.turbo")
                        print("2: gpt-4")
                        model_input = input("Enter which model you would like to use (enter to go back): ")
                        try:
                            model = int(model_input)
                            print("\n")
                        except ValueError:
                            if (model == ""):
                                break
                            else:
                                print("Please enter a whole number, either 1 or 2")
                        match model:
                            case 1:
                                settings["model"] = "gpt-3.5.turbo"
                                break
                            case 2:
                                settings["model"] = "gpt-4"
                                break
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
                            if (temperature == ""):
                                break
                            else:
                                print("Please enter a number between 0.0 and 2.0")
                        if temperature_input.isnumeric and temperature >= 0.0 and temperature <= 2.0:
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
                            if (max_tokens == ""):
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