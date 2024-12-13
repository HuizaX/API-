class User:
    def __init__(self, user_id, name, username, email, address, phone, website, company):
        self.user_id = user_id
        self.name = name
        self.username = username
        self.email = email
        self.address = address  # Diccionario con detalles de la dirección
        self.phone = phone
        self.website = website
        self.company = company  # Diccionario con detalles de la compañía

    def __str__(self):
        return f"User(ID: {self.user_id}, Name: {self.name}, Email: {self.email})"

    @staticmethod
    def from_json(data):
        return User(
            user_id=data["id"],
            name=data["name"],
            username=data["username"],
            email=data["email"],
            address=data["address"],  # Se pasa el diccionario completo
            phone=data["phone"],
            website=data["website"],
            company=data["company"]  # Se pasa el diccionario completo
        )