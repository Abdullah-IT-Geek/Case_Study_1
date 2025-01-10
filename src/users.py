import os

from tinydb import TinyDB, Query
from serializer import serializer


class User():
    # Class variable that is shared between all instances of the class
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('user')

    # Constructor
    def __init__(self, user_name : str, user_email : str):
        self.user_name = user_name
        # The user id of the user that manages the device
        # We don't store the user object itself, but only the id (as a key)
        self.user_id = user_email
        
    # String representation of the class
    def __str__(self):
        return f'User (Object) {self.user_name} ({self.user_id})'

    # String representation of the class
    def __repr__(self):
        return self.__str__()
    
    def store_data(self):
        print("Storing data...")
        # Check if the device already exists in the database
        UserQuery = Query()
        result = self.db_connector.search(UserQuery.user_name == self.user_name)
        if result:
            # Update the existing record with the current instance's data
            result = self.db_connector.update(self.__dict__, doc_ids=[result[0].doc_id])
            print("Data updated.")
        else:
            # If the device doesn't exist, insert a new record
            self.db_connector.insert(self.__dict__)
            print("Data inserted.")
    
    def delete(self):
        print("Deleting data...")
        # Check if the device exists in the database
        UserQuery = Query()
        result = self.db_connector.search(UserQuery.user_name == self.user_name)
        if result:
            # Delete the record from the database
            self.db_connector.remove(doc_ids=[result[0].doc_id])
            print("Data deleted.")
        else:
            print("Data not found.")

    # Class method that can be called without an instance of the class to construct an instance of the class
    @classmethod
    def find_by_attribute(cls, by_attribute: str, attribute_value: str, num_to_return=1):
        # Load data from the database and create an instance of the Device class
        UserQuery = Query()
        result = cls.db_connector.search(UserQuery[by_attribute] == attribute_value)

        if result:
            data = result[:num_to_return]
            user_results = [cls(d['user_name'], d['user_id']) for d in data]
            return user_results if num_to_return > 1 else user_results[0]
        else:
            return None

    @classmethod
    def find_all(cls) -> list:
        # Load all data from the database and create instances of the Device class
        users = []
        for user_data in User.db_connector.all():
            users.append(User(user_data['user_name'], user_data['user_id']))
        return users



    

if __name__ == "__main__":
    # Create a device
    user1 = User("User1", "one@mci.edu")
    user2 = User("User2", "two@mci.edu") 
    user3 = User("User3", "three@mci.edu") 
    user4 = User("User4", "four@mci.edu") 
    user1.store_data()
    user2.store_data()
    user3.store_data()
    user4.store_data()
    user5 = User("User3", "user3@mci.edu") 
    user5.store_data()

    #loaded_device = Device.find_by_attribute("device_name", "Device2")
    loaded_device = User.find_by_attribute("user_id", "two@mci.edu")
    if loaded_device:
        print(f"Loaded User: {loaded_device}")
    else:
        print("User not found.")

    users = User.find_all()
    print("All users:")
    for user in users:
        print(user)

    
