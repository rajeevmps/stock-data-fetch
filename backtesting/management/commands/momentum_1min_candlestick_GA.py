from django.core.management.base import BaseCommand
from backtesting.momentum_1min_candle.optimisation.genetic_algorithm import main


class Command(BaseCommand):
    def handle(self, *args, **options):
        main()
