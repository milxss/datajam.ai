
import re 

  
# Declare a dictionary  

dict = {}  

  
# Method to check whether the word  
# exists in dictionary or not  

def uniqueWord(Word):  

  

    if Word in dict:  

  

        # If the word exists in dictionary then  

        # simply increase its count  

        dict[words] += 1

  

    else:  

  

        # If the word does not exists in  

        # dictionary update the dictionary 

        # and make its count 1  

        dict.update({words: 1})  

  
# Driver code 

if __name__ == '__main__':  


    string = "one, two, three, one, four, five, Kamila , flower, cactis, flower"

      

    # re.split() method is used to split 

    # all the words in a string seperated 

    # by non-alphanumeric characters (\W) 

    ListOfWords = re.split("[\W]+", string) 

  

    # Extract each word from ListOfWords  

    # and pass it to the method uniqueWord()  

    for words in ListOfWords:  

        uniqueWord(words)  

  

    # Iterate over dictionary if the value 

    # of the key is 1, then print the element  

    for elements in dict:  

        if dict[elements] == 1:  

            print(elements)
