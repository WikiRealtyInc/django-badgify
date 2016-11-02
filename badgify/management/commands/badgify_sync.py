# -*- coding: utf-8 -*-
from optparse import make_option

from django.core.management.base import LabelCommand, CommandError

from badgify import commands
from badgify.utils import sanitize_command_options


class Command(LabelCommand):
    """
    Command that synchronizes badges, awards and counts.
    """
    help = u'Synchronizes badges, awards and counts.'

    def add_arguments(self, parser):
        parser.add_argument('args', metavar=self.label, nargs='+')
        parser.add_argument("-b", "--badges", type=str, dest="badges", action="store")
        parser.add_argument("-db", "--db-read", action="store", dest="db_read", type=str)
        parser.add_argument("-ds", "--disable-signals", action="store_true", dest="disable_signals")
        parser.add_argument("-bs", "--batch-size", action="store", dest="batch_size", type=int)
        parser.add_argument("-u", "--update", action="store_true", dest="update")
        parser.add_argument("-x", "--exclude-badges", action="store", dest="exclude_badges", type=str)


    def handle_label(self, label, **options):
        options = sanitize_command_options(options)

        if not hasattr(commands, 'sync_%s' % label):
            raise CommandError('"%s" is not a valid command.' % label)

        getattr(commands, 'sync_%s' % label)(**options)
