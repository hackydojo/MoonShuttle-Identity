import nacl.pwhash.argon2id
from app.interfaces.security import IdentityCredential


# ---------------------------------------------------------------------------------------
# CLASS PASSWORD
# ---------------------------------------------------------------------------------------
class Password(IdentityCredential):

    """
        Provides an abstractions on top of NaCl to provide a secure mechanism to store and
        verify passwords using Argon2 Key Derivation Function.
    """

    # -----------------------------------------------------------------------------------
    # CONSTRUCTOR
    # -----------------------------------------------------------------------------------
    def __init__(self, plain_text_password, salt):
        """

            :param plain_text_password:
            :param salt:
        """
        self.__salt = salt
        self.__pwd: bytes = self.__salt_password(
            plain_text_password,
            self.__salt
        )
        self.__hash = self.__compute_hash()

    # -----------------------------------------------------------------------------------
    # METHOD COMPUTE HASH
    # -----------------------------------------------------------------------------------
    def __compute_hash(self):
        return nacl.pwhash.argon2id.str(self.__pwd)

    # -----------------------------------------------------------------------------------
    # METHOD SALT PASSWORD
    # -----------------------------------------------------------------------------------
    @staticmethod
    def __salt_password(password: str, salt: str):
        """
            Concatenates a given salt value at the end of the password and convert the
            resulting string into bytes
            :param password: the password in plain text
            :param salt: the salt byte generated for this password
            :return:
        """
        return (password + salt).encode()

    # -----------------------------------------------------------------------------------
    # PROPERTY SALT
    # -----------------------------------------------------------------------------------
    @property
    def salt(self):
        """
            String representation of the salt bytes
            :return: A string representation of the salt bytes encoded in UFT-8
        """
        return self.__salt

    # -----------------------------------------------------------------------------------
    # PROPERTY PASSWORD HASH
    # -----------------------------------------------------------------------------------
    @property
    def password_hash(self) -> str:
        """
            String representation
            :return:
        """
        return self.__hash.decode()

    # -----------------------------------------------------------------------------------
    # METHOD VERIFY
    # -----------------------------------------------------------------------------------
    def verify(self, **kwargs):
        """
            Requires a keyword argument called stored_hash that contains the value of the
            stored hash from the original password. This allows verifying a given password
            without having to know the original value of the password.

            :param kwargs: key-word arguments as enforced by abstract class.
            :return: True is password is valid and false if password is not valid.
        """
        stored_hash = self.__get_stored_hash_from_arguments(kwargs).encode()
        return nacl.pwhash.argon2id.verify(
            stored_hash,
            self.__pwd
        )

    # -----------------------------------------------------------------------------------
    # METHOD GET STORED HASH FROM ARGUMENTS
    # -----------------------------------------------------------------------------------
    @staticmethod
    def __get_stored_hash_from_arguments(arguments: dict) -> str:
        """
            Checks if the required key stored_has is present in the dictionary and return
            its value if found.

            :param arguments: a dictionary that contains the key stored_hash
            :return: the value of the key stored_hash
        """
        if 'stored_hash' not in arguments.keys():
            raise ValueError('stored_hash is required')
        if not arguments['stored_hash']:
            raise ValueError('stored_hash cannot be an empty string')
        return arguments['stored_hash']

