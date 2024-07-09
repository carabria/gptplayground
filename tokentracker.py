class tokenTracker:
    def read_tokens_on_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return int(file.read().strip())
        except FileNotFoundError:
            return 0
        except ValueError:
            print("There was an issue with the file! Not a number! Returning 0.")
            return 0
    
    def write_tokens_to_file(self, tokens, file_path='bookkeeping/tokens_used.txt'):
        current_tokens = self.read_tokens_on_file(file_path)
        new_tokens = current_tokens + tokens
        with open(file_path, 'w') as file:
            file.write(str(new_tokens))
