# add your code here
alphabet = {
    'a':'f', 'b':'g', 'c':'h', 'd':'i', 'e':'j', 'f':'k', 'g':'l', 'h':'m', 'i':'n', 'j':'o',
    'k':'p', 'l':'q', 'm':'r', 'n':'s', 'o':'t', 'p':'u', 'q':'v', 'r':'w', 's':'x', 't':'y',
    'u':'z', 'v':'a', 'w':'b', 'x':'c', 'y':'d', 'z':'e'
    } 
message = input('Please enter a sentence: ')
message = message.lower()

cypher = 'The encrypted sentence is: '
for letter in message:

    if letter in alphabet:
        cypher += alphabet[letter] 
    elif letter not in alphabet:
        cypher += letter
    else:
        cypher += ' '

print(cypher)