# This is a python script that merges multiple json files and keeps writing as output files in the same folder as the input.

- First the number of json files are read in the directory.

- Then the key for the json file is noted. 
- Then we iterate through each json file in the directory and then for each time we store the read JSON in a dictionary and simply dump the variable containing the dictionary into a new output json file.

- Thus, the first output file has contents of file1,file2 then the next output file has file1,file2,file3... and it goes on up until all the files in the input directory are read.

- The write operation happens iff the file size is less than the input max size.

# Code Complexity

- If the number of input files in the given input directory  is 'n' and say if there are a maximum of 'm' objects in an input file, then the code runs in: 
# O(n * m)
