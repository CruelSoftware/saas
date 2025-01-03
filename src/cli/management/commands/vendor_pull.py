from typing import Any, Sequence, Mapping

from django.conf import settings
from django.core.management import BaseCommand

import helpers


STATICFILES_VENDOR_DIR = getattr(settings, "STATICFILES_VENDOR_DIR")
VENDOR_STATIC = {
    "flowbite.min.css": "https://cdn.jsdelivr.net/npm/flowbite@2.5.2/dist/flowbite.min.css",
    "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@2.5.2/dist/flowbite.min.js"
}

class Command(BaseCommand):

    def handle(self, *args: Sequence[Any], **options: Mapping[Any, Any]):
        self.stdout.write("Downloading vendor static files")
        completed = list()

        for name, url in VENDOR_STATIC.items():
            out_path = STATICFILES_VENDOR_DIR / name
            download_success = helpers.download_to_local(url, out_path)
            if download_success:
                completed.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f'Failed to download "{url}"')
                )
        if set(completed) == set(VENDOR_STATIC.values()):
            self.stdout.write(
                self.style.SUCCESS("Successfully updated all vendor static files")
            )
        else:
            self.stdout.write(
                self.style.WARNING("Some files were not updated")
            )