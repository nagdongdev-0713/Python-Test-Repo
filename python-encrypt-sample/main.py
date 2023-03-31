from cryptography.fernet import Fernet # 구글에서 뒤져본 cryptography 암호화 모듈 :)

# 128 암호화를 위해 키 생성!
key = Fernet.generate_key()

# 생성한 키로 암호화 객체 생성
cipher_suite = Fernet(key)

# 메시지를 암호화한다(encrypt str)
plaintext = b"Encryptest"
ciphertext = cipher_suite.encrypt(plaintext)

# 메시지를 암호화했던것을 다시 복호화(decrypt encrypted str)
decrypted_text = cipher_suite.decrypt(ciphertext)

print(f"평문 메시지: {plaintext}")
print(f"암호문: {ciphertext}")
print(f"복호화된 메시지: {decrypted_text}")
