def rot13(text):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + 13) % 26 + start)
        else:
            result += char
    return result
input_text = "Hello, World!"
encrypted_text = rot13(input_text)
print(f"Original: {input_text}")
print(rot13('faseeh'))
print(rot13('snfrru'))
