import tkinter as tk

"""
    Simple Word Counter with a Tkinter GUI in python, replicates the WC command in linux provided in the man pages by "wc"
    To run, use the terminal command "python word_counter.py" make sure to have python3 installed and the module tkinter installed as well
"""

class WordCounter:
    def __init__(self, screen_name="Main", base_name="WC", class_name="Word Counter"):
        #initializing the TkInter Window
        self.root = tk.Tk(screenName=screen_name, baseName=base_name, className=class_name, useTk=True)
        
        self.root.title("Word Counter App") #this will set the title of the Tkinter window
        
        label = tk.Label(self.root, text="Enter text to count words: ")
        label.pack()
        
        # I need a text widget that will allow multi-line input
        self.text_input = tk.Text(self.root, height=10, width=50) #10 lines by 50 chars text box
        self.text_input.pack() # packs it in the tk window
        
        # This will be the submit button
        self.count_button = tk.Button(self.root, text="Count Words", command=self.count_words) #you need to pass in the root Tk object, with a text set and a command 
        self.count_button.pack()
        
        self.result_label = tk.Label(self.root, text="Word count will appear here. ")
        self.result_label.pack()
        
        self.result_label2 = tk.Label(self.root, text="Letter count will appear here.")
        self.result_label2.pack()
        
    def count_words(self):
        # you need to get the input text entered by the user in the tkinter text field
        inputtext = self.text_input.get("1.0", "end-1c") #from line 1.0 to end of line count of the text field
        
        #split the text by whitespace and then count the words
        word_count = len(inputtext.split()) #splits by whitespace
        letter_count = len(list(inputtext)) #splits by char
        
        self.result_label.config(text=f"Word count: {word_count}")
        self.result_label2.config(text=f"Letter count: {letter_count}")
        
    def run(self):
        #this will start the Tkinter event loop
        self.root.mainloop()
        
#this creates an instance of the word counter app
app = WordCounter()
app.run() #calls on the run method of the Tk class