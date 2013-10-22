import logging
from django.core.management.base import BaseCommand
from django.conf import settings
from monitor.client import client_mainloop

logging.basicConfig(level=logging.DEBUG)


class Command(BaseCommand):
    args = ''
    help = 'Start an AARTFAAC imaging pipeline monitoring client'

    def handle(self, *args, **options):
        host = settings.AARTFAAC_HOSTS[0]['HOST']
        port = settings.AARTFAAC_HOSTS[0]['PORT']
        client_mainloop(host, port)