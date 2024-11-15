import tkinter as tk
from tkinter import ttk

# Dicionário de conversão para código Morse
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'
}

def text_to_morse(text):
    """Converte texto para código Morse."""
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)

def convert_to_morse():
    """Converte o texto inserido pelo usuário e exibe o resultado."""
    input_text = text_input.get("1.0", tk.END).strip()
    morse_text = text_to_morse(input_text)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, morse_text)

# Criação da janela principal
root = tk.Tk()
root.title("Conversor de Texto para Código Morse")
root.geometry("500x400")
root.configure(bg="#282C34")

# Estilo
style = ttk.Style()
style.configure("TLabel", background="#282C34", foreground="#61AFEF", font=("Helvetica", 12))

# Título
title_label = ttk.Label(root, text="Conversor de Texto para Código Morse", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Caixa de entrada de texto
text_input = tk.Text(root, height=5, width=50, font=("Helvetica", 12), bg="#ABB2BF", fg="#282C34", wrap="word")
text_input.pack(pady=10)

# Botão de conversão
convert_button = tk.Button(root, text="Converter", command=convert_to_morse, font=("Arial", 12, "bold"), bg="#FFFFE0", fg="#006400")
convert_button.pack(pady=10)

# Caixa de saída do texto convertido
text_output = tk.Text(root, height=5, width=50, font=("Helvetica", 12), bg="#ABB2BF", fg="#282C34", wrap="word")
text_output.pack(pady=10)

# Inicia o loop da aplicação
root.mainloop()
