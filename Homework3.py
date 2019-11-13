# This program encrypt each character by adding 3 to the ascii value of each character in text.
# Example a -> d, b -> f, c -> g etc...


def encryption(text,shift):
    # create empty dictionary from a -> z and space
    t_table = dict.fromkeys('abcdefghijklmnopqrstuvwxyz ',None)
    for position in t_table:
        # convert character to ASCII, add + shift and convert back to character. Then store
        new_val = chr(ord(position) + int(shift))
        t_table[position] = new_val

    total = ''
    for elem in text:
        #  for each letter in text translate to the encrypted key
        total = total + str(t_table[elem])
    # print encrypted text
    print (total)

def decryption(text,shift):
    # create empty dictionary from a -> z and space
    t_table = dict.fromkeys('abcdefghijklmnopqrstuvwxyz ',None)
    for position in t_table:
        # convert character to ASCII, add + 3 and convert back to character. Then store
        new_val = chr(ord(position) - int(shift))
        t_table[position] = new_val

    total = ''
    for elem in text:
        #  for each letter in text translate to the encrypted key
        total = total + str(t_table[elem])
    # print encrypted text
    print (total)

mainoption = ''

while(mainoption != 'Q'):
    option = ''
    while ((option != 'E') and (option != 'D')):
        option = input("Enter your option encrypt (type 'E') or decrypt ('D'): ")

    text = input ('Enter your sentence').lower()

    shift = int(input("Enter the shift key for encryption"))


    if(option == 'E'):
        print (text)
        encryption(text, shift)
    elif(option == 'D'):
        decryption(text,shift)
    else:
        print("invalid option")

    mainoption = input('Press Q to quit or any character to start again')
