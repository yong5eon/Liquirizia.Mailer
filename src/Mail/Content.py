# -*- coding: utf-8 -*-

__all__ = (
	'Content'
)


class Content(object):
	def getMessage(self):
		raise NotImplementedError('{} must be implemented getMessage'.format(self.__class__.__name__))
