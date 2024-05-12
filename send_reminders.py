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

