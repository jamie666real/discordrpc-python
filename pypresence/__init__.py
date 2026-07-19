"""
Python RPC Client for Discord
-----------------------------
By: jamie666real
"""

from .baseclient import BaseClient
from .client import AioClient, Client
from .exceptions import *
from .presence import AioPresence, Presence
from .types import ActivityType, StatusDisplayType

__title__ = "pypresence"
__author__ = "jamie666real"
__copyright__ = "Copyright 2018 - Current jamie666real"
__license__ = "MIT"
__version__ = "4.6.2"