from enum import Enum


class Direction(Enum):
    """Enum: Direction value for rules"""
    INBOUND = 1
    OUTBOUND = 2


class Policy(Enum):
    """Enum: Policy value for rules"""
    ACCEPT = 1
    DENY = 2

