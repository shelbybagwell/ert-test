FROM node:18-alpine

# Working dir
WORKDIR /app

# Copy package and package lock
COPY package.json ./
COPY package-lock.json ./

# Install dependencies
RUN npm install

# Copy application files
COPY . .

EXPOSE 3000

CMD [ "npm", "start" ]