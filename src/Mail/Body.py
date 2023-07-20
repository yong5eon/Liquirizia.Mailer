# -*- coding: utf-8 -*-

from .Content import Content

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

__all__ = (
	'Body'
)


class Body(object):
	def __init__(self, message: str, type: str, charset: str = 'utf-8'):
		self.message = message
		self.type = type
		self.charset = charset
		self.contents = list()
		return

	def __str__(self):
		return self.getMessage().as_string()

	def addContent(self, content: Content):
		self.contents.append(content)
		return

	def getMessage(self):
		messageBody = MIMEMultipart("related")
		messageBody.attach(MIMEText(self.message, self.type, self.charset))
		for content in self.contents:
			messageBody.attach(content.getMessage())
		return messageBody


	
