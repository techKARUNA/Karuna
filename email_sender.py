import smtplib
from email.message import EmailMessage
import pandas as pd


sender_email = "gorkhakaruna@gmail.com"
password = "htge avzm chaw elio "

df = pd.read_excel('contacts.xlsx')

subject = "Your Subject Here"
with open("email_template.html", "r") as file:
    html_content = file.read()

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender_email, password)

sent = 0
failed = 0

for index, row in df.iterrows():
    try:
        msg = EmailMessage() 
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = row['Email']

        
        body = html_content.replace("[Recipient Name]", row['Name']) \
                           .replace("[Company Name]", row['Company'])

        msg.set_content(body, subtype='html')


        server.send_message(msg)
        print(f"✅ Sent to {row['Name']} - {row['Email']}")
        sent += 1
    except Exception as e:
        print(f"❌ Failed to send to {row['Name']} - {row['Email']}. Error: {e}")
        failed += 1
print("\n📊 Campaign Summary")
print(f"👥 Total Contacts: {len(df)}")
print(f"✅ Emails Sent: {sent}")
print(f"❌ Failed: {failed}")

server.quit()
