import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def ceasar(word, shift_amount, cipher_direction):
    output_word = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in word:
        if letter in alphabet:
            word_index = (alphabet.index(letter) + shift_amount) % 26
            output_word += alphabet[word_index]
        else:
            output_word += letter
    print(f"Your message after {cipher_direction}: {output_word}")


print(art.logo)
repeat = "yes"
while repeat == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(text, shift, direction)
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'")
