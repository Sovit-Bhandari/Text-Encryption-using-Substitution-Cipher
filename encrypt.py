'''Name = Sovit Bhandari
U-number= U83561265
Brief discription = This code is a Python program that performs text encryption using a simple character substitution cipher'''

def encrypt_text(contents, encrypt_dict):
    encrypted_contents = ""
    for char in contents:
        if char in encrypt_dict:
            encrypted_contents += encrypt_dict[char]
        else:
            encrypted_contents += char
    return encrypted_contents

def main():
    # Prompt the user for the name of a text file
    input_file_name = input("Please enter the name of a text file: ")
    
    # Read the contents of the file
    with open(f'{input_file_name}.txt', 'r') as file:
        contents = file.read()
    
    # Prompt the user for the name of the output text file
    output_file_name = input("Please enter the name of the output text file: ")
    
    # Encrypt the contents using the provided dictionary
    Encrypt_Code = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
    'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
    'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
    'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
    'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
    'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
    'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
    'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
    'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
    '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
    '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
    '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
    ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
    "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
    '{':'[','[':'{','}':']',']':'}'}
    
    encrypted_contents = encrypt_text(contents, Encrypt_Code)
    
    # Write the encrypted contents to the output file
    with open(output_file_name, 'w') as file:
        file.write(encrypted_contents)

if __name__ == "__main__":
    main()

