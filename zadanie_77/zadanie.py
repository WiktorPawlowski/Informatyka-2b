def letter_to_number(c):
    return ord(c) - ord('A')

def number_to_letter(n):
    return chr((n % 26) + ord('A'))

def encrypt_vigenere(text, key):
    encrypted = ''
    key_index = 0
    key_length = len(key)
    for char in text:
        if char.isalpha():
            shift = letter_to_number(key[key_index % key_length])
            encrypted += number_to_letter((letter_to_number(char) + shift) % 26)
            key_index += 1
        else:
            encrypted += char
    return encrypted

def decrypt_vigenere(ciphertext, key):
    decrypted = ''
    key_index = 0
    key_length = len(key)
    for char in ciphertext:
        if char.isalpha():
            shift = letter_to_number(key[key_index % key_length])
            decrypted += number_to_letter((letter_to_number(char) - shift) % 26)
            key_index += 1
        else:
            decrypted += char
    return decrypted

def letter_frequencies(text):
    frequencies = {chr(i + ord('A')): 0 for i in range(26)}
    for char in text:
        if char.isalpha():
            frequencies[char] += 1
    return frequencies

def coincidence_index(frequencies, n):
    numerator = sum(f * (f - 1) for f in frequencies.values())
    denominator = n * (n - 1)
    return numerator / denominator if denominator != 0 else 0

def estimate_key_length(kappa_o):
    return 0.0285 / (0.0385 - kappa_o)

with open('zadanie_77/dokad.txt', 'r', encoding='utf-8') as f:
    dokad_text = f.read().strip()

key_77_1 = "LUBIMYCZYTAC"
only_letters = [c for c in dokad_text if c.isalpha()]
repetitions = (len(only_letters) + len(key_77_1) - 1) // len(key_77_1)
encrypted_text_77_1 = encrypt_vigenere(dokad_text, key_77_1)

with open('zadanie_77/szyfr.txt', 'r', encoding='utf-8') as f:
    szyfr_lines = f.readlines()
cipher_text = szyfr_lines[0].strip()
cipher_key = szyfr_lines[1].strip()
decrypted_text_77_2 = decrypt_vigenere(cipher_text, cipher_key)

frequencies = letter_frequencies(cipher_text)
total_letters = sum(frequencies.values())
letter_counts = '\n'.join(f"{letter}: {count}" for letter, count in frequencies.items())
kappa_o = coincidence_index(frequencies, total_letters)
estimated_key_length = estimate_key_length(kappa_o)

with open('Vigenere_wyniki.txt', 'w', encoding='utf-8') as f:
    f.write("77.1\n")
    f.write(f"Liczba powtórzeń klucza: {repetitions}\n")
    f.write(f"Zaszyfrowany tekst:\n{encrypted_text_77_1}\n\n")
    f.write("77.2\n")
    f.write("Odszyfrowany tekst:\n")
    f.write(f"{decrypted_text_77_2}\n\n")
    f.write("77.3\n")
    f.write("a) Liczby wystąpień liter:\n")
    f.write(f"{letter_counts}\n\n")
    f.write("b) Szacunkowa długość klucza:\n")
    f.write(f"Szacowana długość klucza: {estimated_key_length:.2f}\n")
    f.write(f"Dokładna długość klucza: {len(cipher_key)}\n")
