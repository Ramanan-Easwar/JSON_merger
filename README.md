# JSON Merger 
 A python script that merges any number of json files with same basename and writes into a new json file.
 
 The merging of files happens until the size of the file exceeds the given maximum filesize.
 
 The files are encoded with UTF-8 to support other languages. 

# Running on command-line
 python main.py -i True -d [directory path] -p [input basename] -o [output basename] -m [max filesize in bytes]
 
 python main.py -h *(to get the command-line flags for more details)*

# Using stdin

 Simply run the main.py file and it will prompt you to enter the details (make sure to enter the correct path including starting and the ending '/' or '\\' depending on your os)
 
 _example directory:_
      /home/user1/Documents/files/
      
 

# Code Complexity

- If the number of input files in the given input directory  is 'n', then it runs in:  O(n)


