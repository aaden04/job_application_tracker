class User:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"


