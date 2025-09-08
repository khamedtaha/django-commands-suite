from django.core.management.base import BaseCommand
from django_commands_suite import subcommands

class Command(BaseCommand):
    help = "Run django-commands-suite subcommands"

    def add_arguments(self, parser):
        parser.add_argument("subcommand", help="Subcommand to run")
        parser.add_argument("args", nargs="*", help="Arguments for the subcommand")

        subparsers = parser.add_subparsers(dest="subcommand_name")
        for name, sub in subcommands.registry.items():
            sub_parser = subparsers.add_parser(name)
            if hasattr(sub, "add_arguments"):
                sub.add_arguments(sub_parser)

    def handle(self, *args, **options):
        subcommand = options["subcommand"]
        sub = subcommands.registry.get(subcommand)
        if not sub:
            self.stderr.write(self.style.ERROR(f"Unknown subcommand: {subcommand}"))
            return

        result = sub.run(*args, **options)
        if result:
            self.stdout.write(self.style.SUCCESS(str(result)))
