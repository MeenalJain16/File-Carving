# File Carving
Tool that can be used to extract hidden files from base64 encoded corrupted file.

To run the program, follow these steps:
        Open file_carving.py and press F5. 
        The program will ask for the corrupted input file.
        Enter 'corrupted.docx'.
        You will get the header and footer location and the hash values of the extracted files.
        The extracted files will be created in the same folder where file_carving.py exists.


Procedure to extract the files:
  1. Decoded the source file ‘corrupted.docx’.
  2. The resulted file was in ascii.
  3. Converted from ascii to hexadecimal file
  4. Extracted the data based on header and footer magic numbers from the hex file.
  5. Converted the extracted files into ascii
  6. The ascii files are the extracted files with proper extension.
