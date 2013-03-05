from zope.interface import implements
from Products.CMFPlone import PloneMessageFactory as _
from Products.Archetypes import atapi
from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.field import ExtensionField


class ExtensionBooleanField(ExtensionField, atapi.BooleanField):
    pass


class PresentationSchemaExtender(object):
    implements(ISchemaExtender)

    fields = [
        ExtensionBooleanField(
            'presentation',
            schemata='settings',
            required=False,
            languageIndependent=True,
            widget=atapi.BooleanWidget(
                label=_(
                    u'help_enable_presentation',
                    default=u'Presentation mode'),
                description=_(
                    u'help_enable_presentation_description',
                    default=u'If selected, this will give users the ability '
                            u'to view the contents as presentation slides.')
            ),
        ),
    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
