from django.test import TestCase
from .SyncHandler import SyncHandler
from .models import LocalVlans, RemoteVlans



class MyTest(TestCase):

    def setUp(self):
        l = LocalVlans(id=1, name="test1", description="dddd")
        l.save()
        lm = RemoteVlans(id=2, name="test5", description="dddddd")
        lm.save()








    def test_creaet(self):
        s = SyncHandler()

        s.create(LocalVlans, RemoteVlans)
        s.create(RemoteVlans, LocalVlans)

        self.assertEqual(LocalVlans.objects.count(), RemoteVlans.objects.count())

    def test_delete(self):
        s = SyncHandler()
        s.delete(LocalVlans, RemoteVlans)
        s.delete(RemoteVlans, LocalVlans)
        self.assertEqual(LocalVlans.objects.count(), RemoteVlans.objects.count())

    def test_update(self):
        re = RemoteVlans(id=1 , name= "moATH" , description= "fsidhwdfvnjsrfh")
        s = SyncHandler()
        s.update(LocalVlans,RemoteVlans)
        s.update(RemoteVlans,LocalVlans)
        if LocalVlans.objects.filter(id=re.id ,name= re.name, description=re.description).exists():
            self.assertEqual(LocalVlans.objects.values() , RemoteVlans.objects.values())


# Create your tests here.

