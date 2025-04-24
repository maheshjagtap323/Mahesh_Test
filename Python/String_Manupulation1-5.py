#1-sum of Two vaulues should be 9

list_data = [2,5,7,11,15,7]
target = 9
def two_sum(list_data,target):
    for i in range(len(list_data)):
        for j in range(i+1, len(list_data)):
            if list_data[j]==target- list_data[i]:
                return [i,j]

print(two_sum(list_data,target))

#########################################
##2- unique count after removing duplicates

list_data = [0,0,1,1,1,2,2,3,3,4]
def remove_duplicates(list_data):
    j=0
    for i in range(1,len(list_data)):
        if list_data[i]==list_data[i -1]:
            j +=1  
    return j
            
print(remove_duplicates(list_data))


##other way

list_data = [0,0,1,1,1,2,2,3,3,4]
def remove_duplicates(list_data):
    unique=list(set(list_data))
    unique=len(unique)
    return unique
            
print(remove_duplicates(list_data))

#########################################
##3- remove provided value

list_data = [0,0,1,1,1,2,2,3,3,4]
value=1
def remove_value(list_data,value):
    final_list=[]
    for i in range(len(list_data)):
        if list_data[i]!=value:
            final_list.append(list_data[i])
    return final_list

print (remove_value(list_data,value))


#########################################
##4- Check if All Characters Have Equal Number of Occurrences

from collections import Counter  

String_data='abdabd'
def Char_check(String_data):
    Dict_Count=Counter(String_data)
    print(Dict_Count)
    dict_set=set(Dict_Count.values())
    print(dict_set)
    
    return len(dict_set)==1 
print (Char_check(String_data))

##same will work for list of string as well
from collections import Counter
String_data=['abdabd','abdabd','M','M']

def Char_check(String_data):
    Dict_Count=Counter(String_data)
    print(Dict_Count)
    dict_set=set(Dict_Count.values())
    print(dict_set)
     
    return len(dict_set)==1 
print (Char_check(String_data))
    
#########################################
##5- Find the Index of the First Occurrence in a String 
haystack = "1sadbutsad" 
needle = "sad"
def string_check(haystack,needle):
    return haystack.find(needle)
print(string_check(haystack,needle)) 

#### palledrome

def is_palindrome(s):
    return s == s[::-1]  # Reverse and compare

# Test cases
print(is_palindrome("hello"))  # False


        

            
        