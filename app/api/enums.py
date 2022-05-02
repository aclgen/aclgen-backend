from enum import Enum


class Protocol(str, Enum):
    TCP = "TCP"
    UDP = "UDP"
    ICMP = "ICMP"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class DeviceType(str, Enum):
    FIREWALL = "FIREWALL"
    CLUSTER = "CLUSTER"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class RuleDirection(str, Enum):
    INBOUND = "INBOUND"
    OUTBOUND = "OUTBOUND"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class RuleAction(str, Enum):
    ACCEPT = "ACCEPT"
    DENY = "DENY"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class LockStatus(str, Enum):
    LOCKED = "LOCKED"
    UNLOCKED = "UNLOCKED"
    IMMUTABLE = "IMMUTABLE"

    @classmethod
    def choices(cls):
        return tuple((
            ("LOCKED", cls.LOCKED),
            ("UNLOCKED", cls.UNLOCKED)
        ))

    @classmethod
    def all(cls):
        return tuple((i.name, i.value) for i in cls)
