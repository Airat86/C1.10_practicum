class Clients:
    def __init__(self, name, balans):
        self.name = name
        self.balans = balans

    def get_name(self):
        return self.name

    def get_balans(self):
        return self.balans

    def print_client_info(self):
        return (f'Клиент: "{self.name}", Баланс: {self.balans}, руб.')