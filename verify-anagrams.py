def verify_anagrams(first_word, second_word):
    
    first = []
    second = []
    for x in first_word.replace(" ", ""):
        first.append(x.lower())
        
    for x in second_word.replace(" ", ""):
        second.append(x.lower())

    if len(first) != len(second):
        return False
        
        
    first_copy = first[:]
    second_copy = second[:]

    for x,y in zip(first_copy, second_copy):
        if x in second and y in first:
            try:
                first.remove(y)
                second.remove(x)
#                print('ok')
            except ValueError: return False
        else:
#            print('whut')
            return False
#    print('hmm')
    return True

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"