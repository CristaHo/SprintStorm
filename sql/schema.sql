CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT UNIQUE, 
    password TEXT
);

CREATE TABLE book (
    id SERIAL PRIMARY KEY, 
    user_key TEXT,
    author TEXT, 
    title TEXT, 
    year INTEGER, 
    publisher TEXT
);

CREATE TABLE article (
    id SERIAL PRIMARY KEY, 
    user_key INTEGER, 
    author TEXT,
    year INTEGER,
    journal TEXT,
    volume INTEGER,
    pages TEXT
);


INSERT INTO book (user_key, author, title, year, publisher) VALUES ('AB1', 'Tolkien, J.R.R.', 'The Lord of the Rings', 1954, "Allen & Unwin");
INSERT INTO book (user_key, author, title, year, publisher) VALUES ('BC2', 'Tolkien, J.R.R.', 'The Hobbit', 1937, 'George Allen & Unwin');



