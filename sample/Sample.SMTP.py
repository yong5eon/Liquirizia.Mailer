# -*- coding: utf-8 -*-

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