import logging
from django.core.management.base import BaseCommand
from django.conf import settings
from monitor.server import server_mainloop

logging.basicConfig(level=logging.DEBUG)


class Command(BaseCommand):
    args = ''
    help = 'Start a fake AARTFAAC imaging pipeline monitoring server'

    def handle(self, *args, **options):
        host = settings.AARTFAAC_HOSTS[0]['HOST']
        port = settings.AARTFAAC_HOSTS[0]['PORT']
        server_mainloop(host, port)