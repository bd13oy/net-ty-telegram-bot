# Telegram Бот: "Нет ты" (удваивает текст)

Простой Telegram-бот, который отвечает на фразу "нет ты", каждый раз удваивая её.

Пример:
```
нет ты
нет ты нет ты
нет ты нет ты нет ты нет ты
...
```

## Установка (через Render)

1. Разверните этот репозиторий на Render:
   - Build command: `pip install -r requirements.txt`
   - Start command: `python net_ty_text_multiplier_bot.py`
   - Env var: `TOKEN=ваш_токен_от_BotFather`

## Локальный запуск

```bash
pip install -r requirements.txt
export TOKEN=ваш_токен
python net_ty_text_multiplier_bot.py
```
