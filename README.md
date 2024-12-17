# GEFA SOFT
Sistema Web para Gerenciamento de Casa de Farinha

## Sobre
O GEFA SOFT visa facilitar a vida dos gerentes de Casas de Farinha. Com ele, você pode gerenciar as contas da empresa.

## Instalação

### Configurando o ambiente

 - Clone o [repositório](https://github.com/IFRN-SPP/cooplink)

```bash
git clone https://github.com/IFRN-SPP/cooplink.git
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