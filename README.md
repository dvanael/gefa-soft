
<h1 align="center" style="font-weight: bold;">
 GEFA SOFT
</h1>

<p align="center">
Um Sistema Web para Gerenciamento de Casa de Farinha.
</p>

<p align="center">
  <a href="#sobre">Sobre</a> •
  <a href="#apresentação">Apresentação</a> •
  <a href="#instalação">Instalação</a> •
  <a href="#colaboradores">Colaboradores</a>
</p>

---

## Sobre
O **GEFA SOFT** visa facilitar a vida dos **gerentes de Casas de Farinha**. Com ele, você pode gerenciar as contas da empresa.

Esse sistema foi criado para a conclusão da máteria **Projeto de Desenvolvimento de Sistemas para Internet**. 

Durante seu desenvolvimento, a equipe seguiu **metodologias ágeis**, combinando **Scrum** e **Kamban** para organização das tarefas e acompanhamento do desenvolvimento. Pode ser conferido no [Github Projects](https://github.com/users/dvanael/projects/3) do repositório.

**Figma** foi usado para prototipação. [Confira aqui.](https://www.figma.com/proto/R1nQXjDV6O2fvNt04fQgxm/gefasoft?node-id=26-375&t=7dR4UhBlTo3wWw78-1)

Para desenvolvimento do backend, foi utilizado o framework **Django**. No frontend, foi usado **HTML, CSS e Javascript** junto do framework **Bootstrap**.

## Apresentação
Gravações e telas do sistema funcionando.

<img width="1894" height="930" alt="image" src="https://github.com/user-attachments/assets/841a8e0e-fb7b-4636-856d-02a111e0ae1e" />

<img width="1896" height="937" alt="image" src="https://github.com/user-attachments/assets/ac64ef10-7989-468f-ab69-c6fb963a7288" />


## Instalação

### Configurando o ambiente

 - Clone o [repositório](https://github.com/dvanael/gefa-soft)

```bash
git clone https://github.com/dvanael/gefa-soft.git
```

- Crie um ambiente virtual

```bash
python -m venv .venv
```

- Ative o ambiente virtual

_windows_
```powershell
.venv/Scripts/activate
```
_linux, macOs_
```bash
source .venv/bin/activate
```

---

### Configurando sua máquina

- Instale as dependências

```bash
pip install -r requirements.txt
```

- Crie as variáveis de ambiente

```bash
python scripts/env.py
```

> Se necessário, mude as configurações do  arquivo `.env`

- Faça as migrações necessárias

```bash
python manage.py migrate
```

---

### Rodando o servidor

- Crie um **super usuário**.

```bash
python manage.py createsuperuser
```

- Rode o servidor

```bash
python manage.py runserver
```

- Acesse a aplicação localmente

  - **[localhost:8000/](http://localhost:8000/)**

---

## Colaboradores

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/dvanael" title="Ana Barbosa">
        <img src="https://avatars.githubusercontent.com/dvanael" width="100px;" alt="collaborators pictures"/><br>
        <sub>
          <b>Ana Barbosa 🐋</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/poliana-dev" title="Poliana Pinheiro">
        <img src="https://avatars.githubusercontent.com/poliana-dev" width="100px;" alt="collaborators pictures"/><br>
        <sub>
          <b>Poliana Pinheiro 🐸</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/devwenderson" title="Wenderson Nascimento">
        <img src="https://avatars.githubusercontent.com/devwenderson" width="100px;" alt="collaborators pictures"/><br>
        <sub>
          <b>Wenderson Nascimento 🦆</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
