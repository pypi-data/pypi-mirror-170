from __future__ import annotations

from urllib.parse import urlparse, urlunparse

from airflow.providers.google.cloud.hooks.gcs import GCSHook
from astro.constants import FileLocation
from astro.files.locations.base import BaseFileLocation


class GCSLocation(BaseFileLocation):
    """Handler GS object store operations"""

    location_type = FileLocation.GS

    @property
    def hook(self) -> GCSHook:
        return GCSHook(gcp_conn_id=self.conn_id) if self.conn_id else GCSHook()

    @property
    def transport_params(self) -> dict:
        """get GCS credentials for storage"""
        client = self.hook.get_conn()
        return {"client": client}

    @property
    def paths(self) -> list[str]:
        """Resolve GS file paths with prefix"""
        url = urlparse(self.path)
        bucket_name = url.netloc
        prefix = url.path[1:]
        prefixes = self.hook.list(bucket_name=bucket_name, prefix=prefix)
        paths = [
            urlunparse((url.scheme, url.netloc, keys, "", "", "")) for keys in prefixes
        ]
        return paths

    @property
    def size(self) -> int:
        return -1
