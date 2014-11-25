from django.db import models
import jsonfield


class Bookmark(models.Model):
    #owner
    bookmarks_json = jsonfield.JSONField()