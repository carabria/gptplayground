from actions.gpt_response_actions import openAIActions

class Console:
    def display_menu():
        ai_actions = openAIActions()
        tokens_used_this_session = 0
        settings = {model: "gpt-3.5-turbo", max_tokens: 1020, temperature: 1, n: 1}
        while (True):
            print("###############\n")
            print("1: Change prompt settings")
            print("2: Create a text prompt")
            print("3: Create an image prompt")
            print("4: Create an audio prompt")
            print("Enter: Go back")
            choice = input("Enter your choice: ")
            print("###############\n")
            
            match choice:
                case 1: 
                    this.settings_menu()
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
                case "":
                    break
        return total_used_this_session

    def settings_menu():
        while(True):
            print("1: Model (Default: gpt-3.5-turbo)")
            print("2: Temperature (Default: 1)")
            print("3: Amount of responses (Default: 1)")
            print("4: Max tokens (Default: 1020)")
            print("Enter: Previous Menu")
            settings_choice = input("Enter your choice: ")

            match settings_choice:
                case 1:
                    while(True):
                        print("1: gpt-3.5.turbo")
                        print("2: gpt-4")
                        model = input("Enter which model you would like to use (enter to go back): ")
                        match model:
                            case 1:
                                settings.model = "gpt-3.5.turbo"
                                break
                            case 2:
                                settings.model = "gpt-4"
                            case "":
                                break
                case 2:
                    while(True):
                        print("Input a number for temperature (from 0.0 to 2.0)")
                        print("Enter: Previous Menu")
                        temperature = input("Enter temperature: ")
                        if temperature.isnumeric and temperature >= 0.0 and temperature <= 2.0:
                            settings.temperature = temperature
                            break;
                        elif temperature == "":
                            break
                        print("Please insert a number between 0.0 and 10")

                case 3:
                    while(True):
                        print("Input a number for amount of responses (from 1 to 10)")
                        print("Enter: Previous Menu")
                        n = input("Enter responses: ")
                        if n.is_integer() and n >= 1 and n <= 10:
                            settings.n = n
                            break
                        elif n == "":
                            break
                        print("Please insert a whole number between 1 and 10")
                case 4:
                    while(True):
                        print("Input the max amount of tokens you would like to use")
                        print("Enter: Previous Menu")
                        max_tokens = input("Enter tokens: ")
                        if max_tokens.is_integer():
                            settings.max_tokens = max_tokens
                            break
                        elif n == "":
                            break
                        print("Please insert a whole number.")
                case "":
                    break