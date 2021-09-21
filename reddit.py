import praw
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import credentials

reddit = praw.Reddit(
    client_id = credentials.client_id,
    client_secret = credentials.client_secret,
    username = credentials.username,
    password = credentials.password,
    user_agent= credentials.user_agent
)

subreddit = reddit.subreddit('finance')

hot_finance = subreddit.hot(limit=10)

posts = []

def worldnews():
    for post in hot_finance:
        posts.append(post.title + '\n' + post.url + '\n')


# this function below will send an email with the headlines you have chosen from Reddit. I will leave it here since I have used it in the past but it serves no purpose in this script now
def email():
    # prepare HTML email
    message = MIMEMultipart("alternative")
    message["Subject"] = 'Today\'s headlines'
    message["From"] = 'News bot'
    recipients = []
    message["To"] = ''
    message["bcc"] = " ,".join(recipients)

    # creating the content of the email, first the plain content then the html content

    plain = """
    Today's headlines:
    """ + '\n'.join(posts)

    html = """
    <h1 style="color: #f00; background: #000; font-weight: bold">Today's headlines!</h1>
    """ + '<br />\n'.join(posts)

    # now we compile both parts to prepare them to send

    part1 = MIMEText(plain, 'plain')
    part2 = MIMEText(html, 'html')
    message.attach(part1)
    message.attach(part2)

    # Now send the email

    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.ehlo()
    gmail_user = 'your username here'
    gmail_pwd = 'your password here'
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pwd)
    server.sendmail(message["From"], recipients, message.as_string())


def main():
    worldnews()

main()
