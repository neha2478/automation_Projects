from datetime import datetime
import requests
import csv
import bs4
from bs4 import BeautifulSoup

#writing some functionality to it .

# if __name__ == '__main__':
#     print('Hello World!')

#writing CSV - coma seperated values ...
#2> Read Product URL from CSV 
#here using Python Scripts we will read a CSV file and extract essential URLS from There.

# if __name__ == '__main__':
#     with open('amazon_products_urls.csv', newline='') as csvfile:
#         reader = csv.reader(csvfile, delimiter=',') #here dilemeter ='' is the sperrater that we want to 
#         for row in reader:
#             url = row[0] #we will extract the row and print the url
#             print(url)


# 3 :-Get HTML for URL :-
# for html for url we will create another function...
'''
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
REQUEST_HEADER= {
    'User_Agent' : USER_AGENT,
    'Accept-Lang': 'en-US, en;q= 0.5',
}

#the gent thai is trying to access the web browser is trying access ur
def get_page_html(url):
    res = requests.get(url = url, headers = REQUEST_HEADER) #headers is required to convert the data we got from request.
    return res.content #retuen the response content

def extract_product_info(url):
    product_info = {} #product will go to wrl and excat infor mation
    print(f'Scraping URL : {url}') #using format printing...
    html = get_page_html(url=url) #here in html we are passing function and keyword arg of url
    print(html)

if __name__ == '__main__':
    with open('amazon_product_url.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',') #using reader() and passing csvfile and passing delemeter = ','
        for row in reader:
            url = row[0]
            extract_product_info(url)#here we will print the function
'''

# 4 :- Extracting Products and Prices from HTML
#Here we will use the Beautifulsup aslo
#here we will use Beautifulsoup() object and pass html and lxml to it to parse it.
'''
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
REQUEST_HEADER= {
    'User_Agent' : USER_AGENT,
    'Accept-Lang': 'en-US, en;q= 0.5',
}

def get_page_html(url):
    res = requests.get(url = url, headers = REQUEST_HEADER) #headers is required to convert the data we got from request.
    return res.content #retuen the response content

def get_product_price(soup):
    # process to find file
    # using try and exception
    try:
        main_price_span = soup.find('span', attrs= {
            'class': 'a-price aok-align-center reinventPricePriceToPayMargin priceToPay'
        })
        price_span = main_price_span.findAll('span')#it will find all the spans.
        #we will iterate over price_sapn
        for span in price_span:
            # strip() - remove spaces, replace() - will replace $ with '', replace will replace ',' with '' space.
            price = span.text.strip().replace('$', '').replace(',', '')
            print(price)
    except:
        print("Price not found.")
        return None  # Optional, but prevents further errors

    # Another way of using try and except ....
    # main_price_span = soup.find('span', attrs= {
    #          'class': 'a-price aok-align-center reinventPricePriceToPayMargin priceToPay'
    # })
    # price_span = main_price_span.findAll('span')#it will find all the spans.
    # #we will iterate over price_sapn
    # for span in price_span:
    #     price = span.text.strip().replace('$', '').replace(',', '')
    #     # print(price)
    #     #here we will use the try and except or ...
    #     try:
    #         return float(price)
    #     except ValueError:
    #         print("Value obtained for thr orice couldn't be Parsed!!")
    #         exit() #using exit() method to come out of loop/func


def extract_product_info(url):
    product_info = {} #product will go to wrl and excat infor mation
    print(f'Scraping URL : {url}') #using format printing...
    html = get_page_html(url=url) #here in html we are passing function and keyword arg of url
    soup = bs4.BeautifulSoup(html, 'lxml')
    product_info['price'] = get_product_price(soup)#creating function for it in above
    print(product_info)

if __name__ == '__main__':
    with open('amazon_product_url.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',') #using reader() and passing csvfile and passing delemeter = ','
        for row in reader:
            url = row[0]
            print(extract_product_info(url))#here we will print the html product price...by calling func.
'''

# 5 :- Extracting Product Title from HTML 
'''
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
REQUECT_HEADER = {
    'User-Agent' : USER_AGENT,
    'Accept-Lang': 'en-US, en;q = 0.5'
}

def get_page_html(url):
    #res is response
    res =requests.get(url= url, headers=REQUECT_HEADER)
    return res.content

def get_product_price(soup):
    try:
        main_price_span = soup.find('span', attrs={
            'class': 'a-price aok-align-center reinventPricePriceToPayMargin priceToPay'
        })
        price_span = main_price_span.findAll('span')
        for span in price_span:
            price = span.text.strip().replace('$', '').replace(',', '')
            print(price)

    except ValueError:
        print("Not Found!!")
        return None

def  get_product_title(soup):
    #here we will use id in soup() attributes ....
    prod_title = soup.find('span', id ='productTitle')
    #here we will return product title's text so we are using text , strip() - to remove unnecessary spaces 
    return prod_title.text.strip() 

def extract_product_info(url):
    product_info = {} #Empty Dictionary
    print(f'Scraping URL: {url}') #print Url
    html = get_page_html(url=url) #function to get html , passing keyword argument
    soup = bs4.BeautifulSoup(html, 'lxml') #using bs4.Beautifulsoup(), passing html to parse using lxml
    product_info['price'] = get_product_price(soup)
    product_info['title'] = get_product_title(soup)
    return product_info


if __name__ == '__main__':
    with open('amazon_product_url.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            url = row[0]
            print(extract_product_info(url))
'''

