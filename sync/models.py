from django.db import models


class LocalVlans(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    vlan_id = models.IntegerField(default=1)



    class Meta:
        db_table = 'local_vlans'


class RemoteVlans(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    vlan_id = models.IntegerField(default=1)

    class Meta:
        db_table = 'remote_vlans'


class Tmp(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    vlan_id = models.IntegerField(default=1)

    class Meta:
        db_table = 'tmp'
