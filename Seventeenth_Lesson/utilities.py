#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 21:31:38 2017

@author: ChrisErnst
"""

# create a link adder function:
def add_link(year, model='civic'):
    try:
        model = str(model)
        year =  str(year)
        # Convert to strings
        link = ('https://losangeles.craigslist.org/search/cto?query=%28' + year + '+' + model + '*%29+-salv*&srchType=T&bundleDuplicates=1&nearbyArea=104&nearbyArea=103&nearbyArea=209&nearbyArea=208&min_price=999&max_price=15000&min_auto_miles=999&max_auto_miles=110000')
        # Build the link as a string        
        return link
    except:
        print ("please make sure to use quotes around car model")
    
    

def email_client(attachFile):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email import encoders
    from email.mime.base import MIMEBase

    
    try:
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo() # optional, called by login()
        MY_ADDRESS = input('Please Enter Email Address: ')
        PASSWORD = input('Please Enter Password: ')
        server_ssl.login(MY_ADDRESS, PASSWORD)  
        
        
        msg = MIMEMultipart()
        msg['Subject'] = "Craigslist Data" 
        msg['From'] = "from@email.com"
        msg['To'] =  "to@email.com"
        msg['Text'] = "Here is the latest data"
    
    
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(attachFile, "rb").read())
        encoders.encode_base64(part)
    
        part.add_header('Content-Disposition', 'attachment', filename='TheFileName.csv')
    
        msg.attach(part)
    
        server_ssl.sendmail(MY_ADDRESS, MY_ADDRESS, msg.as_string())
        server_ssl.close()
        print('\n\nSuccessfully sent the email!')

        
    except:
        print('an error occured')
    
            
    
    
    
    

        
