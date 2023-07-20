# -*- coding: utf-8 -*-

from .Mail import Mail

__all__ = (
	'SendMail'
)


class SendMail(object):
	"""
	SendMail Interface Class
	"""
	def __call__(self, mail: Mail):
		raise NotImplementedError('MailerInterface must be implemented __call__, constructor method')
