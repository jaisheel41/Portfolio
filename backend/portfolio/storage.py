"""Supabase Storage (S3-compatible) backend for uploaded media."""

from __future__ import annotations

from storages.backends.s3boto3 import S3Boto3Storage


class PublicSupabaseS3Storage(S3Boto3Storage):
    """
    Store files in a Supabase bucket using the S3 protocol.

    Supabase public object URLs differ from the default S3-style URL boto3 returns.
    Set ``SUPABASE_STORAGE_PUBLIC_BASE`` in Django settings to the public base URL
    from the Supabase dashboard (bucket must allow public read for those URLs).
    """

    def url(self, name, parameters=None, expire=None, http_method=None):
        from django.conf import settings

        base = (getattr(settings, "SUPABASE_STORAGE_PUBLIC_BASE", "") or "").rstrip("/")
        if base:
            clean = self._normalize_name(self.clean_name(name))
            return f"{base}/{clean}"
        return super().url(name, parameters, expire, http_method)
