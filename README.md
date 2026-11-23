<!-- BADGES -->

[PYTHON_BADGE]: https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[FASTAPI_BADGE]: https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white
[POETRY_BADGE]: https://img.shields.io/badge/Poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=white
[PYTEST_BADGE]: https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white
[RUFF_BADGE]: https://img.shields.io/badge/Ruff-D7FF64?style=for-the-badge&logo=ruff&logoColor=black
[WIP_BADGE]: https://img.shields.io/badge/Status-Em%20Desenvolvimento-blue?style=for-the-badge

<!-- PROJECT -->
<h1 align="center" style="font-weight: bold;">FastAPI do Zero (Fast Zero) ⚡</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-blue?style=for-the-badge" alt="Status Em Desenvolvimento">
  <img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python Badge">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI Badge">
  <img src="https://img.shields.io/badge/Poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=white" alt="Poetry Badge">
  <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest Badge">
  <img src="https://img.shields.io/badge/Ruff-D7FF64?style=for-the-badge&logo=ruff&logoColor=black" alt="Ruff Badge">
</p>

<p align="center">
  <a href="#-descrição">Descrição</a> •
  <a href="#-funcionalidades">Funcionalidades</a> •
  <a href="#-destaques-técnicos">Destaques</a> •
  <a href="#-como-executar">Como Executar</a> •
  <a href="#-roadmap-futuro">Roadmap Futuro</a>
</p>

---

## 📌 Descrição

Repositório de estudos dedicado ao acompanhamento do curso gratuito **FastAPI do Zero (2025)** do [Dunossauro](https://fastapidozero.dunossauro.com/).

O objetivo do projeto (`fast-zero`) é construir APIs REST modernas em Python utilizando **FastAPI** com boas práticas de engenharia de software desde a primeira aula: gerenciamento de dependências com Poetry, linting e formatação automatizada com Ruff, automação de tarefas com Taskipy e testes automatizados com Pytest e cobertura de código.

---

## 🚀 Funcionalidades

### Conteúdo Implementado

- **Aula 1 (`aula_1/`):**
  - Configuração do ambiente Python 3.13+ com Poetry (`pyproject.toml` e `poetry.lock`).
  - Endpoint inicial `GET /` em `aula_1/fast_zero/app.py` retornando resposta JSON (`{"message": "Olá Mundo!!"}`).
  - Teste automatizado de integração com `TestClient` e `HTTPStatus` em `aula_1/tests/test_app.py`.

### Próximos Módulos do Curso

- Modelagem de dados com Pydantic e operações CRUD completas.
- Integração com banco de dados relacional (SQLAlchemy e migrações Alembic).
- Autenticação e autorização com JWT.
- Refatoração em routers, testes assíncronos e deploy em container.

---

## 🔒 Destaques Técnicos

- **Qualidade de Código Automatizada:** Configuração completa do **Ruff** no `pyproject.toml` (`line-length = 79`, aspas simples e regras `I`, `F`, `E`, `W`, `PL`, `PT`).
- **Automação de Fluxo com Taskipy:** Tarefas padronizadas (`lint`, `format`, `run`, `test` com hooks `pre_format`, `pre_test` e `post_test` gerando relatório HTML de cobertura).
- **Testes com Cobertura:** Integração nativa de `pytest` + `pytest-cov` executando automaticamente a checagem de lint antes da suíte de testes.

---

## 📍 Como Executar

### Pré-requisitos

- [Python 3.13+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Git](https://git-scm.com/)

### Clonando o Repositório

```bash
# Clone o projeto para a sua máquina local
git clone https://github.com/MarissaBorges/fastAPI.git

# Entre no diretório do projeto
cd fastAPI
```

### Instale as Dependências

```bash
# Instale as dependências de produção e desenvolvimento com Poetry
poetry install
```

### Iniciando o Projeto e Executando Testes

Como os arquivos da primeira aula estão organizados em `aula_1/`:

```bash
# Executar a API em modo desenvolvimento
poetry run fastapi dev aula_1/fast_zero/app.py

# Executar os testes com cobertura (a partir da pasta aula_1)
PYTHONPATH=aula_1 poetry run pytest -s -x --cov=fast_zero -vv aula_1/tests

# Verificar lint e formatação com Ruff
poetry run task lint
poetry run task format
```

Com o servidor ativo, acesse a documentação interativa automática (Swagger UI) em `http://127.0.0.1:8000/docs`.

---

## 🗺️ Roadmap Futuro

- [x] **Aula 1:** Configuração do ambiente, app inicial e primeiros testes com Pytest.
- [ ] **Aula 2:** Desenvolvimento de rotas CRUD e validação de schemas com Pydantic.
- [ ] **Aula 3:** Integração com banco de dados (SQLAlchemy) e migrações (Alembic).
- [ ] **Aula 4:** Autenticação, segurança de senhas e tokens JWT.
- [ ] **Aula 5+:** Routers modulares, testes assíncronos e deploy com Docker.

---

## 🤝 Colaboradores

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/MarissaBorges">
        <img src="https://github.com/MarissaBorges.png?size=100" width="100px;" alt="Foto de Marissa Borges"/><br>
        <sub>
          <b>Marissa Borges</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

---

## 📫 Como Contribuir

Contribuições e sugestões de melhoria são muito bem-vindas!

1. Faça um **Fork** do projeto.
2. Crie uma nova branch para sua Feature (`git checkout -b feature/AmazingFeature`).
3. Faça o **Commit** de suas mudanças (`git commit -m 'Add some AmazingFeature'`).
4. Faça o **Push** da sua branch (`git push origin feature/AmazingFeature`).
5. Abra um **Pull Request**.
