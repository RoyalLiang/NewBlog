import enum


class StatusEnum(enum.IntEnum):
    DELETE = -1
    DRAFT = 0
    USED = 1


class LabelEnum(enum.IntEnum):
    TAG = 1
    CATEGORY = 2


class ResponseCodeEnum(enum.IntEnum):
    SYS_ERROR = -10000
    SUCCESS = 10000


class VoteTypeEnum(enum.IntEnum):
    LIKE = 1
    DISLIKE = -1
