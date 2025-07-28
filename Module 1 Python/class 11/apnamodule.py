def word(txt,word):
    """
    [This function is made by me] 
    txt: accepts string values. 
    word: a word that is to be deleted. 
    return: returns the remaining text. 
    """
    if word in txt:
        return txt.replace(word, "").strip()
    else:
        return f"Word {word} not found in the Text"

def salam():
   return "Assalam u Alaikum"

def sum_list(lst):
    s = 0
    for a in lst:
        s+=a
    return s

def max_list(lst):
    max_num = lst[0]
    for n in lst:
        if n > max_num:
            max_num = n
    return max_num
    

def min_list(lst):
    min_num = lst[0]
    for n in lst:
        if n < min_num:
            min_num = n
    return min_num
    
def add_numbers(a,b,*nums):
    ts=0  
    for x in nums:
        ts+=x
    return s

def hey():
    return "Oye"