# Task 6 :- Extracting Product Ratings from HTML
#here we will add a new function to the code...
#here we wrote a function named get_product_rating(soup), and added a line , product_info['rating'] = get_product_rating(soup)  to 
#function extract_product_info(url)
'''
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
REQUECT_HEADER = {
    'User-Agent' : USER_AGENT,
    'Accept-Lang': 'en-US, en;q = 0.5'
}

def get_page_html(url):
    #res is response
    res =requests.get(url= url, headers=REQUECT_HEADER)
    return res.content

def get_product_price(soup):
    try:
        main_price_span = soup.find('span', attrs={
            'class': 'a-price aok-align-center reinventPricePriceToPayMargin priceToPay'
        })
        price_span = main_price_span.findAll('span')
        for span in price_span:
            price = span.text.strip().replace('$', '').replace(',', '')
            print(price)

    except ValueError:
        print("Not Found!!")
        return None

def  get_product_title(soup):
    #here we will use id in soup() attributes ....
    prod_title = soup.find('span', id ='productTitle')
    #here we will return product title's text so we are using text , strip() - to remove unnecessary spaces 
    return prod_title.text.strip() 

def get_product_rating(soup):
    prod_rating_div = soup.find('div', attrs = {
        'id': 'averageCustomerReviews'
    })
    #to extract the 4.4 from the specific part...
    #this is inside a span tan in the div tag..
    prod_rating_section = prod_rating_div.find('i', attrs = {'class': 'a-icon-star'}) #star we are using random , max of them has a-icon
    #in the i tag only one span is there
    prod_rating_span = prod_rating_section.find('span')
    try:
        rating = prod_rating_span.text.split() #"4.4 out of 5 star" -> ["4.4", "out", "of", "5", "star"]
        print(rating)
        return float(rating[0])
    except ValueError:
        print("Value Obtained for Rating Could Not Be Parsed")
        exit()

def extract_product_info(url):
    product_info = {} #Empty Dictionary
    print(f'Scraping URL: {url}') #print Url
    html = get_page_html(url=url) #function to get html , passing keyword argument
    soup = bs4.BeautifulSoup(html, 'lxml') #using bs4.Beautifulsoup(), passing html to parse using lxml
    product_info['price'] = get_product_price(soup)
    product_info['title'] = get_product_title(soup)
    product_info['rating'] = get_product_rating(soup)   
    return product_info


if __name__ == '__main__':
    with open('amazon_product_url.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            url = row[0]
            print(extract_product_info(url))
'''

#Task -7 :- Extracting Product Details From HTML 
#here we will add another function named get_product_technical details
'''
#Updated code here
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
REQUECT_HEADER = {
    'User-Agent' : USER_AGENT,
    'Accept-Lang': 'en-US, en;q = 0.5'
}

def get_page_html(url):
    #res is response
    res =requests.get(url= url, headers=REQUECT_HEADER)
    return res.content

def get_product_price(soup):
    try:
        main_price_span = soup.find('span', attrs={
            'class': 'a-price aok-align-center reinventPricePriceToPayMargin priceToPay'
        })
        price_span = main_price_span.findAll('span')
        for span in price_span:
            price = span.text.strip().replace('$', '').replace(',', '')
            print(price)

    except ValueError:
        print("Not Found!!")
        return None

def  get_product_title(soup):
    #here we will use id in soup() attributes ....
    prod_title = soup.find('span', id ='productTitle')
    #here we will return product title's text so we are using text , strip() - to remove unnecessary spaces 
    return prod_title.text.strip() 

def get_product_rating(soup):
    prod_rating_div = soup.find('div', attrs = {
        'id': 'averageCustomerReviews'
    })
    #to extract the 4.4 from the specific part...
    #this is inside a span tan in the div tag..
    prod_rating_section = prod_rating_div.find('i', attrs = {'class': 'a-icon-star'}) #star we are using random , max of them has a-icon
    #in the i tag only one span is there
    prod_rating_span = prod_rating_section.find('span')
    try:
        rating = prod_rating_span.text.split() #"4.4 out of 5 star" -> ["4.4", "out", "of", "5", "star"]
        print(rating)
        return float(rating[0])
    except ValueError:
        print("Value Obtained for Rating Could Not Be Parsed")
        exit()
#Adding a new function to fetch Technical details ..
def get_product_technical_details(soup):
    details = {} #empty dictionary to put details in it.
    technical_deatails_section = soup.find('div', id="prodDetails")
    data_table = technical_deatails_section.findAll("table", class_="prodDetTable")#short cut of attrs={} in findAll is class_
    for table in data_table:
        table_rows  = table.findAll('tr')
        for row in table_rows:
            row_key = row.find('th').text.strip()
            row_value = row.find('td').text.strip().replace('\u200e', '') #his will replace the garbage value of u200e from the table data
            details[row_key] = row_value
    return details


def extract_product_info(url):
    product_info = {} #Empty Dictionary
    print(f'Scraping URL: {url}') #print Url
    html = get_page_html(url=url) #function to get html , passing keyword argument
    soup = bs4.BeautifulSoup(html, 'lxml') #using bs4.Beautifulsoup(), passing html to parse using lxml
    product_info['price'] = get_product_price(soup)
    product_info['title'] = get_product_title(soup)
    product_info['rating'] = get_product_rating(soup)   
    product_info.update(get_product_technical_details(soup))
    return product_info


if __name__ == '__main__':
    with open('amazon_product_url.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            url = row[0]
            print(extract_product_info(url))
'''

