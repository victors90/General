
# The purpose of this script is to parse the given string 
# consisting of dot and dash symbols and decode it 
# using the Russian Morse alphabet providing we don't know  
# the position of separating spaces between the letters.
# So the script lists all the possible variants.

import os
# Clearing the Screen
os.system('cls')

String_to_Decode = '...-.---.'

# str_forward   = "...-.---."
# str_backwards = ".---.-..."


print("Initial string: ", String_to_Decode)
print('Length = ', len(String_to_Decode))


Num_of_Spaces = len(String_to_Decode) - 1
SpacesPow = pow(2, Num_of_Spaces)
print('Variations = ', SpacesPow)
print ()


Modifier = "{0:0" + str(Num_of_Spaces) + "b}"
for i in range (SpacesPow):
    bin_num_str = str(Modifier.format(i))
    temp_str = String_to_Decode[0]


    for j in range (len(String_to_Decode)-1):
        spacer = '  '
        if bin_num_str[j] == '1':
            spacer = ''
        temp_str = temp_str + spacer + String_to_Decode[j+1]
    
    Letters = temp_str.split()
    
    Decypher = ""
    skip = 0
    for k in Letters:
        match k:
            case ".-":
                k = "А"
            case "-...":
                k = "Б"
            case ".--":
                k = "В"
            case "--.":
                k = "Г"
            case "-..":
                k = "Д"
            case ".":
                k = "Е"
            case "...-":
                k = "Ж"
            case "--..":
                k = "З"
            case "..":
                k = "И"
            case ".---":
                k = "Й"
            case "-.-":
                k = "К"
            case ".-..":
                k = "Л"
            case "--":
                k = "М"
            case "-.":
                k = "Н"
            case "---":
                k = "О"
            case ".--.":
                k = "П"
            case ".-.":
                k = "Р"
            case "...":
                k = "С"
            case "-":
                k = "Т"
            case "..-":
                k = "У"
            case "..-.":
                k = "Ф"
            case "....":
                k = "Х"
            case "-.-.":
                k = "Ц"
            case "---.":
                k = "Ч"
            case "----":
                k = "Ш"
            case "--.-":
                k = "Щ"
            case ".--.-.":
                k = "Ъ"
            case "-.--":
                k = "Ы"
            case "-..-":
                k = "Ь"
            case "...-...":
                k = "Э"
            case "..--":
                k = "Ю"
            case ".-.-":
                k = "Я"
            
            case _:
                skip = 1
                
        Decypher = Decypher + k
       
    if not skip:
        padding_size = Num_of_Spaces * 2 + Num_of_Spaces + 1
        t_format = "{0: <" + str (padding_size) + "s}"
        temp_str = t_format.format(temp_str)
     
        print(bin_num_str + "   " + temp_str + "    " + Decypher)


print ()
print ()
