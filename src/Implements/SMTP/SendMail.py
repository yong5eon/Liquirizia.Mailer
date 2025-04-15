# -*- coding: utf-8 -*-

from Liquirizia.Mailer import SendMail as Base, Error
from Liquirizia.Mailer.Mail import Mail

from smtplib import SMTP

__all__ = (
	'SendMail'
)


class SendMail(Base):
	"""
	SendMail Class for SMTP
	"""
	def __init__(self, host, port, account, password, secure=False):
		self.host = host
		self.port = port
		self.account = account
		self.password = password
		self.secure = secure
		return

	def __call__(self, mail: Mail):
		try:
			connection = SMTP(self.host, self.port)
			if self.secure:
				connection.starttls()
			connection.login(self.account, self.password)
			connection.sendmail(
				mail.getFromAddress(),
				mail.getToAddresses(),
				mail.getMessage().as_string()
			)
			connection.quit()
		except BaseException as e:
			raise Error(str(e), error=e)
		return
