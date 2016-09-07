from django.db import models


class Admins(models.Model):
    max_len_name = 30
    max_len_pass = 20
    name = models.CharField(max_length=max_len_name)
    surname = models.CharField(max_length=max_len_name)
    e_mail = models.EmailField()
    password = models.CharField(max_length=max_len_pass)


class Dispatcher(models.Model):
    max_len_name = 30
    max_len_pass = 20
    name = models.CharField(max_length=max_len_name)
    surname = models.CharField(max_length=max_len_name)
    e_mail = models.EmailField()
    password = models.CharField(max_length=max_len_pass)


class Pilots(models.Model):
    max_len_name = 30
    max_len_pass = 20
    name = models.CharField(max_length=max_len_name)
    surname = models.CharField(max_length=max_len_name)
    e_mail = models.EmailField()
    password = models.CharField(max_length=max_len_pass)


class Navigators(models.Model):
    max_len_name = 30
    max_len_pass = 20
    name = models.CharField(max_length=max_len_name)
    surname = models.CharField(max_length=max_len_name)
    e_mail = models.EmailField()
    password = models.CharField(max_length=max_len_pass)


class Radiomen(models.Model):
    max_len_name = 30
    max_len_pass = 20
    name = models.CharField(max_length=max_len_name)
    surname = models.CharField(max_length=max_len_name)
    e_mail = models.EmailField()
    password = models.CharField(max_length=max_len_pass)


class Stewardess(models.Model):
    max_len_name = 30
    max_len_pass = 20
    name = models.CharField(max_length=max_len_name)
    surname = models.CharField(max_length=max_len_name)
    e_mail = models.EmailField()
    password = models.CharField(max_length=max_len_pass)


class Flights(models.Model):
    max_city = 30
    from_city = models.CharField(max_length=max_city)
    to_city = models.CharField(max_length=max_city)
    date = models.DateTimeField()
    id_team = models.ForeignKey(to=Team, on_delete=models.CASCADE, related_name='team')


class Team(models.Model):
    id_pilot1 = models.ForeignKey(to=Pilots, on_delete=models.CASCADE, related_name='pilot1')
    id_pilot2 = models.ForeignKey(to=Pilots, on_delete=models.CASCADE, related_name='pilot2')
    id_navigator = models.ForeignKey(to=Navigators, on_delete=models.CASCADE, related_name='navigator')
    id_radioman = models.ForeignKey(to=Radiomen, on_delete=models.CASCADE, related_name='radioman')
    id_stewardess1 = models.ForeignKey(to=Stewardess, on_delete=models.CASCADE, related_name='stewardess1')
    id_stewardess2 = models.ForeignKey(to=Stewardess, on_delete=models.CASCADE, related_name='stewardess2')