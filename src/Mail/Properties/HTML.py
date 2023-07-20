# -*- coding: utf-8 -*-

from ..Body import Body

__all__ = (
	'HTML'
)


class HTML(Body):
	def __init__(self, message: str, charset: str = 'utf-8'):
		super(HTML, self).__init__(message, 'html', charset)
		return
