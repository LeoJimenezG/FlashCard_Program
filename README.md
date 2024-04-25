# FlashCard_Program
Program that uses the flash card technique to practice learning a language

- Initialy, this program will use German as the language to learn. But you can change the language
- If you want to change the language to learn follow the next steps:
  - Open the directory called "data" and delete the csv files
  - Place your own csv file into the same directory
  - Open the file "main.py"
  - In the section called "GET THE DATA" replace the line 'original_data = pd.read_csv("data/Deu_Eng_words.csv")' to 'original_data = pd.read_csv("data/name_of_your_file.csv")'
  - Then, in the section called "VARIABLES" replace 'learning_lang = "Deutch"' to 'learning_lang = "your_language"'
- Once you execute the program, a random word will be displayed
- You will have 3 seconds to know its meaning before its right meaning is displayed
- After its meaning is displayed, you have to options:
  - If you press the "❌" button, it means you didn't know the right meaning
  - But, if you press the "✅" button, it means you did know the right meaning
- When you shutdown the program, all the words you didn't know will be saved into a file named "words_toLearn.csv" placed in the directory called "data"
- Then, when you run the program again, the words you did know will no longer have the chance to be displayed
