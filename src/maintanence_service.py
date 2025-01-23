from maintanence import Maintanence
from devices import Device
from users import User


class MaintanenceService():

    def __init__(self) -> None:
        self.find_all_maintanence()

    def find_all_maintanence(cls) -> list[Maintanence]:
        cls.maintanences = Maintanence.find_all()
        return cls.maintanences

    def find_all_maintanence_by_price(cls, price: str) -> list[Maintanence]:
        return [maintanence for maintanence in cls.maintanences if maintanence.price == price]
    
    def find_all_reservations_by_device_id(cls, device_id: str) -> list[Maintanence]:
        return [maintanence for maintanence in cls.maintanences if maintanence.device_id == device_id]    
    
    def find_all_reservations_by_device_id_and_price(cls,device_id: str, price: str) -> list[Maintanence]:
        return [maintanence for maintanence in cls.maintanences if maintanence.device_id == device_id and maintanence.price == price]

    def check_conflict(cls, device_id: str, start_date: str, end_date: str) -> bool:
        for reservation in cls.maintanences:
            if reservation.device_id == device_id:
                if (start_date >= reservation.start_date and start_date <= reservation.end_date) or (end_date >= reservation.start_date and end_date <= reservation.end_date):
                    return True
        return False

    def device_exists(cls, device_id: str) -> bool:
        return Device.find_by_attribute("id", device_id) is not None
    
    def create_maintanence(cls, device_id: str, price: int, start_date: str, end_date: str) -> bool:
        
        if not cls.device_exists(device_id):
            raise ValueError("Device does not exist")
        
        if cls.check_conflict(device_id, start_date, end_date):
            raise ValueError("Maintanence conflict detected")
        
        maintanence = Maintanence(device_id, price, start_date, end_date)
        maintanence.store_data()
        cls.find_all_maintanence()
        return True


if __name__ == "__main__":
    # Create a device
    maintanence_service = MaintanenceService()
    print(maintanence_service.find_all_maintanence())
    #print(reservation_service.create_reservation("2", "Device2", "2021-01-01 00:00:00", "2021-01-02 00:00:00"))
    #print(reservation_service.create_reservation("one@mci.edu", "Device2", "2021-01-01 00:00:00", "2021-01-02 00:00:00"))
    print(maintanence_service.create_maintanence("one@mci.edu", "Device2", "2021-02-01 00:00:00", "2021-02-02 00:00:00"))
