#!/usr/bin/env python
"""Load all blob stores so that they are visible in the registry."""

# pylint: disable=g-import-not-at-top,unused-import

# The memory stream object based blob store.
from grr.lib.blob_stores import memory_stream_bs
