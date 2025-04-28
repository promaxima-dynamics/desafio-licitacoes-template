# Use uma imagem Node.js oficial como base
FROM node:18-alpine

# Define o diretório de trabalho no container
WORKDIR /app

# Copia package.json e lock file (package-lock.json ou yarn.lock)
# TODO: Certifique-se que esses arquivos existem no diretório frontend/
COPY package*.json yarn.lock* ./ 

# Instala as dependências (use npm ou yarn)
# RUN npm install
RUN yarn install --frozen-lockfile # Use yarn se for o caso

# Copia o restante do código do frontend
COPY . .

# Expõe a porta do servidor de desenvolvimento (Vite usa 5173 ou 3000 por padrão)
EXPOSE 3000

# Comando padrão para rodar o servidor de desenvolvimento
# TODO: Ajuste para o comando correto (npm run dev, yarn dev, etc.)
# Pode ser necessário adicionar --host para expor fora do container
CMD ["yarn", "dev", "--host"] 