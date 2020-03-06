from django.db import models
from django.utils import timezone
# Create your models here.
class ApllyForm(models.Model):
    # author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    introduce = models.TextField('자기소개', max_length=1000)
    position = models.TextField('역할상상', max_length=500)
    goal = models.TextField('목표', max_length=500)
    plan = models.TextField('계획', max_length=500)
    team = models.TextField('팀활동', max_length=500)
    concept = models.TextField('컨셉', max_length=500)

    portfolio = models.FileField('포폴', blank= True, upload_to='portfolio/')
    interview = models.CharField('면접', max_length=255)
    experience = models.TextField('경험', max_length=1000)
    schedule = models.TextField('고정스케줄', max_length=1000)

    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title