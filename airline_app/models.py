from django.db import models


class Roles(models.Model):
    role = models.CharField(max_length=20)


class Users(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    e_mail = models.EmailField()
    password = models.CharField(max_length=20)
    id_role = models.ForeignKey(to=Roles, on_delete=models.CASCADE, related_name='id_role')
    confirmed = models.BooleanField(default=False)


class Team(models.Model):
    id_pilot1 = models.ForeignKey(to=Users, on_delete=models.CASCADE, related_name='pilot1')
    id_pilot2 = models.ForeignKey(to=Users, on_delete=models.CASCADE, related_name='pilot2')
    id_navigator = models.ForeignKey(to=Users, on_delete=models.CASCADE, related_name='navigator')
    id_radioman = models.ForeignKey(to=Users, on_delete=models.CASCADE, related_name='radioman')
    id_stewardess1 = models.ForeignKey(to=Users, on_delete=models.CASCADE, related_name='stewardess1')
    id_stewardess2 = models.ForeignKey(to=Users, on_delete=models.CASCADE, related_name='stewardess2')


class Flights(models.Model):
    from_city = models.CharField(max_length=30, default='')
    to_city = models.CharField(max_length=30, default='')
    id_team = models.ForeignKey(to=Team, on_delete=models.CASCADE, null=True)
