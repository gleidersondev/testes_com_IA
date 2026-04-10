# Imersão Python & Django - Landing Page

Este projeto é uma landing page de um curso fictício "Imersão Python & Django", desenvolvida com Python e Django. A página inclui seções de hero, benefícios, módulos do curso, instrutor, pricing com oferta especial e garantia.

## 🚀 Como clonar e instalar

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd /workspace
```

### 2. Criar ambiente virtual (recomendado)

```bash
python -m venv venv
```

### 3. Ativar o ambiente virtual

**Linux/Mac:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Executar migrações do banco de dados

```bash
python manage.py migrate
```

### 6. Rodar o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse a aplicação em: **http://localhost:8000**

## 📁 Estrutura do Projeto

```
/workspace
├── manage.py
├── requirements.txt
├── curso/                  # App principal da landing page
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── curso/
│           └── landing.html
└── projeto_django/         # Configurações do projeto
    └── settings.py
```

## 🎨 Seções da Landing Page

- **Hero Section**: Título impactante, subtítulo e call-to-action
- **Benefícios**: 6 cards destacando vantagens do curso
- **Módulos**: 5 seções detalhando o conteúdo programático
- **Instrutor**: Informações sobre o professor
- **Pricing**: Oferta especial com desconto e garantia
- **Footer**: Links e copyright

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Django 4.x
- HTML5
- CSS3
- Font Awesome (ícones)
- Google Fonts

## 📝 Personalização

Para personalizar a landing page, edite os seguintes arquivos:

- `curso/templates/curso/landing.html`: Conteúdo HTML e textos
- `curso/views.py`: Lógica da view
- `projeto_django/urls.py`: Configuração de URLs

## ⚠️ Importante

Este é um projeto de exemplo para fins educacionais. Em produção, configure adequadamente:
- `DEBUG = False` no settings.py
- Variáveis de ambiente para dados sensíveis
- Banco de dados adequado (PostgreSQL, MySQL, etc.)
- Servidor WSGI (Gunicorn, uWSGI)