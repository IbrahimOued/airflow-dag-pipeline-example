import argparse
import configparser
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import os

def main(recipients, server, port, from_email, password, attachments_path:str):
    print(f'With love, from {from_email} to {recipients}')
    # Create the message
    subject = 'With love, from ME to YOU'
    text = '''This is an example test'''
    
    msg = MIMEMultipart()

    body = MIMEText(text)
    msg.attach(body)
    
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = ",".join(recipients)
    

    files = _get_files_from_path(attachments_path)
    for f in files or []:
        with open(f, "rb") as file:
            part = MIMEApplication(
                file.read(),
                Name=os.path.basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(f)
        msg.attach(part)

    # Open communication and send
    server = smtplib.SMTP_SSL(server, port)
    server.login(from_email, password)
    server.send_message(msg)
    server.quit()

def _get_files_from_path(path:str):
    matches = []
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            # if filename.endswith(('.xlsx', '.MOV', '.avi', '.mpg')):
            if filename.endswith(('.xlsx')):
                matches.append(os.path.join(root, filename))
    return matches

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--r', dest='recipients', nargs="*", default=['brahim.oued@gmail.com'], help='destination email')
    parser.add_argument('--p', dest='attachments_path', type=str, help='attachments files path')
    parser.add_argument('-c', dest='config', type=argparse.FileType('r'), help='config file', default=None)
    args = parser.parse_args()

    if not args.config:
        print('Error, a config file is required')
        parser.print_help()
        exit(1)

    config = configparser.ConfigParser()
    config.read_file(args.config)

    main(args.recipients,
        server=config['DEFAULT']['server'], 
        port=config['DEFAULT']['port'],
        from_email=config['DEFAULT']['email'],
        password=config['DEFAULT']['password'],
        attachments_path=args.attachments_path)