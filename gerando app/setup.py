from setuptools import setup, find_packages
from pathlib import Path
'''
	Title: Configurações e requisitos para instalação do software

	command: mkdir engesep_relatorios
			 python3 -m venv engesep_relatorios/ambiente # criar o ambiente
			 source engesep_relatorios/ambiente/bin/activate
			 python3 -m install --upgrade pip
			 pip install --upgrade setuptools
			 python3 setup.py sdist
'''

setup(
    name='EngeSEP_Relatorios',
    version='0.0.1',
    author='Miliano Fernades de Oliveira Junior',
    author_email='jrmfilho37@gmail.com',
    packages=find_packages(),
    install_requires=[
        'kivy',
        'kivymd',
    ],
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# python3 /home/jrmfilho23/Documentos/EngeSEP/apps_mvc/APPDB/main.py