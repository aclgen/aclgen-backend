from enum import Enum


class Protocol(Enum):
    TCP = "TCP"
    UDP = "UDP"
    ICMP = "ICMP"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class DeviceType(Enum):
    FIREWALL = "FIREWALL"
    CLUSTER = "CLUSTER"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class RuleDirection(Enum):
    INBOUND = "INBOUND"
    OUTBOUND = "OUTBOUND"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class RuleAction(Enum):
    ACCEPT = "ACCEPT"
    DENY = "DENY"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)