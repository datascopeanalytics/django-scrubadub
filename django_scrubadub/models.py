from django.db import models


class Document(models.Model):
    """The Document stores the raw text of the document that needs to be
    scrubbed
    """

    text = models.TextField()


class FilthType(models.Model):
    """Each type of filth is stored independently in the database including, as
    necessary, any parameters of the filth.
    """

    name = models.CharField(max_length=255)
    detector_cls = models.CharField(max_length=255)
    parameters = models.TextField()


class Filth(models.Model):
    """This stores the relevant information for each piece of filth, including
    the document in which it appears and its FilthType
    """

    beg = models.IntegerField()
    end = models.IntegerField()
    text = models.CharField(max_length=255)
    document = models.ForeignKey(Document)
    type = models.ForeignKey(FilthType)
