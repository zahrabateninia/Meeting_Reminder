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

# day of the week function: 
def dow(date):
    dateobj = datetime.datetime.strptime(date, r"%Y-%m-%d") # datetime.datetime.strptime(date_string, format)
    return dateobj.strftime("%A") # %A is a directive that represents the full name of the day of the week

# print(dow("12/05/2024"))  # Output: "Saturday"

def message_template(date, title, name):
    message = email.message.EmailMessage()
    weekday = dow(date)
    message['Subject'] = f'Meeting reminder: "{title}"'
    message.set_content(f'''
Hi "{name}"!

This is a quick mail to remind you that we have a meeting about:
"{title}"
the {weekday} {date}.


See you there.
''')
    return message

def read_names(contacts):
    names = {}
    with open(contacts) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            names[row[0]] = row[1]
    return names



def send_message(message, emails, contacts):
    smtp = smtplib.SMTP('localhost')
    names = read_names(contacts)
    message['From'] = 'noreply@example.com'
    for email in emails.split(','):
        name = names[email]
        del message['To']
        message['To'] = email
        smtp.send_message(message)
    smtp.quit()
    pass


def main():
    if len(sys.argv) < 2:
        return usage()
    try:
        # split the received parameters in three
        date, title, emails = sys.argv[1].split('|')
        message = message_template(date, title, name)
        send_message(message, emails)
        print("Successfully sent reminders to:", emails)
    except Exception as e:
        print("Failure to send email with {}".format(e), file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main())