#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 21:31:38 2017

@author: ChrisErnst
"""
# this is the one!
# create a link adder function:
def add_link(year, model='civic'):
    try:
        model = str(model)
        year =  str(year)
        # Convert to strings
        linkSuffix = '*%29+-salv*&srchType=T&bundleDuplicates=1&min_price=999&max_price=15000&min_auto_miles=999&max_auto_miles=110000&auto_title_status=1&auto_title_status=3&auto_title_status=4&auto_title_status=5&auto_title_status=6'
        # LA
        link1 = ('https://losangeles.craigslist.org/search/cto?query=%28' + year + '+' + model + linkSuffix)
        # San Diego
        link2 = ('https://sandiego.craigslist.org/search/cto?query=%28' + year + '+' + model + linkSuffix)
        # IE
        link3 = ('https://inlandempire.craigslist.org/search/cto?query=%28' + year + '+' + model + linkSuffix)
        # Orange County
        link4 = ('https://orangecounty.craigslist.org/search/cto?query=%28' + year + '+' + model + linkSuffix)
        # Palm Springs
        link5 = ('https://palmsprings.craigslist.org/search/cto?query=%28' + year + '+' + model + linkSuffix)

        # Build the link as a string         
        return link1, link2, link3, link4, link5
    except:
        print ("please make sure to use quotes around car model")
    
    
    

def email_client(theFileName, recipientEmail):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email import encoders
    from email.mime.base import MIMEBase
    # libs
    
    try:
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo() # optional, called by login()
        MY_ADDRESS = input('Please Enter Email Address: ')
        # asks for user email
        PASSWORD = input('Please Enter Password: ')
        # asks for the password
        server_ssl.login(MY_ADDRESS, PASSWORD)  
        # ssl login
        
        msg = MIMEMultipart()
        msg['Subject'] = "Craigslist Data" 
#        msg['From'] = "from@email.com"
#        msg['To'] =  "to@email.com"
#        msg['Text'] = "Here is the latest data"
    
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(theFileName, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename='TheFileName.csv')
        msg.attach(part)
    
        server_ssl.sendmail(MY_ADDRESS, recipientEmail, msg.as_string())
        server_ssl.close()
        print('\n\nSuccessfully sent the email!')
        
    except:
        print('an error occured')
    
            
    
    
    
    

        
