from .models import LocalVlans, RemoteVlans, Tmp


class SyncHandler:

    def __init__(self):
        pass

    def create(self, vlan_model1, vlan_model2):
        if vlan_model1.objects.count() > Tmp.objects.count() and Tmp.objects.count() == vlan_model2.objects.count():
            vlans = vlan_model1.objects.all()
            [Tmp(id=v.id, name=v.name, description=v.description).save() for v in vlans]
        if Tmp.objects.count() > vlan_model2.objects.count() and Tmp.objects.count() == vlan_model1.objects.count():
            vlan = Tmp.objects.all()
            [vlan_model2(id=v.id, name=v.name, description=v.description).save() for v in vlan]

    def delete(self, vlan_model1, vlan_model2):
        if vlan_model1.objects.count() < Tmp.objects.count() and Tmp.objects.count() == vlan_model2.objects.count():
            vlan_list = vlan_model1.objects.all()
            tmpVlans = Tmp.objects.all()

            local = set()
            tmp = set()

            [local.add(i.id) for i in vlan_list]
            [tmp.add(i.id) for i in tmpVlans]

            inter = local.intersection(tmp)

            print("Vlans should be delete from tmp Vlan")
            l = tmp - inter
            print(l)
            [Tmp.delete(Tmp.objects.get(id=i)) for i in l]

        if Tmp.objects.count() < vlan_model2.objects.count() and vlan_model1.objects.count() == Tmp.objects.count():
            localVlans = vlan_model2.objects.all()
            tmpVlans = Tmp.objects.all()

            local = set()
            tmp = set()

            [local.add(i.id) for i in localVlans]
            [tmp.add(i.id) for i in tmpVlans]

            inter = local.intersection(tmp)

            print("Vlans should be delete from tmp Vlan")
            l = local - inter
            print(l)
            [vlan_model2.delete(vlan_model2.objects.get(id=i)) for i in l]

    def update(self, vlan_model1, vlan_model2):
        tmps = Tmp.objects.all()
        for index,row in enumerate(vlan_model1.objects.all()):
            if row != tmps[index]:
                updated = tmps[index]
                updated.vlan_id = row.vlan_id
                updated.name = row.name
                updated.description = row.description
                updated.save()
                vlan_model_ = vlan_model2.objects.all()[index]
                vlan_model_.vlan_id = updated.vlan_id
                vlan_model_.name = updated.name
                vlan_model_.description = updated.description
                vlan_model_.save()









    @staticmethod
    def startSync():
        sycher = SyncHandler()

        while True:
            sycher.create(LocalVlans, RemoteVlans)
            sycher.delete(LocalVlans, RemoteVlans)
            sycher.update(LocalVlans, RemoteVlans)

            sycher.create(RemoteVlans, LocalVlans)
            sycher.delete(RemoteVlans, LocalVlans)
            sycher.update(RemoteVlans, LocalVlans)

