# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

# Badges (and color lookup)
# The color needs to follow a # that is converted to %23

BADGE_COLORS = {"submission":"green",
                "experiment": "%23eaab1b",
                "builder": "orange",
                "openbases": "%232196f3",
                "testing": "%23783589",
                "data": "red",
                "library": "%23ff69b4",
                "resource": "blue",
                "paper": "%231ab170",
                "other": "lightgrey" }

# brightgreen and blue still not used

BADGE_STYLES = ["plastic",
                "flat",
                "flat-square",
                "for-the-badge",
                "popout",
                "popout-square",
                "social"]


BADGE_LABELS = list(BADGE_COLORS.keys())

# https://img.shields.io/badge/<SUBJECT>-<STATUS>-<COLOR>.sv

BADGE_BASE = "https://img.shields.io/badge/%s-%s-%s.svg"
