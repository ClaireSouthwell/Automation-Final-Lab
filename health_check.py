#! /usr/bin/env python3

import shutil, psutil
import emails
import os, sys
import socket

# Prepare to send an email for any error 

def send_email(error):
    sender = 'automation@example.com'
    receiver = '{}@example.com'.format(os.environ.get('USER'))
    subject = error
    body = 'Please check your system and resolve the issue as soon as possible.'
    message = emails.generate_email(sender, receiver, subject, body)
    emails.send_email(message)

# Check if the CPU usage is over 80 

def cpu_check():
    cpu_usage = psutil.cpu_percent(1)
    if cpu_usage > 80:
        error = 'Error - CPU usage is over 80%' 
        send_email(error)
        
# Check if the available disk space is less than 20%
def disk_check():
    disk_total, disk_used, disk_free = shutil.disk_usage('/')
    if 100 * (disk_free / disk_total) < 20:
        error = 'Error - Available disk space is less than 20%'
        send_email(error)    

# Check if there is over 500 MB of available memory 
def mem_check():
    threshold = 500 * 1024 * 1024 # 500 MB
    mem = psutil.virtual_memory()
    if mem.available < threshold:
        error = 'Error - Available memory is less than 500MB'
        send_email(error)
    
def host_check():
    localhost = socket.gethostbyname('localhost')
    if localhost != '127.0.0.1':
        error = 'Error - localhost cannot be resolved to 127.0.0.1'
        send_email(error)


# Run all the checks 
cpu_check()
disk_check()
mem_check()
host_check()



'''p = psutil.Process()
cpu_usage = p.cpu_percent(interval=None)
if cpu_usage > 80.0:
    error_report = emails.generate_email(sender, receiver, cpu_subj, email_body)
    emails.send(error_report)    

# Report an error if available disk space is lower than 20%
disk_total, disk_used, disk_free = shutil.disk_usage(path)
if disk_free / disk_total < 0.20: # or multiply by 100 and use 20
    error_report = emails.generate_email(sender, receiver, disk_subj, email_body)
    emails.send(error_report)

# Report an error if available memory is less than 500MB
threshold = 500 * 1024 * 1024 # 500 MB
mem = psutil.virtual_memory()
if mem.available <= threshold:
    error_report = emails.generate_email(sender, receiver, mem_subj, email_body)
    emails.send(error_report)

# Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
localhost = socket.gethostbyname('localhost')
if localhost != '127.0.0.1':
    error_report = emails.generate_email(sender, receiver, host_subj, email_body)
    emails.send(error_report)

'''
