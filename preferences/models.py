from django.db import models


class Preferences(models.Model):

    # sms prefs
    introductory_text = models.TextField()
    single_option_text = models.TextField()
    multiple_option_text = models.TextField()
    no_option_text = models.TextField(null=True)
    preferred_day_set_text = models.TextField()
    default_reply_text = models.TextField()
    day_pattern_matching = models.TextField(null=True)