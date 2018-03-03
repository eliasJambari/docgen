import os
import sys
import smtplib
import logging
logger = logging.getLogger()

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from excel import my_constants as cst
from gui import progress

class MailManager():
    def __init__(self, mail_query):
        self.mail_config = MailConfig("test.auto.1990@gmail.com", "galaxys4")
        self.mails = self.extract_query(mail_query)

    # Extracts mails from query (2D table) and creates mail objects
    def extract_query(self, mail_query):
        mails = []

        logger.debug("Mail query : " + str(mail_query))

        for entry in mail_query:
            mail = Mail(self.mail_config, entry[cst.RECIPIENT], entry[cst.SUBJECT], entry[cst.MESSAGE], entry[cst.ATTACHMENTS])
            mails.append(mail)

        return mails

    def send_emails(self):
        for mail in self.mails:
            mail.generate()
            mail.send()


class MailConfig():
    def __init__(self, sender, password):
        self.sender = sender
        self.password = password


class Mail:
    def __init__(self, mail_config, recipient, subject, message, attachments):
        self.recipient = recipient
        self.subject = subject
        self.message = message
        self.attachments = attachments # Array

        self.mail_config = mail_config

        self.status = cst.PENDING

    def generate(self):
        progress.tmp_solution(1, "Sending mails", debug=("Generating mail"))

        # Create the enclosing (outer) message
        outer = MIMEMultipart()
        outer["Subject"] = self.subject
        outer["To"] = self.recipient
        outer["From"] = self.mail_config.__getattribute__("sender")
        # outer.preamble = "You will not see this in a MIME-aware mail reader.\n"

        outer.attach(MIMEText(self.message, 'plain'))

        # Add the attachments to the message
        for file in self.attachments:
            try:
                with open(file, "rb") as fp:
                    msg = MIMEBase("application", "octet-stream")
                    msg.set_payload(fp.read())
                encoders.encode_base64(msg)
                msg.add_header("Content-Disposition", "attachment", filename=os.path.basename(file))
                outer.attach(msg)
            except:
                print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
                raise

        return outer.as_string()

    def send(self):
        self.status = cst.IN_PROGRESS

        composed_msg = self.generate()

        progress.tmp_solution(1, "Sending mails", debug=("Sending mail"))
        sender = self.mail_config.__getattribute__("sender")
        password = self.mail_config.__getattribute__("password")

        # Send the email
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as s:
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(sender, password)
                s.sendmail(sender, self.recipient, composed_msg)
                s.close()
            logger.info("Email sent to '" + str(self.recipient) + "' with '" + str(self.attachments) + "'")
            self.status = cst.SENT
            return self.status
        except:
            print("Unable to send the email. Error: ", sys.exc_info()[0])
            self.status = cst.NOT_SENT
            return self.status


def check_auth(user, password):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()

    try:
        server.login(user, password)
        result = True
    except:
        result = False

    server.quit()

    return result

if __name__ == "__main__":
    user = "test.auto.1990@gmail.com"
    password = "galaxys4"

    result = check_auth(user, password)

    print(result)


