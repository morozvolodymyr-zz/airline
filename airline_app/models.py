from django.db import models


class Roles(models.Model):
    max_len = 20
    role = models.CharField(max_length=max_len)


class Cities(models.Model):
    max_len = 25
    city = models.CharField(max_length=max_len)


class Users(models.Model):
    max_len_name = 30
    max_len_pass = 20
    name = models.CharField(max_length=max_len_name)
    surname = models.CharField(max_length=max_len_name)
    e_mail = models.EmailField()
    password = models.CharField(max_length=max_len_pass)
    id_role = models.ForeignKey(to=Roles, on_delete=models.CASCADE, related_name='id_role')
    confirmed = models.BooleanField()


class Team(models.Model):
    id_pilot1 = models.ForeignKey(to=Users, on_delete=models.CASCADE, related_name='pilot1')
    id_pilot2 = models.ForeignKey(to=Users, on_delete=models.CASCADE, related_name='pilot2')
    id_navigator = models.ForeignKey(to=Users, on_delete=models.CASCADE, related_name='navigator')
    id_radioman = models.ForeignKey(to=Users, on_delete=models.CASCADE, related_name='radioman')
    id_stewardess1 = models.ForeignKey(to=Users, on_delete=models.CASCADE, related_name='stewardess1')
    id_stewardess2 = models.ForeignKey(to=Users, on_delete=models.CASCADE, related_name='stewardess2')


class Flights(models.Model):
    id_from_city = models.ForeignKey(to=Cities, on_delete=models.CASCADE, related_name='from_city')
    id_to_city = models.ForeignKey(to=Cities, on_delete=models.CASCADE, related_name='to_city')
    date = models.DateTimeField()
    id_team = models.ForeignKey(to=Team, on_delete=models.CASCADE, related_name='team')
