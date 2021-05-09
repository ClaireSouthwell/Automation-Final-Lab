#! /usr/bin/env python3

import os, datetime, reports, emails, sys


# Process text data from the supplier-data/descriptions directory

def read_data():
    paragraph = ''
    path = 'supplier-data/descriptions/'
    descriptions = os.listdir(path)

    for description in descriptions:
        if description.endswith('.txt'):
            with open(path + description, 'r') as d:
                lines = d.readlines()
                name = lines[0].strip()
                weight = lines[1].strip()
                paragraph += f'name: {name}</br>weight: {weight}<br/><br/>'

    return paragraph

today = datetime.datetime.now().strftime('%Y-%m-%d')

if __name__ == '__main__':
    title = 'Process Updated on ' + today

    pdf = read_data()

    # Generate the PDF report.   
    reports.generate('/tmp/processed.pdf', title, pdf)                   

    #Generate the email with the given address info  
    sender = 'automation@example.com'
    receiver = '{}@example.com'.format(os.environ.get('USER'))
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully.\nA detailed list is attached to this email.'
    message = emails.generate_email(sender, receiver, subject, body, '/tmp/processed.pdf')

    # Send the email 
    emails.send_email(message)


