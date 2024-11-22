import tkinter as tk
from nltk import CFG, ChartParser
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget
import time
# Define the grammar
grammar=""

def get_grammar():
    global grammar
    grammarEntry = entryGrammar.get("1.0", "end-1c")
    if grammarEntry!="":
        grammar = CFG.fromstring(grammarEntry)

        print("entry1")
    else:
        grammar = CFG.fromstring("""
            E -> E '+' T | E '-' T | T
            T -> T '*' F | T '/' F | F
            F -> '(' E ')' | 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z' | '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
        """)
        print("entry2")




# Function to parse and display the trees
def parse_expression():
    expression = entry.get().split() #get the textbox entry and split it
    parser = ChartParser(grammar) #text analysis
    for tree in parser.parse(expression):
        display_tree(tree)
        root.update()  # Update the Tkinter window to show the tree
        time.sleep(1000)  # Pause for 1 second to show each step



def display_tree(tree):
    for widget in tree_frame.winfo_children():
        widget.destroy()

    cf = CanvasFrame(tree_frame)
    tc = TreeWidget(cf.canvas(), tree)
    cf.add_widget(tc, 10, 10)  # (10, 10) are the coordinates to place the tree
    cf.pack()


# Create the main window
root = tk.Tk()
root.title("CFG Parser")
root.configure(background="lightgray",borderwidth="8px")
root.minsize(1000,700)
root.maxsize(1000,700)
# Create and place the widgets
label = tk.Label(root, text="Enter an expression:",background="lightblue")
label.place(relx=0.75)

entry = tk.Entry(root, width=50,background="lightgreen")
entry.place(relx=0.65,rely=0.05)

button = tk.Button(root, text="Parse", command=parse_expression)
button.place(relx=0.79,rely=0.08)

#create and place the grammar text box
labelGrammar = tk.Label(root,text="paste the grammar")
labelGrammar.place(relx=0.18)

entryGrammar = tk.Text(root, width=50,height=10)
entryGrammar.place(relx=0.05,rely=0.05)

buttonGrammar = tk.Button(root, text="grammar", command=get_grammar)
buttonGrammar.place(relx=0.2,rely=0.3)


# Frame to display the tree
tree_frame = tk.Frame(root)
tree_frame.place(relx=0.05,rely=0.35)

# Run the application
root.mainloop() ## main loop of the aplication