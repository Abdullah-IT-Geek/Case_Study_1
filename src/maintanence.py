from serializable import Serializable
from database import DatabaseConnector
from datetime import datetime
from typing import Self

class Maintanence(Serializable):

    db_connector =  DatabaseConnector().get_table("maintanence")

    def __init__(self, device_id: str, price: int, start_date: datetime, end_date: datetime, creation_date: datetime = None, last_update: datetime = None, id: str = None) -> None:

        if not id:
            id = F"{device_id}_{price}_{start_date}"

        super().__init__(id, creation_date, last_update)
        self.device_id = device_id
        self.price = price
        self.start_date = start_date
        self.end_date = end_date
        
    @classmethod
    def instantiate_from_dict(cls, data: dict) -> Self:
        return cls(data['device_id'], data['price'], data['start_date'], data['end_date'], data['creation_date'], data['last_update'], data['id'])

    def __str__(self):
        return F"Maintanence: for {self.device_id}€: costs {self.price}: {self.start_date} - {self.end_date}"

if __name__ == "__main__":
    # Create a device
    maintanence1 = Maintanence("one@mci.edu", "Device1", "2021-01-01 00:00:00", "2021-01-02 00:00:00")
    maintanence2 = Maintanence("one@mci.edu", "Device2", "2021-01-01 00:00:00", "2021-01-02 00:00:00")
    maintanence3 = Maintanence("two@mci.edu", "Device2", "2021-01-02 00:00:00", "2021-01-03 00:00:00")


    maintanence1.store_data()
    maintanence2.store_data()
    maintanence3.store_data()

    loaded_maintanence = Maintanence.find_by_attribute("device_id", "Device2", num_to_return=-1)
    if loaded_maintanence:
        for loaded_maintanence in loaded_maintanence:
            print(f"Loaded: {loaded_maintanence}")
    else:
        print("Maintanence not found.")