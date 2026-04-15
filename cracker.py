import hashlib

target_hash = input("Enter hash to crack: ")

wordlist = ["123456", "password", "admin", "hello123", "qwerty"]

for word in wordlist:
    if hashlib.sha256(word.encode()).hexdigest() == target_hash:
        print("Password found:", word)
        break
else:
    print("Password not found")
