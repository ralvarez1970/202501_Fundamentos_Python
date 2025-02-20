## R. Alvarez, 2025
## Python bootcamp

## Importa classes

from humans import Human
from registro import Registro


## Cria donos de pets

maria = Human ("Maria", "Nunes", "female", 52, "Rio de Janeiro", "mn@gmail.com", "22304-102")
ze = Human ("Jose", "Cunha", "male", 32, "Florianopolis", "zcl@gmail.com", "52023-098")
roberto = Human ("Roberto", "Alvarez", "male", 20, "Brasilia", "ra@aventures.com.br", "71680-357")


## Entra pets

owner = Registro.request_registry()


## Mostra pets do proprietario(a) selecionado(a)

Registro.show_pet_owner(owner)
