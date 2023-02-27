import smtplib
import os
import email.message

settings = {
    # Django mail settins
    "EMAIL_HOST": "smtp-mail.outlook.com",
    "EMAIL_PORT": 587,
    "EMAIL_HOST_USER": "noreply@novatusadvisory.com",
    "EMAIL_HOST_PASSWORD": os.environ["NOREPLY_EMAIL_PASSWORD"],
    "EMAIL_USE_TLS": True,
    # number of seconds before the verification code is expired in cache
    "EMAIL_VERIFICATION_CODE_EXPIRE_TIME": 300
}

def send_email(subject, recipient, html):
    smtp = smtplib.SMTP(settings["EMAIL_HOST"], settings["EMAIL_PORT"])
    smtp.ehlo('mylowercasehost')
    #Use TLS to add security 
    smtp.starttls() 
    smtp.ehlo('mylowercasehost')
    smtp.login(settings["EMAIL_HOST_USER"], settings["EMAIL_HOST_PASSWORD"])
    msg = email.message.Message()
    msg['Subject'] = subject
    msg['From'] = settings["EMAIL_HOST"]
    msg['To'] = recipient
    msg.add_header('Content-Type','text/html')
    msg.set_payload(html)
    #Sending the Email
    smtp.sendmail(settings["EMAIL_HOST_USER"], recipient, msg.as_string())
    smtp.quit() 

# when a user is first registered, an email is sent to them with their login details
# this function returns the html template of that email for the user
def get_invitation_email_template(email, password):
    template = f'''
    <html>
        <body>
            <img src="https://my-test-bucket11111.s3.eu-west-2.amazonaws.com/testing/novatus_logo.png" style="width: 100%;">
            <div>
                <p>Welcome to TRA Tool!</p>
            </div>
            <div>
                <p>Here are the login details required for your initial access to the website:</p>
            </div>
            <h2>username: novatus</h2>
            <h2>password: Syg046#9Vavo</h2>
            <div>
                <p>Upon entering the site, you will be prompted to input your account details. Here are your account details:</p>
            </div>
            <h2>username: {email}</h2>
            <h2>password: {password}</h2>
            <div>
                <p>The first time you log into our system <a href="tra.novatusregtech.com">tra.novatusregtech.com</a>, you will be asked to change your password.</p>
                <p>
                    <div>Best regards,</div>
                    <div>Novatus Advisory RegTech Team</div>
                </p>
            </div>
        </body>
        <footer>
            <br/>
            <p>This is an auto-generated email, please do not reply.</p>
        </footer>
    </html>
    '''
    return template

if __name__ == "__main__":
  send_email('test', 'hchen@novatusadvisory.com', get_invitation_email_template('test_email', 'test_password'))