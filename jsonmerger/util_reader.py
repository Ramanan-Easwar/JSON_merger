import argparse

def cmd_args():
    parser = argparse.ArgumentParser()
    # parser.add_argument('-i','--interactive', help='intercative input',default=False)
    parser.add_argument('-d','--dir', help='directory where exist',default='.')
    parser.add_argument('-p','--prefix', help='prefix input file name',default='data')
    parser.add_argument('-o','--oprefix', help='prefix output file name',default='merge')
    parser.add_argument('--max-size', help='max file size',default=1)
    args = parser.parse_args()
    return vars(args)

def get_user_data():
    print("get_user_data from stdin TODO")
    # ans[constants.INPUT_DIR] = args.dir
    # ans[constants.INPUT_PREFIX] = args.prefix
    # ans[constants.OUTPUT_PREFIX] = args.oprefix
    # return vars(ans)

