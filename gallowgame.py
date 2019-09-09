password="gallow"
word = input("podaj jedno słowo do odgadnięcia: ")
space=''
e=0
for i in range(len(word)):
    word=list(word)
    word.insert(0+e,' ')
    e=e+2
    space=space+' _'
space=list(space)
word=''.join(word)
letter=''
guess=''
n=1
loser=False
while guess!=word:
    letter=input("Oto słowo do odgadnięcia:"+''.join(space)+" podaj literę: ")
    if letter in list(word):
        foo = ([pos for pos, char in enumerate(word) if char == letter]) #znajduje tablice indeksów liter w słowie word
        y=0
        for x in foo:
            space[foo[y]] = letter
            y=y+1
            space = ''.join(space)
            guess = space
            space = list(space)
    else:
        password=list(password)
        z=password[0:n]
        print(''.join(z))
        n=n+1
        if n-1==len("gallow"):
            print("przegrałeś")
            loser=True
            break
if loser==False:
    print("Wygrałeś! Słowo to: "+word)




