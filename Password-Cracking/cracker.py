import hashlib

target_hash = input("Enter hash to crack: ") 
/* here we have to enters the hash we recieved from entering the original password from the hashing */
wordlist = ["123456", "password", "admin", "hello123", "qwerty"]

for word in wordlist:
    if hashlib.sha256(word.encode()).hexdigest() == target_hash:
        print("Password found:", word)
        break
else:
    print("Password not found")
