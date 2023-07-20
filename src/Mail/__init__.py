# -*- coding: utf-8 -*-

from .Mail import Mail
from .Contact import Contact
from .Body import Body
from .Properties import Text, HTML
from .ContentImage import ContentImage
from .ContentImageFile import ContentImageFile
from .Attachment import Attachment
from .File import File

__all__ = (
	'Mail',
	'Contact',
	'Body',
	'Text',
	'HTML',
	'ContentImage',
	'ContentImageFile',
	'Attachment',
	'File',
)
