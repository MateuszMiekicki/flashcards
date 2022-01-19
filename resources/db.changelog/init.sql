CREATE TABLE "role" (
    id SERIAL,
    role VARCHAR NOT NULL UNIQUE,
    PRIMARY KEY (id)
);
CREATE TABLE user_type (
    id SERIAL,
    type VARCHAR NOT NULL UNIQUE,
    PRIMARY KEY (id)
);
CREATE TABLE "user" (
    id SERIAL,
    role_id INT NOT NULL,
    user_type_id INT NOT NULL,
    login VARCHAR NOT NULL UNIQUE,
    email VARCHAR NOT NULL UNIQUE,
    password VARCHAR NOT NULL,
    is_activate BOOLEAN NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT role_fk FOREIGN KEY (role_id) REFERENCES "role" (id),
    CONSTRAINT user_type_fk FOREIGN KEY (user_type_id) REFERENCES user_type (id)
);
CREATE TABLE category (
    id SERIAL,
    name VARCHAR NOT NULL UNIQUE,
    PRIMARY KEY (id)
);
CREATE TABLE subcategory (
    id SERIAL,
    category_id INT NOT NULL,
    subcategory_id INT,
    name VARCHAR NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT section_fk FOREIGN KEY (category_id) REFERENCES category (id)
);
CREATE TABLE set_cards (
    id SERIAL,
    subcategory_id INT NOT NULL,
    user_id INT NOT NULL,
    name VARCHAR NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT category_fk FOREIGN KEY (subcategory_id) REFERENCES subcategory (id),
    CONSTRAINT user_fk FOREIGN KEY (user_id) REFERENCES "user" (id)
);
CREATE TABLE card (
    id SERIAL,
    set_cards_id INT NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT set_cards_fk FOREIGN KEY (set_cards_id) REFERENCES set_cards (id)
);
CREATE TABLE question (
    id SERIAL,
    card_id INT NOT NULL,
    content VARCHAR NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT card_fk FOREIGN KEY (card_id) REFERENCES card (id)
);
CREATE TABLE question_answer (
    id SERIAL,
    question_id INT NOT NULL,
    content VARCHAR NOT NULL,
    is_correct_answer BOOLEAN NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT question_fk FOREIGN KEY (question_id) REFERENCES question (id)
);