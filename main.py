from jsonmerger import *

def get_user_data():
    values = {}
    values[INPUT_DIR] = input("Enter the directory of the input file (with the '\\' or '/' appended depending on os.): ")
    values[INPUT_PREFIX] = input("Enter input file prefix: ")
    values[OUTPUT_PREFIX] = input("Enter output file prefix: ")
    values[FILE_SIZE] = input("Enter the maximum size of merge: ")
    return values



if __name__ == "__main__":

    input_args = cmd_args()
    if not input_args[constants.INTERACTIVE]:
    	input_args = get_user_data()
    
    merger = Merger(input_args[constants.INPUT_DIR],input_args[constants.INPUT_PREFIX],input_args[constants.OUTPUT_PREFIX],input_args[constants.FILE_SIZE])
    
    all_json = merger.read_files()
    
    compact_json = merger.merge(all_json)
    
    merger.save(compact_json)
