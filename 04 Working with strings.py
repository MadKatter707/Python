print("Giraffe Academy")
print("Giraffe\nAcademy")
print("Giraffe \"Academy\"")
#escape character "\" whatever comes after it is printed out
#as a character without function
#typicaly \n is new line
phrase = "Choi San is my husbando"
print(phrase)
stream = "inception"
print(stream)
#using variables to print
print("stream " + stream + " BISHES")
print(phrase + " forever")
#concatenation

#####functions#####
print(phrase.lower()) #all letters low
print(phrase.capitalize()) #first letter only
sentences = "first one. second one."
print(sentences.capitalize()) #only first one xD
print(phrase.upper()) #all caps
print(phrase.isupper()) #returns true or false
print(phrase.islower())
print(phrase.upper().isupper())
print(len(phrase)) #length of string
#one letter by one
print(phrase[0])
print(phrase[1])
print(phrase[2])
print(phrase[3])
print(phrase[4])
print(phrase[5])
print(phrase[6])
print(phrase[7])
print(phrase[8])
print(phrase[9])
print(phrase[10])
print(phrase[11])
print(phrase[12])
print(phrase[13])
print(phrase[14])
print(phrase[15])
print(phrase[16])
print(phrase[17])
print(phrase[18])
print(phrase[19])
print(phrase[20])
print(phrase[21])
print(phrase[22])
#index function
print(phrase.index("S"))
print(phrase.index("a"))
print(phrase.index("n"))
print(phrase.index("San"))
#print(phrase.index("e"))
#Traceback (most recent call last):
 # File "C:\Users\youwish;p\PycharmProjects\Giraffe\04 Working with strings.py", line 55, in <module>
 #   print(phrase.index("e"))
#ValueError: substring not found
print(phrase.replace("husbando" , "love"))
