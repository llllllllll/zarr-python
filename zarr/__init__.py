# -*- coding: utf-8 -*-
# flake8: noqa
from __future__ import absolute_import, print_function, division


from zarr.core import Array
from zarr.creation import (empty, zeros, ones, full, array, empty_like, zeros_like,
                           ones_like, full_like, open_array, open_like, create)
from zarr.storage import (DictStore, MemoryStore, DirectoryStore, ZipStore, TempStore,
                          NestedDirectoryStore, DBMStore, LMDBStore, SQLiteStore,
                          LRUStoreCache, ABSStore, RedisStore, MongoDBStore)
from zarr.hierarchy import group, open_group, Group
from zarr.sync import ThreadSynchronizer, ProcessSynchronizer
from zarr.codecs import *
from zarr.convenience import (open, save, save_array, save_group, load, copy_store,
                              copy, copy_all, tree, consolidate_metadata,
                              open_consolidated)
from zarr.n5 import N5Store
from zarr.errors import CopyError, MetadataError, PermissionError
from zarr.version import version as __version__
