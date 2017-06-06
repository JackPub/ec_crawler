import sys, getopt
from crawler_fetch import fetch_online,fetch_file
from crawler_parse import parse_yahoo_buy

def arg_reminder():
    print '-m <mode>'
    print '1: parse online context 2: parse file '
    print '-b <board>'
    print '1: billboard 2: others. To be implemented'
    print '-c <cate_file>'
    print 'categories file save path'
    print '-r <result_file>'
    print 'result file save path'
    print '-i <inpute_file>'
    print 'input file path for mode 2'
    
def main(argv):
    #argv process==================================================================================
    mode = ''
    board = ''
    cate_file=''
    result_file=''
    inpute_file=''
   
    try:
        opts, args = getopt.getopt(argv,"hm:b:c:r:i:",["mode=","board=","cate_file=","result_file=","inpute_file="])
    except getopt.GetoptError:
        print 'Input Error'
        arg_reminder()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            arg_reminder()
            sys.exit()
        elif opt in ("-m", "--mode"):
            mode = arg
        elif opt in ("-b", "--board"):
            board = arg
        elif opt in ("-c", "--cate_file"):
            cate_file = arg
        elif opt in ("-r", "--result_file"):
            result_file = arg 
        elif opt in ("-i", "--inpute_file"):
            inpute_file = arg 
    
    print 'Mode is "', mode         
    print 'Board is "', board
    print 'cate_file is "', cate_file
    print 'result_file is "', result_file
    print 'inpute_file is "', inpute_file
    print
    
    if(mode==''):
        mode='1'
    if(cate_file==''):
        cate_file='c_cate_file.txt'
    if(result_file==''):
        result_file='c_result_file.txt'
    if(inpute_file==''):
        inpute_file='c_fetch_result.txt'           
    
    pageSource = ''
    
    #main flow=====================================================================================
    
    if(mode=='1'):
        print 'mode 1 fetching source'
        pageSource = fetch_online()
        print 'mode 1 fetched source'
    elif(mode=='2'):
        if inpute_file=='':
            print 'Input file is not defined'
        else:
            print 'mode 2 fetching source'
            pageSource = fetch_file(inpute_file)
            print 'mode 2 fetched source'
    else:
        print 'To be implemented'
   
    if(pageSource !=''):
        print 'parsing'
        parse_yahoo_buy(pageSource, cate_file, result_file)
        print 'parsed'
    else:
        print 'no source'
        
if __name__ == "__main__":
   main(sys.argv[1:])