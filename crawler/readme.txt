0. Enviroment
    0.1 Python 2.7+

1. Prerequisites & dependencies  
    1.1 BeautifulSoup 4.6.0+
    1.2 Selenium 3.4.3+
    1.3 Chrome driver 2.29+

2 Design
    2.1 use chrome driver to simulate user's browsing behavior (including javascript rendering)
    2.2 save web source page to temp file
    2.3 use BeautifulSoup to parse meaningful information, like category name, item name or item price.
    2.4 save info into file. Also we can save info into database, that will be more conveient.
    
    
3. Limitations
    In this case we can't fetch one category billboard directly.
    The billboard show to customer is based on yahoo's algorithm.
    Every time we excute program will get different categories' billboard.
    If we want to fetch one category billboard directly, we may try to fetch from https://tw.buy.yahoo.com/catalog/ajax/recmdHotNew
    