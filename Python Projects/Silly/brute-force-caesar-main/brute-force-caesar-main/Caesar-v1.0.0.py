alphabet= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(start_text):
    shift_amount=0
    for n in range(0,26):
        end_text=""
        for letter in start_text:
            if letter == ' ':
                end_text+= ' '
            else:
                position=alphabet.index(letter)
                new_position = position+shift_amount
                new_letter=alphabet[new_position]
                end_text+=alphabet[new_position]
        shift_amount+=1
        print(f"A decoded text is: {end_text}")

text=input("Type your message:\n").lower().replace("!", "").replace("?", "").replace(",", "").replace(".", "").replace(":", "").replace(";","")

caesar(start_text=text)
