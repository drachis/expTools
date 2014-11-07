import string
import random

def generatePassword(upper=0, lower=0, digits=0, special=0):
    char_set = random.sample(string.ascii_uppercase, upper)+\
        random.sample(string.ascii_lowercase, lower)+\
        random.sample(string.digits, digits)+\
        random.sample(string.punctuation, special)
    pword = ''
    while len(char_set)>0:
        idx = random.randint(0,len(char_set))
        pword += char_set.pop(idx-1)
    return pword

def randInt(maximum):
    return random.randint(0,maximum)
    
if __name__ == "__main__":
    pword = generatePassword(4,2,2,2)
    print pword

