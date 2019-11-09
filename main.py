from jsonmerger import *



if __name__ == "__main__":
    #write verbose comments in this file

    input_args = cmd_args()
    # if input_args[constants.INTERACTIVE]: # interactive get data from stdin
    #     input_args = get_user_data()
    
    parser = Parser(input_args[constants.INPUT_DIR],input_args[constants.INPUT_PREFIX],input_args[constants.OUTPUT_PREFIX],input_args[constants.FILE_SIZE])
    
    all_json = parser.read_files()
    
    compact_json = parser.merge(all_json)
    
    parser.save(compact_json)