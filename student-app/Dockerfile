FROM node:20-alpine

WORKDIR /app

# Установка curl и bash
RUN apk add --no-cache curl bash

# Установка Bun
RUN curl -fsSL https://bun.sh/install | bash && \
    ln -s /root/.bun/bin/bun /usr/local/bin/bun

# Копируем файлы зависимостей
COPY package.json bun.lock ./

# Устанавливаем зависимости
RUN bun install

# Копируем исходный код
COPY . .

# Собираем приложение
RUN bun run build

EXPOSE 3000

CMD ["bun", "run", "dev"]