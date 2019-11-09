from collections import Counter
import json

class Parser:
    
    def __init__(self,input_dir,input_prefix,output_prefix,max_file_size):
        self.input_dir = input_dir
        self.input_prefix = input_prefix
        self.output_prefix =  output_prefix
        self.max_file_size = max_file_size
    
    def read_files(self):
        if self.input_dir == '.':
            self.input_dir = ''
        counter = 1
        result_jsons = []
        while True:
            try:
                json_file = open(self.input_dir + self.input_prefix + str(counter) + ".json", "r") # reading the file in the given directory
                result_jsons.append(json.load(json_file))
                json_file.close()
            except FileNotFoundError: # all files under the input basename read
                print("inputs recived") 
                break
            counter += 1 # to move to the next input file
        return result_jsons

    def merge(self,jsons):
        result = {}
        for json in jsons:
            for key in json:              
                if key in result: # has key then append lists to existing data
                    result[key].extend(json[key])
                else:
                    result[key] = json[key]
        return result
    
    def save(self,json_data):
        try:
            with open(self.input_dir + self.output_prefix + '1' + '.json',"w") as f: # storing as utf-8 to allow non-english char
                f.write(json.dumps(json_data,ensure_ascii=False))
        except Exception as e:
            print(e)
            print("File write error")
            
            
        

    
