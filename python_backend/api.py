from json import dumps as json_dumps
from requests import request
from time import sleep

from .common import error_response, success_response


HEADERS = {'accept' : 'application/json'}
QUERY_FAIL_SLEEP = 30
QUERY_FAIL_TRIES_COUNT = 5


class AMSHandler:


    def __init__(self, address : str, port : int, application : str,
                 user : any = None, password : any = None) -> None:

        if not isinstance(user, (str, None, )):
            raise TypeError('AMSHandler() init: Invalid user name type.')
        if not isinstance(password, (str, None, )):
            raise TypeError('AMSHandler() init: Invalid user name type.')
        self.__address = address
        self.__port = port
        self.__application = application
        self.__user = user
        self.__password = password


    @property
    def address(self) -> str:

        return self.__address


    @property
    def application(self) -> str:

        return self.__application


    def get(self, endpoint : any, method : str, data : any = None,
            failure_sleep : int = QUERY_FAIL_SLEEP,
            tries_count : int = QUERY_FAIL_TRIES_COUNT, url : any = None) -> dict:

        method_ = method.upper()
        if method_ not in ['DELETE', 'GET', 'POST', 'PUT']:
            return error_response(f'Unsupported Ant Media Server API method "{method_}".')
        if url is None:
            if isinstance(endpoint, str): url_ = f'http://{self.__address}:{self.__port}/{self.__application}/rest/v2/{endpoint}'
            elif isinstance(endpoint, list): url_ = f'http://{self.__address}:{self.__port}/{self.__application}/rest/v2/{"/".join(endpoint)}'
            else: return error_response(f'Invalid endpoint data type "{type(endpoint)}".')
            if method_ != 'POST' and isinstance(data, list):
                url_ += "/".join(data)
        else:
            url_ = url
        if method_ == 'POST':
            json_ = data
        else:
            json_ = None
        do_loop_ = True
        try_count_ = 0
        response_data_ = None
        while do_loop_:
            try_count_ += 1
            handler_ = request(method_, url_, headers=HEADERS, json=json_)
            if handler_.status_code == 200:
                try:
                    response_data_ = handler_.json()
                    do_loop_ = False
                except Exception:
                    if try_count_ > tries_count:
                        do_loop_ = False
                    else:
                        sleep(failure_sleep)
            else:
                return error_response(f'Failed with response status code {handler_.status_code}')
        if response_data_ is None:
            return error_response('API connection failed permanently.')
        return success_response(response_data_)


    @property
    def password(self) -> any:

        return self.__password


    @property
    def port(self) -> int:

        return self.__port


    @property
    def user(self) -> any:

        return self.__user


def main():

    pass


if __name__ == '__main__':
    main()