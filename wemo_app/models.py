from django.db import models


class Memo(models.Model):
    memo_title = models.CharField(max_length=77)
    memo_text = models.TextField()

    def __str__(self):
        return self.memo_title
