from django.db import models

class Menu(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_DISABLE = 'disable'

    LIST_STATUSES = ((STATUS_ACTIVE, STATUS_ACTIVE), (STATUS_DISABLE, STATUS_DISABLE))

    status = models.CharField(max_length=50, choices=LIST_STATUSES)
    url = models.CharField(unique=True, max_length=255, blank=True, default=None)

    def relations(key = False):
        if key:
            result = MenuLang.objects.filter(menu_id = key, lang='uk')
            if result:
                return result
            else:
                return MenuLang()
        else:
            return MenuLang()

class MenuLang(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, default=None)
    lang = models.CharField(max_length=255, blank=True, default=None)
