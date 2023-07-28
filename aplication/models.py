class User:
    def __int__(self, _id, username, email, password_hash):
        self.id = _id
        self.username = username
        self.email = email
        self.password_hash = password_hash


class NVR:
    def __int__(self, location, ip, model, serial_number, users, channels, cameras):
        self.ip = ip
        self.location = location
        self.model = model
        self.serial_number = serial_number
        self.users = users
        self.channels = channels
        self.cameras = cameras
