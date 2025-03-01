class User:
    _id_counter = 1

    def __init__(self, name, email):
        self.id = User._id_counter
        self.name = name
        self.email = email
        User._id_counter += 1

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}
