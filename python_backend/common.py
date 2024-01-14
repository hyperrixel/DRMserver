#############
# CONSTANTS #
#############


KEY_ERROR = 'error'
KEY_RESULT = 'result'


########################
# ENUM ALIKE CONSTANTS #
########################


class EncryptionAlgorithm:


    AES_CBC = 'aes-cbc'
    AES_CTR = 'aes-ctr'


class EncryptionDepth:


    BIT_128 = 16
    BIT_256 = 32


class EncryptionGenerator:


    RANDOM = 0
    FIXED = 1
    FROM_COLLECTION = 2


class ProtectionType:


    CUSTOM = 'custom'
    DRM_BASE = 'drm_base'
    FAIR_PLAY = 'fair_play'
    PLAY_READY = 'play_ready'
    WIDEVINE = 'widevine'


class Status:


    NON_EXISTING = 0
    DELETED = 1
    SUSPENDED = 2
    ACTIVE = 3


class StreamAccess:


    NOT_ACCESSIBLE = 0
    OPEN = 1
    RESTRICTED_WITHOUT_SUBSCRIPTION = 2
    FREE_FOR_SUBSCRIBE = 3
    RESTRICTED_WITH_SUBSCRIPTION = 2


class StreamRestrictionBase:


    NO_RESTRICTION = 0
    TIME_BASED = 1
    COUNT_BASED = 2
    GEOLOCATION_BASED = 4


class StreamType:


    DASH_CMAF = 'dash_cmaf'
    HLS = 'hls'
    MULTIPART = 'multipart'
    RTMP = 'rtmp'
    RTSP = 'rtsp'
    SRT = 'srt'
    WebRTC = 'web_rtc'


#####################
# MID-LEVEL CLASSES #
#####################


class AntMediaStream:


    def __init__(self, name : str, status : int, stream_type : int) -> None:

        if not const_exists(status, Status):
            raise ValueError('AntMediaStream() init: Unknown stream status.')
        if not const_exists(stream_type, StreamType):
            raise ValueError('AntMediaStream() init: Unknown stream type.')
        self.__name = name
        self.__status = status
        self.__stream_type = stream_type


    @staticmethod
    def from_dict(data : dict) -> any:

        if not AntMediaStream.has_all_keys(data):
            raise KeyError('AntMediaStream.from_dict(): Missing key(s).')
        return AntMediaStream(data['name'], data['status'], data['stream_type'])


    @staticmethod
    def has_all_keys(data : dict) -> bool:

        return all_keys_set(data, ['name', 'status', 'stream_type'])


    @property
    def name(self) -> str:

        return self.__name


    @name.setter
    def name(self, new_value : str) -> None:

        self.__name = new_value


    @property
    def status(self) -> int:

        return self.__status


    @status.setter
    def status(self, new_value : int) -> None:

        if not const_exists(new_value, Status):
            raise ValueError('AntMediaStream() set status: Unknown stream status.')
        self.__status = new_value


    @property
    def stream_type(self) -> int:

        return self.__stream_type


    @stream_type.setter
    def stream_type(self, new_value : int) -> None:

        if not const_exists(new_value, StreamType):
            raise ValueError('AntMediaStream() set stream type: Unknown stream type.')
        self.__stream_type = new_value


class StreamAccess:


    def __init__(self) -> None:

        pass


    @staticmethod
    def from_dict(data : dict) -> any:

        pass


    @staticmethod
    def has_all_keys(data : dict) -> bool:

        return all_keys_set(data, [])


class StreamStatistics:


    def __init__(self) -> None:

        pass


    @staticmethod
    def from_dict(data : dict) -> any:

        pass


    @staticmethod
    def has_all_keys(data : dict) -> bool:

        return all_keys_set(data, [])


class UserCredentials:

    def __init__(self) -> None:

        pass


    @staticmethod
    def from_dict(data : dict) -> any:

        pass


    @staticmethod
    def has_all_keys(data : dict) -> bool:

        return all_keys_set(data, [])


class UserPaymentInformation:

    def __init__(self) -> None:

        pass


    @staticmethod
    def from_dict(data : dict) -> any:

        pass


    @staticmethod
    def has_all_keys(data : dict) -> bool:

        return all_keys_set(data, [])


