from tkinter import *

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter.upper()] + ' '
        else:
            cipher += ' '
    textbox2.delete(0, "end")
    textbox2.insert("end", cipher)

# Function to decrypt the string
# from morse to english
def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    textbox2.delete(0, "end")
    textbox2.insert("end", decipher)

def table():
    # Create a new window for the table
    table_window = Toplevel(root)
    table_window.title("Morse Code Table")
    table_window.geometry("400x400")
    table_window.configure(bg="#3E3E3E")

    # Display the table with proper grid layout and styling
    for i, (key, value) in enumerate(MORSE_CODE_DICT.items()):
        row = i // 5
        col = i % 5
        label = Label(table_window, text=f"{key}: {value}", fg="#FFFFFF", bg="#3E3E3E", font=("Arial", 12), anchor="center")
        label.grid(row=row, column=col, pady=5, padx=5, sticky="nsew")
    
    # Adjust row and column weights for proper resizing
    for i in range(6):
        table_window.grid_rowconfigure(i, weight=1)
    for i in range(5):
        table_window.grid_columnconfigure(i, weight=1)

root = Tk()
root.title("Morse Code Converter")
root.geometry("1000x700")
root.configure(bg='#3E3E3E')  # Setting background color

# Labels and Entry Widgets
label1 = Label(root, text="Enter your text for converting", font=("Arial", 14), bg="#3E3E3E", fg="#FFFFFF", anchor="center")
label1.place(x=30, y=50, width=400)
textbox1 = Entry(root, font=("Arial", 14), bg="#FFFFFF")
textbox1.place(x=30, y=100, width=400, height=30)
textbox1.focus()

label2 = Label(root, text="Result:", font=("Arial", 14), bg="#3E3E3E", fg="#FFFFFF", anchor="center")
label2.place(x=30, y=150, width=400)
textbox2 = Entry(root, font=("Arial", 14), bg="#FFFFFF")
textbox2.place(x=30, y=200, width=400, height=30)

# Buttons
encrypt_button = Button(root, text="Encrypt", command=lambda: encrypt(textbox1.get()), font=("Arial", 14), bg="#4CAF50", fg="#FFFFFF")
encrypt_button.place(x=30, y=250, width=100)
decrypt_button = Button(root, text="Decrypt", command=lambda: decrypt(textbox1.get()), font=("Arial", 14), bg="#FF5733", fg="#FFFFFF")
decrypt_button.place(x=150, y=250, width=100)
table_button = Button(root, text="Morse Code Table", command=table, font=("Arial", 14), bg="#3498DB", fg="#FFFFFF")
table_button.place(x=270, y=250, width=150)

root.mainloop()
