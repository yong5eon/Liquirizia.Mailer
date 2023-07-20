# -*- coding: utf-8 -*-

from .ContentImage import ContentImage
from ..Error import Error

from os.path import split

__all__ = (
	'ContentImageFile'
)


class ContentImageFile(ContentImage):
	def __init__(self, file, name=None):
		try:
			self.file = file
			self.path, self.filename = split(file)
			super(ContentImageFile, self).__init__(open(self.file, 'rb').read(), name if name else self.filename)
		except Exception as e:
			# TODO : exception handling for file not found
			raise Error(reason=str(e), error=e)
		return
