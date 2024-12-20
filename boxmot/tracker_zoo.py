# Mikel Broström 🔥 Yolo Tracking 🧾 AGPL-3.0 license

from types import SimpleNamespace

import yaml

from boxmot.utils import BOXMOT


def get_tracker_config(tracker_type):
    tracking_config = \
        BOXMOT /\
        'configs' /\
        (tracker_type + '.yaml')
    return tracking_config


def create_tracker(tracker_type, tracker_config, reid_weights, device, half, per_class):

    with open(tracker_config, "r") as f:
        cfg = yaml.load(f.read(), Loader=yaml.FullLoader)
    cfg = SimpleNamespace(**cfg)  # easier dict acces by dot, instead of ['']
    if tracker_type == 'piglettrack':
        from boxmot.trackers.pigletsort.piglet_sort import PigletSORT
        pigletsort = PigletSORT(
            track_thresh=cfg.track_thresh,
            match_thresh=cfg.match_thresh,
            track_buffer=cfg.track_buffer,
            frame_rate=cfg.frame_rate,
            nms_thresh=cfg.nms_thresh,
        )
        return pigletsort
    else:
        print('No such tracker')
        exit()