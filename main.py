#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


#### Get names of the guests
with open("Input/Names/invited_names.txt") as name_file:
    names = [name.strip() for name in name_file.readlines()]


#### Get the starting letter
with open("Input/Letters/starting_letter.txt") as starting_letter_file:
    starting_letter = starting_letter_file.read()


for name in names:
    with open(f"Output/ReadyToSend/letter_for_{name}", mode="w") as letter:
        letter.write(starting_letter.replace("[name]", name))
