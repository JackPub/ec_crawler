# encoding: utf-8
import codecs
from bs4 import BeautifulSoup

#==================================================================================================
def parse_yahoo_buy(ipageSource, cate_file, result_file):

    #remove <!-- & --> to get item info of comment paragraph 
    srcTmp = ipageSource.replace("<!--", "")
    pageSource = srcTmp.replace("-->", "")
    
    #use BeautifulSoup to parse source page
    soup = BeautifulSoup(pageSource, 'html.parser')

    #==============================================================================================
    #get categories' mapping and save to cate_file
    f_cate = codecs.open(cate_file,'w', "utf-8", buffering=-1)
    f_cate.write('hpp' + ',' + 'cate_name' + '\n')
    #build dictory of product categories
    dict_categories = {}
    for link in soup.find_all('li'):
        if link.get('hpp') and link.get('hpp').find('chart_sub')==0:
            f_cate.write('"' + link.get('hpp') + '","' + link.text.strip() + '"\n')
            dict_categories[link.get('hpp')]=link.text
    f_cate.close()
    
    #==============================================================================================
    #get item info and save to result_file
    f_result = codecs.open(result_file,'w', "utf-8", buffering=-1)
    f_result.write('item_hpp' + ',' + 'cate' + ',' + 'cate_name' + ',' + 'item_name' + ',' + 'item_price' + '\n')
    for link in soup.find_all('a'):
        #print type(link)
        if link.get('hpp') and link.get('hpp').find('chart_sub')==0:
            item_hpp = link.get('hpp')
            cate = item_hpp[:len('chart_sub')+item_hpp[len('chart_sub'):].find('_')] #extract cate of item
            cate_name = dict_categories[cate] #lookup by cate that we can get cate_name
            print(item_hpp)
            print(cate)
            print(dict_categories[cate])

            if link.get('hpp') and link.get('hpp').find('item1')>=0: #for rank1 parsing
                item_name = link.contents[5].text
                item_price = link.contents[7].text
            else: #for rank2-5 parsing
                item_name = link.contents[3].contents[3].text
                item_price = link.contents[3].contents[5].text
            print(item_name)
            print(item_price)
            print('=========================')
        
            f_result.write('"' + item_hpp + '","' + cate + '","' + cate_name + '","' + item_name + '","' + item_price + '"\n')
    f_result.close()
        
#==================================================================================================
