# CF Ops &amp; Observability

Sistema para gerenciar Cloudflare (API v4) e observar tráfego/logs, com:

- Backend em FastAPI (Python).
- Frontend em React + Vite (pronto para Vercel).
- Backend preparado para deploy no Render.

## Estrutura

- `backend/`
  - FastAPI, cliente Cloudflare, ingestão de logs e métricas.
- `frontend/`
  - React + Vite SPA (dashboard).
- `backend/render.yaml`
  - Exemplo de configuração para deploy no Render (backend).

## Como rodar localmente

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

O frontend usará por padrão `http://localhost:8000/api` como backend.

## Deploy do frontend na Vercel

1. Suba o repositório para o GitHub.
2. Crie um projeto na Vercel apontando para a pasta `frontend/`.
3. Configure:
   - Build Command: `npm run build`
   - Output Directory: `dist`
4. Adicione variável de ambiente:
   - `VITE_API_BASE_URL = https://SEU_BACKEND_PUBLICO/api`

## Deploy do backend no Render (exemplo)

Você pode:

- Usar o plano Python Web Service.
- Ou usar o Dockerfile em `backend/Dockerfile`.

Exemplo simples (usando render.yaml como referência):

- Crie um Web Service apontando para o diretório `backend/`.
- Build Command: `pip install --no-cache-dir -r requirements.txt`
- Start Command: `uvicorn app.main:app --host 0.0.0.0 --port 8000`
- Defina as env vars:
  - `POSTGRES_DSN`
  - `CLICKHOUSE_DSN`
  - `LOGPUSH_SHARED_SECRET`
  - `BACKEND_CORS_ORIGINS` (por exemplo: `[\"https://seu-frontend.vercel.app\"]`)

Depois de o backend estar público, atualize:

- Na Vercel:
  - `VITE_API_BASE_URL` para apontar para a URL do backend.

## Git / GitHub

Na raiz do projeto:

```bash
git init
git add .
git commit -m "Initial CF Ops & Observability skeleton"
git branch -M main
git remote add origin git@github.com:SEU_USUARIO/SEU_REPO.git
git push -u origin main
```

Depois disso, é só conectar a Vercel ao repositório (para o frontend) e o Render (para o backend).