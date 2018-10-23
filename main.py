import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'vlanSync.settings'
import django

django.setup()

from sync.SyncHandler import SyncHandler
from sync.models import LocalVlans, RemoteVlans, Tmp


def main():

    SyncHandler.startSync()


if __name__ == '__main__':
    main()
