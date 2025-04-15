# Liquirizia.Mailer

이메일 송신자

## 사용 방법

```python
from Liquirizia.Mailer import Mailer, SendMail
from Liquirizia.Mailer.Mail import Mail


# 이메일 송신 객체 구현
class SampleSendMail(SendMail):
 def __call__(self, mail: Mail):
  # TODO : do something
  return

# 이메일 송신자를 사용해서 메일 전속
sender = Mailer(SampleSendMail())

# 텍스트 메일 전송
sender.sendText(
 '${SENDER_EMAIL_ADDRESS}',
 '${RECEIVER_EMAIL_ADDRESS}',
 '${SUBJECT}',
 '${CONTENT}',
 sender='${SENDER}',
 receiver='${RECEIVER}',
)

# HTML 메일 전송
sender.sendHTML(
 '${SENDER_EMAIL_ADDRESS}',
 '${RECEIVER_EMAIL_ADDRESS}',
 '${SUBJECT}',
 '${CONTENT_WITH_HTML}',
 sender='${SENDER}',
 receiver='${RECEIVER}',
)

# Mail 객체를 활용한 전송
mail = Mail('${SENDER_EMAIL_ADDRESS}', '${SENDER}')
mail.addTo('${RECEIVER_EMAIL_ADDRESS}', '${RECEIVER}')
mail.setSubject('${SUBJECT}')
mail.setHTML('${CONTENT_WITH_HTML')
mail.addContentImageFile('${ATTACHED_IMAGE_FILE_PATH_IN_CONTENT}')
mail.addFile('${ATTACHED_FILE_PATH}')

sender.send(mail)
```

## SMTP 구현체 사용

```python

from Liquirizia.Mailer import Mailer
from Liquirizia.Mailer.Mail import Mail

from Liquirizia.Mailer.Implements.SMTP import SendMail

if __name__ == '__main__':

 Mailer(SendMail(
  host='${SMTP_HOST_ADDRESS}',
  port=567,  # SMTP HOST PORT
  account='${SMTP_ACCOUNT}',
  password='${SMTP_ACCOUNT_PASSWORD}',
  secure=True,  # True or False
 ))

 # 텍스트 메일 전송
 Mailer.SendText(
  '${SENDER_EMAIL_ADDRESS}',
  '${RECEIVER_EMAIL_ADDRESS}',
  '${SUBJECT}',
  '${CONTENT}',
  sender='${SENDER}',
  receiver='${RECEIVER}',
 )

 # HTML 메일 전송
 Mailer.sendHTML(
  '${SENDER_EMAIL_ADDRESS}',
  '${RECEIVER_EMAIL_ADDRESS}',
  '${SUBJECT}',
  '${CONTENT_WITH_HTML}',
  sender='${SENDER}',
  receiver='${RECEIVER}',
 )

 # Mail 객체를 활용한 전송
 mail = Mail('${SENDER_EMAIL_ADDRESS}', '${SENDER}')
 mail.addTo('${RECEIVER_EMAIL_ADDRESS}', '${RECEIVER}')
 mail.setSubject('${SUBJECT}')
 mail.setHTML('${CONTENT_WITH_HTML')
 mail.addContentImageFile('${ATTACHED_IMAGE_FILE_PATH_IN_CONTENT}')
 mail.addFile('${ATTACHED_FILE_PATH}')

 Mailer.Send(mail)
```

## 구현체

* [AWS SES(Simple Email Service)](https://github.com/yong5eon/Liquirizia.Mailer.Implements.AWS.SimpleEmailService)
