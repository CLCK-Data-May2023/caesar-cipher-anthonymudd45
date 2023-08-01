# add your code here
alphabet = "abcdefghijklmnopqrstuvwxyz"
cypher = "fghijklmnopqrstuvwxyzabcde"
encryption = {}
i = 0
for letter in alphabet:
    encryption[letter] = cypher[i]
    i += 1

message = str(input("Please enter a sentence:")).lower()

output = [encryption.get(letter, letter) for letter in message]
print("".join(output))
