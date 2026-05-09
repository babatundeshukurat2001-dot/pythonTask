1. #ask user for one character and store as letter
2. #convert letter to lowercase
3. #if length of letter is not 1 OR letter is not a letter THEN
      # print "Invalid input"
   #elif letter is a, e, i, o, or u THEN
       #print "Vowel"
   #else
       #print "Consonant"



letter = input("Enter one letter: ").lower()

if len(letter) != 1 or not letter.isalpha():
    print("Invalid input")
elif letter in "aeiou":
    print("Vowel")
else:
    print("Consonant")
