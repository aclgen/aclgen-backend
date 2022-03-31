from enum import Enum


class Direction(Enum):
    """Enum: Direction value for rules"""
    INBOUND = "INBOUND"
    OUTBOUND = "OUTBOUND"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class Action(Enum):
    """Enum: Policy value for rules"""
    ACCEPT = "ACCEPT"
    DENY = "DENY"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

