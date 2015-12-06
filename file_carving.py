'''
File Carving Tool

Author: Meenal Jain

'''

import base64
import codecs
import binascii
import hashlib

# Function that extracts files based on header and footer magic numbers of different files

def extract(header, footer, hex_file, output):
    with open(hex_file, 'r') as f:
        data = f.read()
        header_index = data.find(header, 0)
        footer_index = data.find(footer, 0)
        if header_index >= 0 and footer_index >= header_index:
            print ("Found header at %s and footer at %s" \
                  % (header_index, footer_index))
            body = header + data[header_index + len(header): footer_index] + footer
            while body is not None:
                #Writing into output file
                f=open(output,"w")
                f.write(str(body))
                f.close()

                # Finding index of header and footer
                header_index = data.find(header,\
                                         footer_index + len(footer))
                footer_index = data.find(footer,\
                                         footer_index + len(footer) + len(header))
                if header_index >= 0 and footer_index >= header_index:
                    print ("Found header at %s and footer at %s" \
                           % (header_index, footer_index))

                    # header and footer values should also be appended to the extracted data
                    body = header + data[header_index + len(header): footer_index] + footer
                else:
                    body = None
                    
    #Returns extracted hex file as output
    return output

# Function that converts from hex file to ascii file and saves the final file with proper extension
def hex_to_ascii(output17,final_file,extension):
    with open(output17, 'rb') as f:
        content = f.read()
    output1 = binascii.unhexlify(content)
    f = open(final_file, 'wb')
    f.write(output1)
    f.close()
    
    # Finding md5 values of the extracted file
    m=hashlib.md5(open(final_file,'rb').read()).hexdigest()
    print("Hash Value of "+extension+" is "+ m)

def main():

    # Taking corrupted base64 decoded file from the user
    file_name=input("Enter the name of file you want to extract data from:  ")
    x=open(file_name, "rb")
    s=x.read()
    d=base64.standard_b64decode(s)
    hexlify=codecs.getencoder('hex')
    z=hexlify(d)[0]

    # Saving the decoded contents to a text file
    f=open("base64_decoded.txt","w")
    f.write(str(z))
    f.close()

    #Calling extract function
    a=extract("ffd8","ffd9","base64_decoded.txt","output1.txt")
    b=extract("255044462d312e", "2525454f46","base64_decoded.txt","output2.txt")
    c=extract("89504e470d0a1a0a","49454e44ae426082","base64_decoded.txt","output3.txt")
    d=extract("474946383961","00003b","base64_decoded.txt","output4.txt")
    e=extract("504b0304","504b0506","base64_decoded.txt","output5.txt")

    #a,b,c,d,e has extracted file in hex formats

    #Calling hex_to_ascii function and passing extension
    hex_to_ascii(a,"secret.jpeg","JPEG")
    hex_to_ascii(b,"Confidential.pdf","PDF")
    hex_to_ascii(c,"secure.png","PNG")
    hex_to_ascii(d,"clue.gif","GIF")
    hex_to_ascii(e,"hidden.docx","Docx")

main()
