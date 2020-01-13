from collections import OrderedDict


def normalize(word,n):

    diff = n - len(word)

    return ['#'] * diff + word

def get_letters(words):

    letters = OrderedDict()

    for i in reversed(range(len(words[-1]))):
        for word in words:
            c = word[i]
            if c not in letters:
                letters[c] = None

    return letters


def is_valid(words,letters):

    w1,w2,w3 = words
    carry = 0
    n = len(words[-1])

    for i in reversed(range(n)):
        if any(letters[word[i]] is None for word in words):
            return True
        elif letters[w1[i]] + letters[w2[i]] + carry == letters[w3[i]]:
            carry = 0
        elif letters[w1[i]] + letters[w2[i]] + carry == 10 + letters[we[i]]:
            carry = 1
        else:
            return False

    return True

def solver(words,letters,unassigned,index,numbers):

    if index == unassigned:
        print(letters)
        return

    letter = unassigned[index]
    
    for number in numbers:
        letters[letter] = number
        numbers.remove(number)
        if is_valid(words,letters):
            pass

        numbers.add(number)
        letters[letter] = None

def solve(words):


    n = len(words[-1])

    words[0] = normalize(words[0],n)
    words[1] = normalize(words[1],n)


    letters = get_letters(words)
    letters['#'] = 0
    unassigned = [letter for letter in letters if letter != '#']
    index = 0
    numbers = set(range(0,10))
    solver(words,letters,unassigned,index)


