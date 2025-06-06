# Akame 

### Projeto Django voltado a loja virtual de veículos

## Como Rodar

* Tenha o python instalado na máquina (recomendado  versão acima de 3.8)
* Este projeto utiliza de ambiente virtual, o nome está no arquivo .gitignore
    * ``` ambienteVirtual ```
    * Criando o ambiente
        * ``` python -m venv ambienteVirtual ```
    * Ativando
        * Windows
            * ``` ambienteVirtual\Scripts\activate ```
        * Linux
            * ``` source ambienteVirtual\bin\activate ```
    * Desativando
        * Windows
            * ``` ambienteVirtual\Scripts\deactivate ```
        * Linux
            * ``` deactivate ```
* Instalar dependências
    * Django
        * ``` python3 -m pip install Django ``` 
    * Pillow
        * ``` pip install pillow ```
    * requests
        * ``` pip install requests ```
    * matplotlib
        * ``` pip install matplotlib ```
    * djangorestframework
        * ``` pip install djangorestframework ```
    * django-cors-headers
        * ``` pip install django-cors-headers ```
* Rodando
    * ``` python3 manage.py runserver ```
    * Será informado a url do servidor, copiar e colar no navegador
