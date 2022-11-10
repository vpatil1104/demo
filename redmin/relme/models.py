from django.db import models

# Create your models here.
from mongoengine import Document, fields

class Blogs(Document):
    name = fields.StringField()
    topic = fields.StringField()
    date = fields.DateTimeField()
    addition_info = fields.DictField()