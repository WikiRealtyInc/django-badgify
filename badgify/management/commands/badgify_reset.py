# -*- coding: utf-8 -*-
from optparse import make_option

from django.core.management.base import BaseCommand

from badgify.commands import reset_awards
from badgify.utils import sanitize_command_options


class Command(BaseCommand):
    """
    Commands that resets awards.
    """
    help = 'Resets awards.'

    def add_arguments(self, parser):
        parser.add_argument("-b", "--badges", action="store", dest="badges", type=str)
        parser.add_argument("-e", "--exclude-badges", action="store", dest="exclude_badges", type=str)


    def handle(self, *args, **options):
        options = sanitize_command_options(options)
        reset_awards(**options)
