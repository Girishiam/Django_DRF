"""
django command to wait for the database to be ready before running migrations or starting the server.

"""
import time
from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        "Entry point for the command."

        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                # Check if the database is available
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))