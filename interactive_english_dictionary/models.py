from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class DictionaryQuery(models.Model):
    '''
        we are saving the searched data
        how many times user searches for a word
        is the user is not authenicated then the search will be saved with "admin"
        if the user is authenticated then the user name will be saved
        the purpose for this is find the result we are unable to find
    '''
    user = models.ForeignKey(User, blank=True, null=True, on_delete = models.SET_NULL)
    word = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add = True)
    result = models.CharField(max_length=120)

    # def __str__(self):
    #     return "{user}-{word}-{result}".format(
    #                             user=self.user,
    #                             word=self.word,
    #                             result=self.result1,
    #                             )
