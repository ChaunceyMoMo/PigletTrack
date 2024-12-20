# Mikel Broström 🔥 Yolo Tracking 🧾 AGPL-3.0 license

__version__ = '10.0.51'

from boxmot.tracker_zoo import create_tracker, get_tracker_config
from boxmot.trackers.pigletsort.piglet_sort import PigletSORT

TRACKERS = ['piglettrack']

__all__ = ("__version__", 'PigletSORT')
