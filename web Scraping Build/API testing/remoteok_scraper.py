#things that we need to install in terminal :-
'''
- python -m venv venv
- Venv/Scripts/activate
- pip install requests
- pip install xlwt  - plugin

'''


import requests
import xlwt # Allows to work with xl work sheets
from xlwt import Workbook
import smtplib # includes in the standard python installation
from  os.path import basename 
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

#This is to check everything is working successfully or not
'''
if __name__ == '__main__':
    # print("Hello World!!") # succesfully working
'''

#Reteriving Data from API
''' 
#  We will try to get some responce from remort ok API using python Script
#URL - is store in a variable which is globally accessable

#This are Global Variables....

BASE_URL = 'https://remoteok.com/api/'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
REQUEST_HEADER = {
    'User-Agent':USER_AGENT,
    'Accept-Lan': 'en-US, en;q=0.5',
}

def get_job_postings():
    #res - request variable , using get() to fetch URL
    res = requests.get(url=BASE_URL, headers=REQUEST_HEADER )
    return res.json() #it will retuen the responce in the json format


if __name__ == '__main__':
    json = get_job_postings()[1] #[1] it will return the first index values in jason format  
    print(json)
'''

# API Scraping Exporting Data To Spreadsheet :-
'''
BASE_URL = 'https://remoteok.com/api/'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
REQUEST_HEADER = {
    'User-Agent':USER_AGENT,
    'Accept-Lan': 'en-US, en;q=0.5',
}

def get_job_postings():
    #res - request variable , using get() to fetch URL
    res = requests.get(url=BASE_URL, headers=REQUEST_HEADER )
    return res.json() #it will retuen the responce in the json format

def output_job_to_xls(data):
    wb = Workbook() #Workbook - is an Object Instance
    job_sheet = wb.add_sheet('Jobs') #parameter that we have passed into the sheet is name of Sheet
    #we need to add the Headers value for what the data will be
    headers = list(data[0].keys()) #header will be be the data of the list , keys()
    for i in range(0, len(headers)):
        job_sheet.write(0, i, headers[i]) #here in write(row, column, value)

    #Adding remaing data ..
    for i in range(0, len(data)):
        job = data[i] #here data will be store in job 
        values = list(job.values()) #same we we collected values in list like headers 
        for x in range(0, len(values)):
            job_sheet.write(i+1, x, values[x]) #here i+1 from next line it will store data, values will be store using write()
    wb.save('remote_jobs.xls')

if __name__ == '__main__':
    json = get_job_postings()[1:] #[1] it will return the first index values in jason format  
    output_job_to_xls(json)
'''
'''
O/P :- 
[dict_keys(['slug', 'id', 'epoch', 'date', 'company', 'company_logo', 'position', 'tags', 'description', 'location', 'salary_min', 'salary_max', 'apply_url', 'logo', 'url'])]
here all those things will be stored in Excel...
'''

#Sending Email Using Python & SMTP 
# To send email than we need to enable a feature on Email
#example :- Gmail, SendGrid Email Platform we need to enable some links in Gmail

BASE_URL = 'https://remoteok.com/api/'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
REQUEST_HEADER = {
    'User-Agent':USER_AGENT,
    'Accept-Lan': 'en-US, en;q=0.5',
}

def get_job_postings():
    #res - request variable , using get() to fetch URL
    res = requests.get(url=BASE_URL, headers=REQUEST_HEADER )
    return res.json() #it will retuen the responce in the json format

def output_job_to_xls(data):
    wb = Workbook() #Workbook - is an Object Instance
    job_sheet = wb.add_sheet('Jobs') #parameter that we have passed into the sheet is name of Sheet
    #we need to add the Headers value for what the data will be
    headers = list(data[0].keys()) #header will be be the data of the list , keys()
    for i in range(0, len(headers)):
        job_sheet.write(0, i, headers[i]) #here in write(row, column, value)

    #Adding remaing data ..
    for i in range(0, len(data)):
        job = data[i] #here data will be store in job 
        values = list(job.values()) #same we we collected values in list like headers 
        for x in range(0, len(values)):
            job_sheet.write(i+1, x, values[x]) #here i+1 from next line it will store data, values will be store using write()
    wb.save('remote_jobs.xls')

def send_email(send_from, send_to, subject, text, files =None):
    assert isinstance(send_to, list)
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject 

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(fil.read(), Name=basename(f))
        part['Content-Disposition'] = f'attachment; filename="{basename}"'
        msg.attach(part)

    smtp = smtplib.SMTP('smtp.gamail.com: 587')
    smtp.starttls()
    smtp.login(send_from, '')
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

if __name__ == '__main__':
    json = get_job_postings()[1:] #[1] it will return the first index values in jason format  
    output_job_to_xls(json)
    send_email('karmakarshruti36@gmail.com', ['shruti.karmakar18@gmail.com'], 'Job Posting','Please find a attached list of Job Postings',
     files=['remote_jobs.xls'])