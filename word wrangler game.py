"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    result=[]
    copy_list=list(list1)
    while len(copy_list)!=0:
        element=copy_list[0]
        if element  not in result:
            result.append(element)
        copy_list.pop(0)
    return result

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    result=[]
    if len(list1)>=len(list2):
        itr_list=list(list2)
        copy_list=list(list1)
    else:
        itr_list=list(list1)
        copy_list=list(list2)
    while len(itr_list)!=0:
        element=itr_list[0]
        if element in copy_list and element not in result:
            result.append(element)
        itr_list.pop(0)
    return result

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """
    copy_list1=list(list1)
    copy_list2=list(list2)
    answer=[]
    while len(copy_list1)!=0 and len(copy_list2)!=0:
        if copy_list1[0]>copy_list2[0]:
            answer.append(copy_list2[0])
            copy_list2.pop(0)
        else:
            answer.append(copy_list1[0])
            copy_list1.pop(0)
    if len(copy_list1)!=0:
        answer.extend(copy_list1)
    else:
        answer.extend(copy_list2)
    return answer
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    # this is the base condition
    sorted_list=[]
    if len(list1)<2:
        return list1
    else:
        divide_point=len(list1)//2
        left_list=list(list1[:divide_point])
        right_list=list(list1[divide_point:])
        sorted_list=merge(merge_sort(left_list),merge_sort(right_list))
    return sorted_list

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if word=="":
        return [""]
    else:
        first=word[0]
        rest=word[1:]
        rest_strings=gen_all_strings(rest)
        all_strings=[]
        for string in rest_strings:
            for dummy_i in range(len(string)+1):
                all_strings.append(string[:dummy_i]+first+string[dummy_i:])
    return all_strings+rest_strings

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    url = codeskulptor.file2url(filename)
    netfile = urllib2.urlopen(url)
    words_file = netfile.readlines()
    
    words = [word[:-2] for word in words_file]
    
    return words

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)
# Uncomment when you are ready to try the game
#run()

    
    