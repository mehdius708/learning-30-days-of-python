import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from templates import Template

# environment variables
username ='pythonesquet@gmail.com'
password ='Em@il4815162342'


class Emailer():
    from_email='pythonesquet@gmail.com'
    subject = 'Hi'
    to_emails = []
    has_html = False

    def __init__(self, subject='', template_name=None, context={}, template_html=None, to_emails=None, test_send=True):
        if template_name == None and template_html == None:
            raise Exception('You must set a template.')
        assert isinstance(to_emails, list)
        self.to_emails = to_emails
        self.subject = subject

        self.template_html = template_html
        if template_html != None:
            self.has_html = True

        self.template_name = template_name
        self.context = context

        self.test_send = test_send

    def format_msg(self):
        msg = MIMEMultipart('alternative')
        msg['From'] = self.from_email
        msg['To'] = ", ".join(self.to_emails)
        msg['Subject'] = self.subject

        if self.template_name != None:
            tmpl_str = Template(template_name=self.template_name, context=self.context)
            txt_part = MIMEText(tmpl_str.render(), 'plain')
            print(txt_part)
            msg.attach(txt_part)

        if self.template_html != None:
            tmpl_str = Template(template_name=self.template_html, context=self.context)
            html_part = MIMEText(tmpl_str.render(), 'html')
            print(html_part)
            msg.attach(html_part)

        msg_str = msg.as_string()
        return msg_str

    def send_mail(self):
        msg = self.format_msg()
        did_send = False
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(self.from_email, self.to_emails, msg)
            did_send = True
        return did_send
