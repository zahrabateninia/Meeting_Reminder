#!/usr/bin/env python3

import datetime
import email
import smtplib
import sys

def usage():
    print("send_reminders: Send meeting reminders")
    print()
    print("invocation:")
    print("     send_reminders 'date|Meeting Title|Emails' ")
    return 1

def dow(date):
    dateobj = datetime.datetime.strftime(date, r"%d/%m/%Y")
    return dateobj.strftime("%A")

def message_template(date, title):
    message = email.message.EmailMessage()
    weekday = dow(date)
    message['Subject'] = f'Meeting reminder: "{title}"'
    message.set_content(f'''
Hi all!

This is a qick mail to remind you all that we have a meeting about:
"{title}"
the {weekday} {date}.


See you there.
''')
    return message



