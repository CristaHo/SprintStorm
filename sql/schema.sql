CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY, 
    username TEXT UNIQUE, 
    password TEXT
);

CREATE TABLE IF NOT EXISTS category (
    id SERIAL PRIMARY KEY,
    name TEXT,
    user_id INTEGER REFERENCES users NOT NULL
);

CREATE TABLE IF NOT EXISTS reference (
    id SERIAL PRIMARY KEY, 
    author TEXT, 
    title TEXT, 
    year INTEGER
);

CREATE TABLE IF NOT EXISTS book (
    id SERIAL PRIMARY KEY, 
    cite_key TEXT,
    author TEXT, 
    title TEXT, 
    year INTEGER, 
    publisher TEXT,
    category_id INTEGER REFERENCES category ON DELETE CASCADE,
    user_id INTEGER REFERENCES users NOT NULL
);

CREATE TABLE IF NOT EXISTS article (
    id SERIAL PRIMARY KEY, 
    cite_key TEXT, 
    author TEXT,
    title TEXT,
    year INTEGER,
    journal TEXT,
    volume INTEGER,
    pages TEXT,
    category_id INTEGER REFERENCES category ON DELETE CASCADE,
    user_id INTEGER REFERENCES users NOT NULL
);
