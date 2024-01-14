from os import urandom

from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CBC, CTR

class Cryptographer:
    
    def __init__(self, algorithm : str, algorithm_depth : int, mode : str,
                 nonce_depth : int, fixed_nonce : bool = True, key : any = None,
                 nonce : any = None) -> None:

        algorithm_ = algorithm.upper()
        if algorithm_ not in ['AES']:
            raise NotImplementedError(f'Cryptographer() init: algorithm "{algorithm_}" not yet implemented or don\'t exist.')
        mode_ = mode.upper()
        if mode_ not in ['CBC', 'CTR']:
            raise NotImplementedError(f'Cryptographer() init: mode "{mode_}" not yet implemented or don\'t exist.')
        if algorithm_depth not in [128, 256]:
            raise ValueError(f'Cryptographer() init: algorithm depth "{algorithm_depth}" is not supported.')
        if algorithm_depth % 8 != 0:
            raise ValueError(f'Cryptographer() init: algorithm depth "{algorithm_depth}" is invalid.')
        if nonce_depth not in [128, 256]:
            raise ValueError(f'Cryptographer() init: nonce depth "{algorithm_depth}" is not supported.')
        if nonce_depth % 8 != 0:
            raise ValueError(f'Cryptographer() init: nonce depth "{algorithm_depth}" is invalid.')
        if not isinstance(key, (str, bytes, None, )):
            raise TypeError(f'Cryptographer() init: nonce value has invalid data type "{type(nonce)}".')
        if not isinstance(nonce, (str, bytes, None, )):
            raise TypeError(f'Cryptographer() init: nonce value has invalid data type "{type(nonce)}".')
        if fixed_nonce is True and nonce is None:
            raise ValueError('Cryptographer() init: dubious nonce settings.')
        elif fixed_nonce is False and nonce is not None:
            raise ValueError('Cryptographer() init: dubious nonce settings.')
        self.__algorithm = algorithm_
        self.__mode = mode_
        self.__algorithm_depth = algorithm_depth
        self.__nonce_depth = nonce_depth
        self.__fixed_nonce = fixed_nonce
        if key is None:
            self.__key = urandom(self.__algorithm_depth % 8)
        else:
            self.__key = key
        if nonce is None:
            self.__nonce = urandom(self.__nonce_depth % 8)
        else:
            self.__nonce = nonce
        if self.__mode == 'CBS':
            self.__engine = Cipher(AES(self.__key), CBC(self.__nonce))
        elif self.__mode == 'CTR':
            self.__engine = Cipher(AES(self.__key), CTR(self.__nonce))


    @property
    def algorithm(self) -> str:

        return self.__algorithm


    @property
    def algorithm_depth(self) -> int:

        return self.__algorithm_depth


    @property
    def engine(self) -> any:

        return self.__engine


    @property
    def fixed_nonce(self) -> bool:

        return self.__fixed_nonce


    @property
    def key(self) -> bytes:

        return self.__key


    @property
    def mode(self) -> str:

        return self.__mode


    @property
    def nonce(self) -> bytes:

        return self.__nonce


    @property
    def nonce_depth(self) -> int:

        return self.__nonce_depth
