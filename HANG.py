import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):

    i=len(secret_word)
    for x in letters_guessed:
       for y in secret_word:
           if x is y:
               i-=1

    if i is 0:
        return True
    else:
        return False
    #pass



def get_guessed_word(secret_word, letters_guessed):
    s='_ '*len(secret_word)
    c=-1
    for c in letters_guessed:
        i=0
        while i<len(secret_word):
            ch=secret_word[i]
            if ch is c:
                c=1
                s = s[:2*i]+ secret_word[i]+ s[2*i+1:len(s)]
            i+=1
    s=" ".join([letter if letter in letters_guessed else "_" for letter in secret_word])
    st1="Good Guess: "
    st2="Sorry :( That letter is not in my word:  "
    if c==1:
        s=st1+s
    else:
        s=st2+s
    print(s)
    return c
    
    #pass



def get_available_letters(letters_guessed):
    st=string.ascii_lowercase
    s=sorted(letters_guessed)
    i=0
    j=0
    while i<len(s):
        ch = s[i]
        while j<len(st):
            c=st[j]
            if ch == c:
                st = st[:j]+st[j+1:len(st)]
                break
            j+=1
        i+=1
    return st
    #return "".join([letter if letter not in letters_guessed else "" for letter in string.ascii_lowercase])
    
    

def hangman(secret_word):

    letters_guessed=[]
    print('Welcome to the game HANGMAN!!!')
    print('I am thinking of a word that is',len(secret_word),'letters long.')
    print('\n****************************************\n')
    i=6
    warn=1
    while i>0 and (is_word_guessed(secret_word,letters_guessed) is False):
        #i=6-len(letters_guessed)
        print('You have', i, 'guesses left')
        print('Available letters:',get_available_letters(letters_guessed))
        item=input("Please guess a letter: ")
        if item.isalpha() is False and warn<4:
            print('Warning',warn,'!!!!!!','Only uppercase/Lowercase alphabets are allowed!!')
            print(3-warn, 'Warning(s) left')
            warn+=1
        elif item in letters_guessed and warn<4:
            print('Warning',warn,'!!!!!!','You aleady guessed this letter')
            print(3-warn, 'Warning(s) left')
            warn+=1
        else:
            item.lower()
            letters_guessed.append(item)
            z=get_guessed_word(secret_word,letters_guessed)
            if z!=1:
                i-=1
        print('\n**************************************\n')
        
    if(i>0):
        print('Congratulations!!! You won the game!!')
    else:
        print('Sorry :( You ran out of guesses. The word was',secret_word)

if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman(secret_word)
