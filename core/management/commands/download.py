#! encoding:utf-8
from django.core.management import BaseCommand
from argparse import ArgumentParser


class Command(BaseCommand):
    help = u"下载数据并存入数据库"

    def add_arguments(self, parser):
        """

        :param parser:
        :type parser: ArgumentParser
        :return:
        """
        super(Command, self).add_arguments(parser)

        parser.add_argument('--get_stock_basics', action='store_true', default=False,
                            dest='get_stock_basics', help='download get_stock_basics and save')

    def handle(self, *args, **options):
        if options['get_stock_basics']:
            print True
