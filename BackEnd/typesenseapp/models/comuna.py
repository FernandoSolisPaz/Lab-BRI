from mongoengine import Document, StringField, DictField

# Indica el nombre y polígono de la comuna correspondiente.
class Comuna(Document):
    nombre = StringField(required=True, unique=True)
    geometria = DictField(required=True)

    meta = {
        'collection': 'comunas',
        'indexes': [
            {
                'fields': [('geometria','2dsphere')]
            }
        ]
    }