import json
import os
import sqlite3
from objects.login_object import LoginObject
from objects.login_result_object import LoginResultObject
from utils.singelton_base import SingletonBase  # Example database library;

# DataSource 
# implements a Singleton Design pattern
# return JSON data either from a file or from a database
# Singleton will ensure only one instance of the data source is created and reused throughout the application.
# 
class DataSource(SingletonBase):

    def _initialize(self,path):
        # Load JSON objects from the file or Database - configuration im .env 
        self.source_type = os.getenv("TEST_DATA_SOURCE_TYPE", "file")
        self.db_config = {"database": "test_data.db"}
        self.data = None
        self.file_path = path

        if self.source_type == "file" and self.file_path:
            self.data = self._load_data_from_file()
        elif self.source_type == "database" and self.db_config:
            self.data = self._load_data_from_database()

    def _load_data_from_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def _load_data_from_database(self):
        conn = sqlite3.connect(self.db_config['database'])
        cursor = conn.cursor()
        cursor.execute("SELECT json_data FROM test_data_table WHERE id=1")  # Example query; adjust as needed
        row = cursor.fetchone()
        conn.close()
        if row:
            return json.loads(row[0])
        return None 
    
    def get_data(self):
        return self.data  
 
class LoginObjectDataSource(DataSource):
    def _initialize(self):
        path =  os.getenv("TEST_DATA_LOGIN_OBJECT_FILE_PATH", "data/test_data.json")
        super()._initialize(path)
        # You can add any user-specific initialization here
     
    def get_data(self):
        return LoginObject.from_json(self.data)  
    
    def get_data_json(self):
        return self.data 


class LoginResultObjectDataSource(DataSource):
    def _initialize(self):
        path =  os.getenv("TEST_DATA_LOGIN_RESULT__OBJECT_FILE_PATH", "data/test_result_expected_data.json")
        super()._initialize(path)
        # You can add any group-specific initialization here

    def get_data(self):
        return LoginResultObject.from_json(self.data)  