class Console:
    def display_menu():
        settings = {model: "gpt-3.5-turbo", max_tokens: 1020, temperature: 1, n: 1}
        while (True):
            print("###############\n")
            print("1: Change prompt settings")
            print("2: Create a text prompt")
            print("3: Create an image prompt")
            print("4: Create an audio prompt")
            print("5: Exit program")
            choice = input("Enter your choice: ")
            print("###############\n")
            
            match choice:
                case 1: 
                    this.settings_menu()
                    
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    break

    def settings_menu():
        while(True):
            print("1: Model (Default: gpt-3.5-turbo)")
            print("2: Temperature (Default: 1)")
            print("3: Amount of responses (Default: 1)")
            print("4: Max tokens (Default: 1020)")
            print("5: Previous menu")
            settings_choice = input("Enter your choice ")

            match settings_choice:
                case 1:
                    while(True):
                        print("1: gpt-3.5.turbo")
                        print("2: gpt-4")
                        model = input("Enter which model you would like to use: ")
                        
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    break