# -*- coding: utf-8 -*-

from email.header import Header
from email.utils import formataddr

__all__ = (
	'Contact'
)


class Contact(object):

	def __init__(self, address: str, alias: str = None, charset: str = 'utf-8'):
		self.address = address
		self.alias = alias
		self.charset = charset
		return

	def __str__(self):
		return formataddr((str(Header(self.alias, self.charset)), self.address))

	def __repr__(self):
		return formataddr((str(Header(self.alias, self.charset)), self.address))
