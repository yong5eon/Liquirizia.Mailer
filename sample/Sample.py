# -*- coding: utf-8 -*-

from Liquirizia.Mailer import Mailer, SendMail
from Liquirizia.Mailer.Mail import Mail

# 이메일 송신 객체 구현
class SampleSendMail(SendMail):
	def __call__(self, mail: Mail):
		print(mail.getFromAddress())
		print(mail.getToAddresses())
		print(mail.getMessage().as_string())
		return

# 이메일 송신자를 사용해서 메일 전속
sender = Mailer(SampleSendMail())

# 텍스트 메일 전송
sender.sendText(
	'from@email.com',
	'to@email.com',
	'제목',
	'내용',
	sender='보내는 사람',
	receiver='받는 사람',
)

# HTML 메일 전송
sender.sendHTML(
	'from@email.com',
	'to@email.com',
	'제목',
	'<HTML><BODY>내용</BODY></HTML>',
	sender='보내는 사람',
	receiver='받는 사람',
)

# Mail 객체를 활용한 전송
mail = Mail('from@email.com', '보내는 사람')
mail.addTo('to@email.com', '받는사람')
mail.setSubject('제목')
mail.setHTML('<HTML><BODY>내용<BR/><IMG SRC="cid:img.png"/></BODY></HTML>')
mail.addContentImageFile('res/img.jpg')
mail.addFile('README.md')

sender.send(mail)
