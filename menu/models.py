from django.db import models


class Menu(models.Model):
    id = models.CharField(max_length=50, verbose_name='שם',primary_key=True)
    parent = models.ForeignKey('self',verbose_name='הורה', null=True, blank=True, related_name='children',
                               on_delete=models.PROTECT)
    link = models.CharField(max_length=100,verbose_name='כתובת URL', null=True, blank=True)
    info = models.CharField(max_length=100,verbose_name='תיאור בקצרה', null=True, blank=True)

    def __str__(self):
        return self.id

# class Link(models.Model):
#     parent = models.ForeignKey(Menu, null=True, blank=True, related_name='link', on_delete=models.PROTECT)
#     link = models.CharField(max_length=100, null=True, blank=True)
#     info = models.CharField(max_length=100, null=True, blank=True)
#     name = models.CharField(max_length=100, null=True, blank=True)
#
#     def __str__(self):
#         return self.name
