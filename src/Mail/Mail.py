# -*- coding: utf-8 -*-

from .Contact import Contact
from .File import File
from .Attachment import Attachment

from .Properties import Text, HTML
from .ContentImage import ContentImage
from .ContentImageFile import ContentImageFile

from email.mime.multipart import MIMEMultipart

__all__ = (
	'Mail'
)


class Mail(object):
	"""
	Mailer Class

	TODO :
	* Support Audio Content
	* Support Video Content
	* Support Application Content
	"""
	def __init__(self, address: str, alias: str = None, charset: str = 'utf-8'):
		self.charset = charset
		self.frm = Contact(address, alias, charset)
		self.to = []
		self.cc = []
		self.bcc = []
		self.subject = None
		self.body = None
		self.attachments = []
		return

	def setFrom(self, address: str, alias: str = None):
		self.frm = Contact(address, alias, self.charset)
		return

	def getFromAddress(self):
		return self.frm.address

	def getFrom(self):
		return str(self.frm)

	def addTo(self, address: str, alias: str = None):
		self.to.append(Contact(address, alias, self.charset))
		return

	def addCC(self, address: str, alias: str = None):
		self.cc.append(Contact(address, alias, self.charset))
		return

	def addBCC(self, address: str, alias: str = None):
		self.bcc.append(Contact(address, alias, self.charset))
		return

	def getToAddresses(self):
		contacts = []
		contacts.extend(self.to)
		contacts.extend(self.cc)
		contacts.extend(self.bcc)
		return [contact.address for contact in contacts]
		# return ','.join([contact.address for contact in contacts])

	def getToes(self):
		contacts = []
		contacts.extend(self.to)
		contacts.extend(self.cc)
		contacts.extend(self.bcc)
		return ','.join([str(contact) for contact in contacts])

	def setSubject(self, text):
		self.subject = text
		return

	def setText(self, text):
		self.body = Text(text, self.charset)
		return

	def setHTML(self, html):
		self.body = HTML(html, self.charset)
		return

	def addContentImage(self, buffer, name=None):
		self.body.addContent(ContentImage(buffer, name))
		return

	def addContentImageFile(self, file, name=None):
		self.body.addContent(ContentImageFile(file, name))
		return

	def addFile(self, file):
		self.attachments.append(File(file))
		return

	def addAttachment(self, buffer, format=None, charset=None, name=None):
		self.attachments.append(Attachment(buffer, format, charset, name))
		return
	
	def getMessage(self):
		message = MIMEMultipart()
		message['Subject'] = self.subject
		message['From'] = str(self.frm)
		message['To'] = ','.join([str(contact) for contact in self.to])
		if self.cc and len(self.cc):
			message['Cc'] = ','.join([str(contact) for contact in self.cc])
		if self.bcc and len(self.bcc):
			message['Bcc'] = ','.join([str(contact) for contact in self.bcc])
		body = self.body.getMessage()
		message.attach(body)
		for attach in self.attachments if self.attachments else []:
			message.attach(attach.getMessage())
		return message
	
