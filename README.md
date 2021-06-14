Proyecto Pokemon V0.1
Autor:Jesus pozzo


## Instalación

1. Clonar este repositorio en tu equipo locas: `https://github.com/jpozzo5/project_pokemon-.git`.
2. Para iniciar nuestro entorno virtual accedemos al proyecto y en la carpera `env_pokemon/Scripts` ejecutamos el comando `source active`.
3. Para mayor informacion en la carpeta del proyecto se encuentra un archivo llamado requerements.txt el cual nos indica cuales son las dependecias utilizadas en este proyecto para instalarlas podemos utilizar el comando
`pip install -r requirements.txt`.
4. Django nos proporciona crear nuestro propios comandos,el cual se han creado 4 para importar los pokemones,localizacion,regiones y areas ,Tomando la informacion de los archivo json en se cuentran en la siguiente ruta `project_pokemon\PokemonApp\management\static` y los comandos en `project_pokemon\PokemonApp\management\commands`.
5. Importar localizacion, acceder a la ruta principal del proyecto  y ejecutar el comando `python manage.py load_data_location`.
6. Importar Regiones, acceder a la ruta principal del proyecto  y ejecutar el comando `python manage.py load_data_regions`.
7.  Importar Areas, acceder a la ruta principal del proyecto  y ejecutar el comando `python manage.py load_data_areas`
8. Importar Pokemones, acceder a la ruta principal del proyecto  y ejecutar el comando `python manage.py load_data_pokemon`


Finalmente la informacion ya ha sido importada ya podremos utilizar nuestra api Rest para Consultar toda la mayor informacion de los pokemones!!