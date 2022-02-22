import enum


class StatusEnum(enum.IntEnum):
    DELETE = -1
    DRAFT = 0
    USED = 1


class LabelEnum(enum.IntEnum):
    TAG = 1
    CATEGORY = 2
