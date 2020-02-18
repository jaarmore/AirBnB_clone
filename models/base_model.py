#!/usr/bin/python3
""" BaseModel """
from datetime import datetime
from dateutil import parser
import models
import uuid


class BaseModel():
    """ BaseModel Class """
    def __init__(self, *args, **kwargs):
        """ Initialize objects """
        if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    setattr(self, k, parser.parse(v))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.__class__ = __class__.__name__
            models.storage.new(self)

    def __str__(self):
        """ String representation """
        dic = {}
        for k, v, in self.__dict__.items():
            if k != "__class__":
                dic[k] = v
        return "[{}] ({}) {}".format(type(self).__name__, self.id, dic)

    def save(self):
        """ Update and save object """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return directory """
        dic = {}
        for k, v, in self.__dict__.items():
            if k == 'created_at' or k == 'updated_at':
                dic[k] = datetime.isoformat(v)
            else:
                dic[k] = v
        return dic

    def __class__(self):
        """ Format name to string """
        return str(__class__.__name__)
