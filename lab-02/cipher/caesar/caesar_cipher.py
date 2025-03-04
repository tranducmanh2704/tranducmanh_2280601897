from cipher.caesar.alphabet import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        encrypted_text = []
        for letter in text:
            if letter.isalpha():  # Chỉ xử lý chữ cái
                letter_index = self.alphabet.index(letter.upper())  # Dùng chữ hoa để tìm index
                output_index = (letter_index + key) % alphabet_len
                output_letter = self.alphabet[output_index]
                # Giữ nguyên chữ hoa hoặc chữ thường
                if letter.islower():
                    encrypted_text.append(output_letter.lower())
                else:
                    encrypted_text.append(output_letter)
            else:
                encrypted_text.append(letter)  # Ký tự không phải chữ cái giữ nguyên
        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        decrypted_text = []
        for letter in text:
            if letter.isalpha():  # Chỉ xử lý chữ cái
                letter_index = self.alphabet.index(letter.upper())  # Dùng chữ hoa để tìm index
                output_index = (letter_index - key) % alphabet_len
                output_letter = self.alphabet[output_index]
                # Giữ nguyên chữ hoa hoặc chữ thường
                if letter.islower():
                    decrypted_text.append(output_letter.lower())
                else:
                    decrypted_text.append(output_letter)
            else:
                decrypted_text.append(letter)  # Ký tự không phải chữ cái giữ nguyên
        return "".join(decrypted_text)
