# Mega Sena Bot 🎯

Bot do Telegram que gerencia jogos da Mega-Sena, verifica resultados e permite registrar manualmente sorteios.

## Funcionalidades

- ✅ Adicionar, remover e listar jogos (admin)
- 🎯 Conferência automática com API da Caixa
- 🖊 Resultado manual opcional
- 📅 Consulta de concursos anteriores

## Como usar

### 1. Clone o projeto

```bash
git clone https://github.com/seu-usuario/mega-bot.git
cd mega-bot
```

### 2. Instale dependências

```bash
pip install -r requirements.txt
```

### 3. Configure o token

Defina a variável de ambiente `TELEGRAM_BOT_TOKEN`:

```bash
export TELEGRAM_BOT_TOKEN=8046819996:SEU_TOKEN_AQUI
```

### 4. Execute o bot

```bash
python bot.py
```

---

### 👤 Admin

Apenas o ID definido no código como `ADMIN_ID` tem permissão para adicionar/remover jogos e registrar resultados manuais.

---

📦 Projeto pronto para rodar localmente ou no deploy (Render, Heroku, etc).