-- Criar banco de dados (caso ainda não exista)
CREATE DATABASE mydatabase;

-- Conectar ao banco
\c mydatabase;

-- Criar tabela de usuários
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Inserir usuário de exemplo
INSERT INTO users (name, email) VALUES ('Julio', 'julio@example.com')
ON CONFLICT (email) DO NOTHING;

