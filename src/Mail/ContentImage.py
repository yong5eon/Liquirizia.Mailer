# -*- coding: utf-8 -*-

from .Content import Content

from email.mime.image import MIMEImage

__all__ = (
	'ContentImage'
)


class ContentImage(Content):
	def __init__(self, buffer, name=None):
		self.buffer = buffer
		self.name = name
		return

	def getMessage(self):
		image = MIMEImage(self.buffer)
		if self.name:
			image.add_header('Content-ID', "<{name}>".format(name=self.name))
		return image
