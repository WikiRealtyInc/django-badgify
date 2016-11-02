# -*- coding: utf-8 -*-
from optparse import make_option

from django.core.management.base import BaseCommand

from badgify.commands import show_stats


class Command(BaseCommand):
    """
    Commands that shows badge stats.
    """
    help = 'Shows badge stats.'

    def add_arguments(self, parser):
        parser.add_argument("-d", "--db-read", type=str, dest="db_read", action="store")

    def handle(self, *args, **options):
        show_stats(**options)
