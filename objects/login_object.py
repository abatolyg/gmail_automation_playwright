# models/login_object.py
import logging
from utils.pwd_manager import PasswordManager
from utils.logger_config import logger  # Import the global logger

class LoginObject:
    def __init__(self, username: str, password_decrypted: str):
        self.username = username
        self.password = password_decrypted

    @classmethod
    def from_json(self, data: dict):
        return self(username=data['username'], password_decrypted=self.get_password_decrypted(data['password']))
    
    @staticmethod
    def get_password_decrypted(password_encripted):
       
        # Create an instance of PasswordManager
         password_manager = PasswordManager()

         if password_encripted:
            # Decrypt the password
            password_decrypted = password_manager.decrypt_password(password_encripted)
            #logger.info(f"Decrypted: {password_decrypted}")
            return password_decrypted    
         else:
            logger.info(f"Decrypted: {password_decrypted}")
            return password_decrypted