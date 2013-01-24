from zope.interface import Interface


class IPresentationMode(Interface):
	"""Marker for content that supports presentation mode.

	By default this is applied to ATDocument in configure.zcml.
	"""