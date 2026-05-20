"""Cipher application with a simple shift cipher and Tkinter UI.

This module implements a configurable shift cipher that supports a combined
alphabet of Latin letters, digits, Cyrillic letters, Greek letters, Hebrew
letters, Arabic letters, and common symbols. Encoding and decoding are done
by shifting characters within that combined alphabet based on the input length.

The module also provides a minimal Tkinter UI for entering text and displaying
encoded or decoded results.
"""

import tkinter as tk


def __Main__():
    """Build and run the main Tkinter application.

    Creates the application window, input and output text widgets, and buttons
    for encoding and decoding. The function then enters the Tkinter event loop.
    """
    windowInit()

    label_text = tk.Label(root, text="Enter text to encode or decode")
    label_text.pack()

    moreText = tk.Text(root, height=10, width=50)
    moreText.pack()
    moreText.insert(tk.END, "")

    encodeButton = tk.Button(
        root,
        text="Encode",
        command=lambda: textReturn.insert(
            tk.END, cipher(moreText.get("1.0", tk.END).strip())
        ),
    )
    encodeButton.pack()

    decodeButton = tk.Button(
        root,
        text="Decode",
        command=lambda: textReturn.insert(
            tk.END, decode(moreText.get("1.0", tk.END).strip())
        ),
    )
    decodeButton.pack()

    textReturn = tk.Text(root, height=10, width=50)
    textReturn.pack()

    root.mainloop()


def start():
    """Run a minimal console demonstration of encode/decode.

    Prompts the user for input, prints the encoded text, and then prints the
    decoded text to verify that the encode/decode cycle returns the original
    string.
    """
    print("Type something")
    x = input()
    print(cipher(x))
    print(decode(cipher(x)))


def cipher(x):
    """Encode text by shifting each character forward in the combined alphabet.

    The shift amount is derived from the length of the input string. If the
    shift is larger than the size of the combined alphabet, the value wraps
    around using modulo arithmetic.

    Args:
        x (str): The plaintext string to encode.

    Returns:
        str: The encoded ciphertext.
    """
    cipher_num = len(x)
    while cipher_num > len(combine):
        cipher_num -= len(combine)

    encoded = ""
    for ch in x:
        idx = combine.index(ch)
        encoded += combine[(idx + cipher_num) % len(combine)]
    return encoded


def decode(x):
    """Decode text by shifting each character backward in the combined alphabet.

    The shift amount is derived from the length of the encoded string. If the
    shift is larger than the size of the combined alphabet, the value wraps
    around using modulo arithmetic.

    Args:
        x (str): The ciphertext string to decode.

    Returns:
        str: The decoded plaintext.
    """
    cipher_num = len(x)
    while cipher_num > len(combine):
        cipher_num -= len(combine)

    decoded = ""
    for ch in x:
        idx = combine.index(ch)
        decoded += combine[(idx - cipher_num) % len(combine)]
    return decoded


def windowInit():
    """Initialize the Tkinter root window.

    Sets the window title and geometry for the application.
    """
    global root
    root = tk.Tk()
    root.title("Cipher Module")
    root.geometry("1080x720")


# Latin lowercase letters
alphaL = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# Latin uppercase letters
alphaU = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# Cyrillic lowercase letters
crAlphaL = [
    'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
    'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э',
    'ю', 'я'
]

# Cyrillic uppercase letters
crAlphaU = [
    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О',
    'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э',
    'Ю', 'Я'
]

# Greek lowercase letters
grAlphaL = [
    'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο',
    'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω'
]

# Greek uppercase letters
grAlphaU = [
    'Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο',
    'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω'
]

# Hebrew letters
heAlpha = [
    'א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'כ', 'ל', 'מ', 'נ', 'ס',
    'ע', 'פ', 'צ', 'ק', 'ר', 'ש', 'ת'
]

# Arabic letters
arAlpha = [
    'ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض',
    'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي'
]

# Digits
num = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

# Common punctuation and whitespace symbols
symble = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '[', ']',
    '{', '}', '|', ':', ';', '<', '>', '.', '?', '/', '~', '`', ' ', ',', "'"
]

combine = (
    alphaL
    + alphaU
    + num
    + crAlphaL
    + crAlphaU
    + grAlphaL
    + grAlphaU
    + heAlpha
    + arAlpha
    + symble
)

__Main__()
