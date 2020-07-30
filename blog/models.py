# Blog Model
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)  # title
    pubdate = models.DateTimeField()  # pubdate
    image = models.ImageField(upload_to='images/')  # image
    body = models.TextField(max_length=400)  # body

    # To show in admin page and other pages
    def __str__(self):
        return self.title

    # Too long texts get shortened
    def summary(self):
        if len(self.body) < 50:
            return self.body
        else:
            return (self.body[:50] + " [...]")

    # Property for showing pretty date
    def pubdate_pretty(self):
        return self.pubdate.strftime("%d. %B %Y")
        # Jeg vil gerne indarbejde dette:
        # http://babel.pocoo.org/en/latest/dates.html
