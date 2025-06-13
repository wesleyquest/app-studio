## app studio
웨슬리퀘스트의 DATA, AI 기반 App 레포지토리

## Getting Started
#### 1. Installation
uv sync --frozen --no-install-project --no-dev
source .venv/bin/activate
#### 2. Run
reflex run

## Development Process
#### 1. Environment
uv init --python 3.12
uv add -r requirements.txt
source .venv/bin/activate
reflex init
#### 2. DB model
reflex db init
reflex db makemigrations
reflex db migrate

