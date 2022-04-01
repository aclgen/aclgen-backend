from enum import Enum


class Protocol(Enum):
    """Enum: Protocol"""
    TCP = "TCP"
    UDP = "UDP"
    ICMP = "ICMP"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