# Task - 8 Wrting data to CSV File 

#Updated code...
#here we will add a new values of product_data = [] empty list that will store the value.
#i will append this with the extract_product_info data into it ussing append()
#we will return product_info instead of printing ...
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
REQUECT_HEADER = {
    'User-Agent' : USER_AGENT,
    'Accept-Lang': 'en-US, en;q = 0.5'
}

def get_page_html(url):
    #res is response
    res =requests.get(url= url, headers=REQUECT_HEADER)
    return res.content

def get_product_price(soup):
    try:
        main_price_span = soup.find('span', attrs={
            'class': 'a-price aok-align-center reinventPricePriceToPayMargin priceToPay'
        })
        price_span = main_price_span.findAll('span')
        for span in price_span:
            price = span.text.strip().replace('$', '').replace(',', '')
            return price

    except ValueError:
        print("Not Found!!")
        return None

def  get_product_title(soup):
    #here we will use id in soup() attributes ....
    prod_title = soup.find('span', id ='productTitle')
    #here we will return product title's text so we are using text , strip() - to remove unnecessary spaces 
    return prod_title.text.strip() 

def get_product_rating(soup):
    prod_rating_div = soup.find('div', attrs = {
        'id': 'averageCustomerReviews'
    })
    #to extract the 4.4 from the specific part...
    #this is inside a span tan in the div tag..
    prod_rating_section = prod_rating_div.find('i', attrs = {'class': 'a-icon-star'}) #star we are using random , max of them has a-icon
    #in the i tag only one span is there
    prod_rating_span = prod_rating_section.find('span')
    try:
        rating = prod_rating_span.text.split() #"4.4 out of 5 star" -> ["4.4", "out", "of", "5", "star"]
        # print(rating)
        return float(rating[0])
    except ValueError:
        print("Value Obtained for Rating Could Not Be Parsed")
        exit()
#Adding a new function to fetch Technical details ..
def get_product_technical_details(soup):
    details = {} #empty dictionary to put details in it.
    technical_deatails_section = soup.find('div', id="prodDetails")
    data_table = technical_deatails_section.findAll("table", class_="prodDetTable")#short cut of attrs={} in findAll is class_
    for table in data_table:
        table_rows  = table.findAll('tr')
        for row in table_rows:
            row_key = row.find('th').text.strip()
            row_value = row.find('td').text.strip().replace('\u200e', '') #his will replace the garbage value of u200e from the table data
            details[row_key] = row_value
    return details


def extract_product_info(url):
    product_info = {} #Empty Dictionary
    print(f'Scraping URL: {url}') #print Url
    html = get_page_html(url=url) #function to get html , passing keyword argument
    soup = bs4.BeautifulSoup(html, 'lxml') #using bs4.Beautifulsoup(), passing html to parse using lxml
    product_info['price'] = get_product_price(soup)
    product_info['title'] = get_product_title(soup)
    product_info['rating'] = get_product_rating(soup)   
    product_info.update(get_product_technical_details(soup))
    return product_info


if __name__ == '__main__':
    products_data = [] #here is the empty List 
    with open('amazon_product_url.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            url = row[0]
            products_data.append(extract_product_info(url))


    output_file_name = 'output-{}.csv'.format(datetime.today().strftime("%m-%d-%Y"))
    #file is opened in write mode - 'w'
    with open(output_file_name, 'w') as outputfile:
        writer = csv.writer(outputfile) #here writer() will 
        writer.writerow(products_data[0].keys()) #index o , we will take keys from it using keys()
        for product in products_data:
            writer.writerow(product.values())

