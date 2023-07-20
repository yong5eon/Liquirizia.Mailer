# -*- coding: utf-8 -*-

from ..Body import Body

__all__ = (
	'Text'
)


class Text(Body):
	def __init__(self, message: str, charset: str = 'utf-8'):
		super(Text, self).__init__(message, 'plain', charset)
		return
