class FileStatus:
    # constructor (Plato's Form)
    def __init__(self, filepath):
        self.filepath = filepath #attribute
        self.has_YAML = None #attribute
        self.numOfWords = None #attribute
        self.has_GPT = None #attribute
        self.dateCreated = None #attribute
        self.dateEdited = None #attribute
        #print(f'Constructor filepath: {filepath}')
        
# accessors
    def get_filepath(self):
        return self.filepath
    def get_hasYAML(self):
        return self.has_YAML
    def get_hasGPT(self):
        return self.has_GPT
    def get_numOfWords(self):
        return self.numOfWords

# accessors are channels/interfaces to and from the object

# =================== SAVE YOUR FILES EVERY TIME ========================== #

    def check_yaml(self):
        # sets has_YAML to true/false
        try:
            file = open(self.filepath) #auto set to reading 'r'
            first_line = file.readline().strip() 
            #searches for '---' (indicates start/end of yaml. yaml must be on top of file)
            if first_line != "---":
                self.has_YAML = False
                file.close()
                return self.has_YAML
            # search for the second "---" (indicates end of yaml)
            for line in file: 
                if line.strip() == "---":
                    self.has_YAML = True # has YAML status
                    file.close() # exit file
                    return self.has_YAML
            #if the second "---" is not found
            self.has_YAML = False
            file.close() #exit the file

        except FileNotFoundError:
            print(f"Error: File not found at: {self.filepath}")

    def check_gpt(self):
        #sets has_GPT to true/false like check_yaml()
        try:
            file = open(self.filepath)
            longstring = file.read() #stores the whole file in one string
            file.close() # exit

            #remove puncuations like project 4
            cleaned = ""
            for ch in longstring:
                if ch.isalpha():
                    cleaned += ch
                else:
                    cleaned += " "
            cleaned = cleaned.lower()
            self.has_GPT = False
            #split into words
            for word in cleaned.split(): #no quotes = a space (" ") as argument
                if word == "gpt":
                    self.has_GPT = True
                    break #no point in continuing
                    
        except FileNotFoundError:
            print(f"Error: File not found at: {self.filepath}")
   
    def check_howmanywords(self):
        #counts how many words, split then count
        try:
            file = open(self.filepath) #open file at filepath
            longstring = file.read() #store file
            file.close() #exit
            numofwords = 0
            cleaned = ""
            for ch in longstring:
                if ch.isalpha():
                    cleaned += ch
                else:
                    cleaned += " "
            cleaned = cleaned.lower()
            for word in cleaned.split():
              if len(word) >= 3:
                  numofwords += 1  
            self.numOfWords = numofwords

            
        except FileNotFoundError:
            print(f"Error: File not found at: {self.filepath}")
    # converts memory addresses into readable info
    def __str__(self):
        return f"{self.filepath} | YAML={self.has_YAML} | GPT={self.has_GPT} | Words={self.numOfWords}"