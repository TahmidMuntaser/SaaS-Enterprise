from django.core.management.base import BaseCommand
from tenant_manager.models import Tenant, Domain


class Command(BaseCommand):
    help = "Creates a public tenant with domains for localhost and 127.0.0.1"

    def handle(self, *args, **options):
        # Check if a public tenant already exists
        if Tenant.objects.filter(schema_name="public").exists():
            self.stdout.write(self.style.WARNING("Public tenant already exists. Skipping creation."))
            return

        # Create the public tenant
        tenant = Tenant(
            schema_name="public",
            name="Public Tenant",
        )
        tenant.save()

        # Add domains for localhost and 127.0.0.1
        for domain in ["localhost", "127.0.0.1"]:
            Domain.objects.create(
                domain=domain,
                tenant=tenant,
                is_primary=(domain == "localhost"),
            )

        self.stdout.write(self.style.SUCCESS("Successfully created public tenant with domains: localhost, 127.0.0.1"))