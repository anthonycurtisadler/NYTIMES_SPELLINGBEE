import os


about = """

             SPELLING BEE SOLVER 
         by Anthony Curtis Adler 2019

    
     
     SPELLING BEE SOLVER FINDS SOLUTIONS
          TO THE 'SPELLING BEE'
     PUZZLE in THE NEW YORK TIMES.

          I'VE INCLUDED words.txt from:
      https://github.com/dwyl/english-words.

     THIS, HOWEVER, INCLUDES MANY
     WORDS THAT WILL NOT BE ACCEPTED
     BY THE NEW TIMES PUZZLE ENGINE.
     
     OTHER WORDS CAN BE USED. \n\n\n"""

print(about)

filename = 'words.txt'
# GET TEXT FILE 
while True:
     print('GETTING TEXT FILE!')
     try:
          textfile = open(filename,'r', encoding='utf-8')
          textfile=textfile.read()
          print(filename+' OPENED! \n')
          break
     except:
          print(textfile+' NOT FOUND\n')
          print('ENTER NEW WORD FILE!')
          filename= input('textfile')


# FIND THE CHARACTER DIVIDING THE WORDS
for x in textfile:
     if x not in 'abcdefghijklomnopqrstuvwxyz0123456789':
          split = x
          break

words = textfile.split(x)
print('NUMBER OF WORDS: '+str(len(words)))

print()

found_words = []
while True:
     central_letters = input('WHAT IS THE CENTRAL LETTER?')
     print()
     surrounding_letters = input('WHAT ARE THE SURROUNDING LETTERS?')
     print()
     if central_letters.isalpha() and surrounding_letters.isalpha():
           try:
                min_length = int(input('MINIMUM LENGTH?'))
                all_letters = central_letters+surrounding_letters
                break
           except:
                print('MUST BE INTEGER!')
     
     print('YOU MUST ENTER LETTER(S)!')
     


for word in words:
      central_letters_found = True
      for letter in central_letters:
           if letter not in word:
                central_letters_found = False
      no_other_letters = True
      for letter in word:
           if letter not in all_letters:
                no_other_letters = False
      if central_letters_found and no_other_letters and len(word)>=min_length:
           found_words.append(word)


print('\n'.join(found_words))
input('')
      

     
                
                



          
          


          
               
          
          





          
          


