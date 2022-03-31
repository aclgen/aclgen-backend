from enum import Enum


class Direction(Enum):
    """Enum: Direction value for rules_old"""
    INBOUND = 1
    OUTBOUND = 2


class Policy(Enum):
    """Enum: Policy value for rules_old"""
    ACCEPT = 1
    DENY = 2

