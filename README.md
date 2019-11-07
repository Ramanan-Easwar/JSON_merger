# JSON Merger 
-This is a python script that merges multiple json files and keeps writing them to output files in the same directory.

- First the number of json files in the directory are read and the count is stored.

- Then the key for the json file is noted by converting the json to a string object using json.dumps() and getting the common JSON object name for the json files. 
- Then we iterate through each JSON file in the directory and then for each time we store the JSON that was read in a dictionary and simply dump the dictionary variable into a new output JSON file i.e. writing it to a JSON file.

- Thus, the first output file has contents of file1,file2 then the next output file has file1,file2,file3... and it goes on up until all the files in the input directory are read.

- The write operation happens iff the file size is less than the input max size.

- NOTE: The max_size check happens as soon as the ouput json is written. If the file size exceeds the given size, the json file is deleted as soon as it is written.

# Code Complexity

- If the number of input files in the given input directory  is 'n' and say if there are a maximum of 'm' objects in an input file, then the code runs in: 
# O(n * m)


