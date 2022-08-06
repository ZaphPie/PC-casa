from pathlib import Path

path_to_file = 'ejemplo.txt'
path = Path(path_to_file)

if path.is_file():
    print(f'El archivo {path_to_file} existe')
else:
    print(f'El archivo {path_to_file} no existe')
