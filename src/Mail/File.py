# -*- coding: utf-8 -*-

from .Attachment import Attachment
from ..Error import Error

from mimetypes import guess_type
from os.path import split

__all__ = (
	'File'
)


class File(Attachment):
	def __init__(self, file):
		try:
			self.file = file
			self.path, self.filename = split(file)
			self.format, self.charset = guess_type(file)
			super(File, self).__init__(open(self.file, 'rb').read(), self.format, self.charset, self.filename)
		except Exception as e:
			# TODO : exception handling for file not found
			raise Error(reason=str(e), error=e)
		return
