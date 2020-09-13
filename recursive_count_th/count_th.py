'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    if len(word) == 0:
        return 0
    if isinstance(word, str) != True:
        return None
    if word.find('th') == -1:
        return 0
    index = word.find('th')    
    return 1 + count_th(word[index+2:])
        
    
