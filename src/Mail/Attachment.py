# -*- coding: utf-8 -*-

from email.mime.application import MIMEApplication

__all__ = (
	'Attachment'
)


class Attachment(object):
	def __init__(self, buffer, format=None, charset=None, name=None):
		self.buffer = buffer
		self.format = format
		self.charset = charset
		self.name = name
		return

	def getMessage(self):
		attach = MIMEApplication(self.buffer)
		if self.name:
			attach.add_header('Content-Disposition', 'attachment', filename=self.name)
		if self.format:
			attach.add_header('Content-Type', self.format, charset=self.charset)
		return attach
