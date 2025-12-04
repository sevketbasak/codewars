from preloaded import MORSE_CODE

def decode_morse(morse_code):
    result = ""
    morse_code = morse_code.strip()
    words = morse_code.split('   ')
    for aga in words:
        letters = aga.split(' ')
        for ogo in letters:
            result += MORSE_CODE[ogo]
        result += " "
    return result[:-1]

decode_morse ('.... . -.--   .--- ..- -.. .')