# Welcome to kelev project

## Obrigatório
1. Clone no projeto.
```bash
$ git clone https://github.com/YaakovDantas/kelev.git
```

2. Entre no diretorio raiz do projeto.
```bash
seu/path/petmania
```

3. Crie uma [`virtualenv`](https://virtualenv.pypa.io/en/latest/index.html).
3.1. Você deverá ter acesso sudo.
  ```bash
  # Instalar a ferramenta virtualenv pelo pip3(python3)
  $ [sudo] pip3 install virtualenv
  # Criar uma virtual env(maquina virtual) 'env'
  $ virtualenv env
  # Ative sua máquina virtual!
  $ source env/bin/activate
  ```

4. Instale todas as depedências do projeto.
  ```bash
  (env) $ pip install -r requirements.txt
  ```
5. Configurar banco de dados:
```bash
  (env) $ python manage.py makemigrations
  (env) $ python manage.py migrate
```

6. Criar uma conta de adm:
```bash
  (env) $ python manage.py createsuperuser
```
Informe nome de login, email e senha.

7. Executar o projeto.

```bash
  (env) $ python manage.py runserver
```