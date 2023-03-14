from collections import OrderedDict
import re


def createwordlist(filename:str) -> list[str]:
    '''This function creates a list of all the possible words in wordle'''
    file = open(filename, 'r')
    line = file.readline()
    word_list = []
    
    while line != '':
        stripped = line.strip()
        word_list.append(stripped)
        line = file.readline()
        
    return word_list







def get_remaining(color1: str, color2: str, color3: str, color4: str, color5: str, guess: 'str', rem_list: list[str]) -> list[str]:
    '''
    Takes the word that you guessed and the color of each letter as parameters. It will return the remaining words the answer could be.
    '''
    
    
    new_list = []
    new_list2 = []
    new_list3 = []
    new_list4 = []
    remaining_words = []
        
    
    letter1 = guess[0]
    letter2 = guess[1]
    letter3 = guess[2]
    letter4 = guess[3]
    letter5 = guess[4]
                 
            
    
    if color1 == 'x':
        for word in rem_list:
            if letter1 not in word:
                new_list.append(word)
                
    if color1 == 'y':
        for word in rem_list:
            if letter1 in word:
                if letter1 not in word[0]:
                    new_list.append(word)
                
                
    if color1 == 'g':
        for word in rem_list:
            if letter1 in word[0]:   
                new_list.append(word)
                
                

                
                
                
    if color2 == 'x':
        for word in new_list:
            if letter2 not in word:
                new_list2.append(word)
                            
    if color2 == 'y':
        for word in new_list:
            if letter2 in word:
                if letter2 not in word[1]:
                    new_list2.append(word)
                            
                            
    if color2 == 'g':
        for word in new_list:
            if letter2 in word[1]:   
                new_list2.append(word)
                
                
        
    
    
                
    if color3 == 'x':
        for word in new_list2:
            if letter3 not in word:
                new_list3.append(word)
                                        
    if color3 == 'y':
        for word in new_list2:
            if letter3 in word:
                if letter3 not in word[2]:
                    new_list3.append(word)
                                        
                                        
    if color3 == 'g':
        for word in new_list2:
            if letter3 in word[2]:   
                new_list3.append(word)
                
                


    if color4 == 'x':
        for word in new_list3:
            if letter4 not in word:
                new_list4.append(word)
                                                    
    if color4 == 'y':
        for word in new_list3:
            if letter4 in word:
                if letter4 not in word[3]:
                    new_list4.append(word)
                                                    
                                                    
    if color4 == 'g':
        for word in new_list3:
            if letter4 in word[3]:   
                new_list4.append(word)
                
                
                
                
                
    if color5 == 'x':
        for word in new_list4:
            if letter5 not in word:
                remaining_words.append(word)
                                                                
    if color5 == 'y':
        for word in new_list4:
            if letter5 in word:
                if letter5 not in word[4]:
                    remaining_words.append(word)
                                                                
    if color5 == 'g':
        for word in new_list4:
            if letter5 in word[4]:   
                remaining_words.append(word)    
                
                

                
                
                
    return remaining_words
                
    




def full_game():
    
    answerlist = createwordlist("AllWordleAnswers.txt")
    
    
    print("grey = x")
    print("yellow = y")
    print("green = g")
    guess = input("Enter first guess: ")
    color1 = input("Enter first color: ")
    color2 = input("Enter second color: ")
    color3 = input("Enter third color: ")
    color4 = input("Enter fourth color: ")
    color5 = input("Enter fifth color: ")
    
    rem_list1 = get_remaining(color1, color2, color3, color4, color5, guess, createwordlist("AllWordleAnswers.txt"))
    
    print("Remaining Answers:", rem_list1)
    
       
    guess = input("Enter second guess: ")
    color1 = input("Enter first color: ")
    color2 = input("Enter second color: ")
    color3 = input("Enter third color: ")
    color4 = input("Enter fourth color: ")
    color5 = input("Enter fifth color: ")
    
    rem_list2 = get_remaining(color1, color2, color3, color4, color5, guess, rem_list1)
    
    print("Remaining Answers:",get_remaining(color1, color2, color3, color4, color5, guess, rem_list1))
    
  
    guess = input("Enter third guess: ")
    color1 = input("Enter first color: ")
    color2 = input("Enter second color: ")
    color3 = input("Enter third color: ")
    color4 = input("Enter fourth color: ")
    color5 = input("Enter fifth color: ")
    
    rem_list3 = get_remaining(color1, color2, color3, color4, color5, guess, rem_list2)
    
    print("Remaining Answers:",get_remaining(color1, color2, color3, color4, color5, guess, rem_list2)) 
    
    
    guess = input("Enter fourth guess: ")
    color1 = input("Enter first color: ")
    color2 = input("Enter second color: ")
    color3 = input("Enter third color: ")
    color4 = input("Enter fourth color: ")
    color5 = input("Enter fifth color: ")
    
    rem_list4 = get_remaining(color1, color2, color3, color4, color5, guess, rem_list3)
    
    print("Remaining Answers:",get_remaining(color1, color2, color3, color4, color5, guess, rem_list3))
    
      
    guess = input("Enter fifth guess: ")
    color1 = input("Enter first color: ")
    color2 = input("Enter second color: ")
    color3 = input("Enter third color: ")
    color4 = input("Enter fourth color: ")
    color5 = input("Enter fifth color: ")
    
    rem_list5 = get_remaining(color1, color2, color3, color4, color5, guess, rem_list4)
    
    print("Remaining Answers:",get_remaining(color1, color2, color3, color4, color5, guess, rem_list4))    
    
    
    

    






    
def count_letters(all_words: list[str]) -> dict[int:int]:
    letter_dict = {}
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    one_string = "".join(all_words)
    
    for letter in alphabet:
        letter_dict[letter] = one_string.count(letter)
        
    
    return letter_dict


def get_weights(rem_list: list[str]) -> list[str]:
    
    unsorted_dict = {}
    final_list = []
    weight_dict = count_letters(rem_list)
        
    for word in rem_list:
        total = weight_dict[word[0]] + weight_dict[word[1]] + weight_dict[word[2]] + weight_dict[word[3]] + weight_dict[word[4]]
        unsorted_dict[word] = total
        
    sorted_list = sorted(unsorted_dict.items(), key=lambda x: x[1], reverse=True)
    
    for tup in sorted_list:
        final_list.append(tup[0])
        
    return final_list
    
    
     
    
    
    
createwordlist("AllWordleAnswers.txt")

 
get_weights(createwordlist("AllWordleAnswers.txt"))














