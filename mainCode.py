import tkinter as tk

"""Simple Caesar-style cipher module.

This module defines a basic shift cipher that encodes and decodes text using a combined
character set of latin letters, digits, Cyrillic letters, Greek letters, Hebrew letters,
Arabic letters, and common symbols.
"""
def __init_():
    """Initialize the cipher module.

    This function is currently a placeholder and does not perform any initialization.
    It can be expanded in the future to set up any necessary state or configurations.
    """
    root = tk.Tk()
    root.title("Cipher Module")
    root.geometry("1080x720")
    root.mainloop()

def start():
    """Prompt the user for input, encode it, and decode it back.

    This function reads a line of text from standard input, prints the encoded result,
    and then prints the decoded result to verify the transformation.
    """
    print("Type something")
    x = input()
    print(cipher(x))
    print(decode(cipher(x)))

def cipher(x):
    """Encode a string by shifting each character forward in the combined alphabet.

    The shift amount is determined by the length of the input string. If the shift
    exceeds the length of the combined alphabet, it wraps around using modulo arithmetic.

    Args:
        x (str): The plaintext string to encode.

    Returns:
        str: The encoded ciphertext.
    """
    cipherNum = len(x)
    while cipherNum > len(combine):
        cipherNum -= len(combine)
    newWords = ""
    for ch in x:
        idx = combine.index(ch)
        newWords += combine[(idx + cipherNum) % len(combine)]
    return newWords

def decode(x):
    """Decode a string by shifting each character backward in the combined alphabet.

    The shift amount is determined by the length of the encoded string. If the shift
    exceeds the length of the combined alphabet, it wraps around using modulo arithmetic.

    Args:
        x (str): The ciphertext string to decode.

    Returns:
        str: The decoded plaintext.
    """
    cipherNum = len(x)
    while cipherNum > len(combine):
        cipherNum -= len(combine)
    newWords = ""
    for ch in x:
        idx = combine.index(ch)
        newWords += combine[(idx - cipherNum) % len(combine)]
    return newWords

#print("Hello, World")

alphaL = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphaU = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
crAlphaL =['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
crAlphaU =['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
grAlphaL = ['α','β','γ','δ','ε','ζ','η','θ','ι','κ','λ','μ','ν','ξ','ο','π','ρ','σ','τ','υ','φ','χ','ψ','ω']
grAlphaU = ['Α','Β','Γ','Δ','Ε','Ζ','Η','Θ','Ι','Κ','Λ','Μ','Ν','Ξ','Ο','Π','Ρ','Σ','Τ','Υ','Φ','Χ','Ψ','Ω']
heAlpha = ['א','ב','ג','ד','ה','ו','ז','ח','ט','י','כ','ל','מ','נ','ס','ע','פ','צ','ק','ר','ש','ת']
arAlpha = ['ا','ب','ت','ث','ج','ح','خ','د','ذ','ر','ز','س','ش','ص','ض','ط','ظ','ع','غ','ف','ق','ك','ل','م','ن','ه','و','ي']
num = ['0','1','2','3','4','5','6','7','8','9']
symble = ['!','@','#','$','%','^','&','*','(',')','-','=','+','[',']','{','}','|',':',';','<','>','.','?','/', '~','`',' ', ',']

combine = alphaL + alphaU + num + crAlphaL + crAlphaU + grAlphaL + grAlphaU + heAlpha + arAlpha + symble

start()
