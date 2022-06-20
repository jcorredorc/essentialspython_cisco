import restaurante
import users

mi_restaurante = restaurante.Restaurante(
    "bnGusto", "tipica", 3, ["arroz", "papa"])
cliente = users.Users("Pedro", "Coral", 1234)

mi_restaurante.order(cliente)