class UserStatistics:

    def __init__(self, registered : int, streams_count : int,
                 views_count : int) -> None:

        self.__registered = registered
        self.__streams_count = streams_count
        self.__views_count = views_count


    @staticmethod
    def from_dict(data : dict) -> any:

        if not UserStatistics.has_all_keys(data):
            raise KeyError('UserStatistics.from_dict(): Missing key(s).')
        return UserStatistics(data['registered'], data['streams_count'],
                              data['views_count'])


    @staticmethod
    def has_all_keys(data : dict) -> bool:

        return all_keys_set(data, ['registered', 'streams_count', 'views_count'])


    @property
    def registered(self) -> int:

        return self.__registered


    @registered.setter
    def registered(self, new_value) -> None:

        self.__registered = new_value


    @property
    def streams_count(self) -> int:

        return self.__streams_count


    @streams_count.setter
    def streams_count(self, new_value : int) -> None:

        self.__streams_count = new_value


    @property
    def views_count(self) -> int:

        return self.__views_count


    @views_count.setter
    def views_count(self, new_value : int) -> None:

        self.__views_count = new_value


#####################
# TOP-LEVEL CLASSES #
#####################


class Stream:


    def __init__(self, name : str, ams_stream : AntMediaStream, status : int,
                 statistics : StreamStatistics, access : StreamAccess) -> None:

        if not const_exists(status, Status):
            raise ValueError('Stream() init: Unknown stream status.')
        self.__name = name
        self.__ams_stream = ams_stream
        self.__status = status
        self.__statistics = statistics
        self.__access = access


    @property
    def access(self) -> StreamAccess:

        return self.__access


    @property
    def ams_stream(self) -> AntMediaStream:

        return self.__ams_stream


    @staticmethod
    def from_dict(data : dict) -> any:

        if not Stream.has_all_keys(data):
            raise KeyError('Stream.from_dict(): Missing key(s).')
        return Stream(data['name'], AntMediaStream.from_dict(data['ams_stream']),
                      data['status'], UserStatistics.from_dict(data['statistic']),
                      StreamAccess.from_dict(data['access']))


    @staticmethod
    def has_all_keys(data : dict) -> bool:

        return all_keys_set(data, ['access', 'ams_stream', 'name', 'statistics',
                                   'status'])


    @property
    def name(self) -> str:

        return self.__name


    @name.setter
    def name(self, new_value : str) -> None:

        self.__name = new_value


    @property
    def statistics(self) -> StreamStatistics:

        return self.__statistics


    @property
    def status(self) -> int:

        return self.__status


    @status.setter
    def status(self, new_value : int) -> None:

        if not const_exists(new_value, Status):
            raise ValueError('Stream() set status: Unknown stream status.')
        self.__status = new_value


class User:


    def __init__(self, user_id : str, status : int,
                 credentials : UserCredentials, payment : UserPaymentInformation,
                 statistics : UserStatistics) -> None:

        if not const_exists(status, Status):
            raise ValueError('User() init: Unknown user status.')
        self.__user_id = user_id
        self.__status = status
        self.__credentials = credentials
        self.__payment = payment
        self.__statistics = statistics


    @property
    def credentials(self) -> UserCredentials:

        return self.__credentials


    @staticmethod
    def from_dict(data : dict) -> any:

        if not User.has_all_keys(data):
            raise KeyError('User.from_dict(): Missing key(s).')
        return User(data['user_id'], data['status'],
                    UserCredentials.from_dict(data['credentials']),
                    UserPaymentInformation.from_dict(data['payment']),
                    UserStatistics.from_dict('statistics'))


    @staticmethod
    def has_all_keys(data : dict) -> bool:

        return all_keys_set(data, ['credentials', 'payment', 'statistics',
                                   'status', 'user_id'])


    @property
    def payment(self) -> UserPaymentInformation:

        return self.__payment


    @property
    def statistics(self) -> UserStatistics:

        return self.__statistics


    @property
    def status(self) -> int:

        return self.__status


    @status.setter
    def status(self, new_value : int) -> None:

        if not const_exists(new_value, Status):
            raise ValueError('User() set status: Unknown user status.')
        self.__status = new_value


    @property
    def user_id(self) -> str:

        return self.__user_id


    @user_id.setter
    def user_id(self, new_value : str) -> None:

        self.__user_id = new_value


#############
# FUNCTIONS #
#############


def all_keys_set(data : dict, keys : list) -> bool:

    return all([k in data for k in keys])


def const_exists(key : str, source : any) -> bool:

    if not key.isupper(): return False
    return key in [k for k in dir(source) if k.find('__') == -1]


def error_response(text : str) -> dict:

    result_ = get_result_template()
    result_[KEY_ERROR] = text
    return result_


def get_result_template() -> dict:

    return {KEY_RESULT : None, KEY_ERROR : None}


def success_response(data : any) -> dict:

    result_ = get_result_template()
    result_[KEY_RESULT] = data
    return result_