from django.core.management.base import LabelCommand
from yoppi.indexer.app import Indexer

from django.conf import settings as django_settings


try:
    settings = django_settings.INDEXER_SETTINGS
except KeyError:
    settings = {}


class Command(LabelCommand):
    args = '<server_address> [server_address [...]]'
    help = 'DEBUG COMMAND. Index the specified FTP server twice, making sure there are no unexpected changes'
    label = 'address'

    def __init__(self):
        super(Command, self).__init__()
        self.indexer = Indexer(**settings)

    def handle_label(self, address, **options):
        print 'First pass for "%s"' % address
        self.indexer.index(address)
        print 'Second pass for "%s"' % address
        _, _, to_insert, to_delete = self.indexer.index(address)
        assert not to_insert
        assert not to_delete
        print 'Oll Korrect for "%s"' % address
