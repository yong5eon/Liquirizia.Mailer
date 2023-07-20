# -*- coding: utf-8 -*-

from Liquirizia.Template.Singleton import Singleton

from .SendMail import SendMail
from .Mail import Mail

__all__ = (
	'Mailer'
)


class Mailer(Singleton):
	"""
	Mailer Class
	"""
	def __init__(self, sender: SendMail):
		self.sender = sender
		return

	@classmethod
	def Send(cls, mail: Mail):
		mailer = cls()
		return mailer.send(mail)

	def send(self, mail: Mail):
		return self.sender(mail)

	@classmethod
	def SendText(cls, frm: str, to: str, subject: str, body: str, charset: str = 'utf-8', sender: str = None, receiver: str = None):
		mailer = cls()
		return mailer.sendText(frm, to, subject, body, charset, sender, receiver)

	def sendText(self, frm: str, to: str, subject: str, body: str, charset: str = 'utf-8', sender: str = None, receiver: str = None):
		mail = Mail(frm, sender, charset)
		mail.addTo(to, receiver)
		mail.setSubject(subject)
		mail.setText(body)
		return self.send(mail)

	@classmethod
	def SendHTML(cls, frm: str, to: str, subject: str, body: str, charset: str = 'utf-8', sender: str = None, receiver: str = None):
		mailer = cls()
		return mailer.sendHTML(frm, to, subject, body, charset, sender, receiver)

	def sendHTML(self, frm: str, to: str, subject: str, body: str, charset: str = 'utf-8', sender: str = None, receiver: str = None):
		mail = Mail(frm, sender, charset)
		mail.addTo(to, receiver)
		mail.setSubject(subject)
		mail.setHTML(body)
		return self.send(mail)
