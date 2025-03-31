import flet as ft  
import pyperclip  

MORSE_CODE = { 
    'A': '.-',
    'B': '-...', 
    'C': '-.-.', 
    'D': '-..', 
    'E': '.', 
    'F': '..-.', 
    'G': '--.', 
    'H': '....',
    'I': '..', 
    'J': '.---', 
    'K': '-.-', 
    'L': '.-..', 
    'M': '--', 
    'N': '-.', 
    'O': '---', 
    'P': '.--.',
    'Q': '--.-', 
    'R': '.-.', 
    'S': '...', 
    'T': '-', 
    'U': '..-', 
    'V': '...-', 
    'W': '.--', 
    'X': '-..-', 
    'Y': '-.--', 
    'Z': '--..', 
    '1': '.----', 
    '2': '..---', 
    '3': '...--', 
    '4': '....-', 
    '5': '.....',
    '6': '-....', 
    '7': '--...', 
    '8': '---..', 
    '9': '----.', 
    '0': '-----', 
    ' ': '//'
}

POLAR_CENIT = {
    'P': 'C', 'O': 'E', 'L': 'N', 'A': 'I', 'R': 'T',
    'C': 'P', 'E': 'O', 'N': 'L', 'I': 'A', 'T': 'R'
}

def text_to_morse(message):
    morse = []
    for char in message.upper():
        morse.append(MORSE_CODE.get(char, char))  
    return '/'.join(morse)  

def morse_to_text(morse):
    text = []
    words = morse.split(' // ')
    for word in words:
        letters = word.split('/')  
        decrypted_word = []
        for code in letters:
            found = False
            for i in range(len(MORSE_CODE)):  
                letter = list(MORSE_CODE.keys())[i]  
                morse_symbol = list(MORSE_CODE.values())[i]  
                if morse_symbol == code:  
                    decrypted_word.append(letter)
                    found = True
                    break
            if not found:
                decrypted_word.append(code)  
        text.append(''.join(decrypted_word))
    return ' '.join(text)

def letters_to_numbers(message):
    numbers = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in message.upper():
        if char in alphabet:
            numbers.append(str(alphabet.index(char) + 1))  
    return ' '.join(numbers)

def numbers_to_letters(number_str):
    letters = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    parts = number_str.split()
    for part in parts:
        if part.isnumeric():  
            num = int(part)
            if 1 <= num <= 26:
                letters.append(alphabet[num-1])
    return ''.join(letters)

def polar_cenit_cipher(message, encrypt=True):
    result = []
    polar_cenit_keys = list(POLAR_CENIT.keys())
    polar_cenit_values = list(POLAR_CENIT.values())
    
    if encrypt:
        swap_rules = POLAR_CENIT
    else:
        swap_rules = {}
        for i in range(len(polar_cenit_keys)):
            swap_rules[polar_cenit_values[i]] = polar_cenit_keys[i]

    for char in message.upper():
        result.append(swap_rules.get(char, char))  
    return ''.join(result)

def main(page: ft.Page):
    page.title = "Secret Message Machine"
    page.window_width = 600
    page.window_height = 600
    
    input_box = ft.TextField(label="Your Message", multiline=True, height=100)
    output_box = ft.TextField(label="Result", multiline=True, height=100, read_only=True)
    
    cipher_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option("Morse Code"),
            ft.dropdown.Option("A1Z26"),
            ft.dropdown.Option("Polar Cenit")
        ],
        value="Morse Code",
        width=200
    )
    
    def process_message(encrypt):
        message = input_box.value.strip()
        if not message:
            output_box.value = "Please enter a message!"
            page.update()
            return
            
        method = cipher_dropdown.value
        try:
            if method == "Morse Code":
                if encrypt:
                    output_box.value = text_to_morse(message)
                else:
                    output_box.value = morse_to_text(message)
            elif method == "A1Z26":
                if encrypt:
                    output_box.value = letters_to_numbers(message)
                else:
                    output_box.value = numbers_to_letters(message)
            elif method == "Polar Cenit":
                output_box.value = polar_cenit_cipher(message, encrypt)
            page.update()
        except Exception as e:
            output_box.value = f"Error: {str(e)}"
            page.update()
    
    def copy_result(e):
        if output_box.value:
            pyperclip.copy(output_box.value)
            output_box.value = output_box.value + "(Copied!)"
            page.update()

    page.add(
        ft.Column([
            input_box,
            cipher_dropdown,
            ft.Column([
                ft.ElevatedButton("Encrypt", on_click=lambda e: process_message(True)),
                ft.ElevatedButton("Decrypt", on_click=lambda e: process_message(False)),
            ]),
            ft.ElevatedButton("Copy", on_click=copy_result),
            output_box
        ], spacing=10)
    )

ft.app(target=main)


#W3 schools(2025)Python String join() Method,https://www.w3schools.com/python/ref_string_join.asp
#Toppr(2025)Python chr() https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/built-in/chr/python-chr/#:~:text=What%20is%20a%20char%20in,the%20keyboard%20in%20one%20keystroke.
#W3 schools(2025) Python String isnumeric() Method,https://www.w3schools.com/python/ref_string_isnumeric.asp
#W3 schools(2025) Python Dictionary get() Method,https://www.w3schools.com/python/ref_dictionary_get.asp
#W3 schools(2025) not Operator in Python,https://www.geeksforgeeks.org/python-not-keyword/
#W3 schools(2025) Python String split() Method,https://www.w3schools.com/python/ref_string_split.asp
#W3 schools(2025) Python List index() Method,https://www.w3schools.com/python/ref_list_index.asp
#W3 schools(2025) Python Dictionary keys() Method,https://www.w3schools.com/python/ref_dictionary_keys.asp