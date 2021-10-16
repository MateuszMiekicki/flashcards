CREATE TABLE "role" (
    id INT,
    role VARCHAR NOT NULL UNIQUE,
    PRIMARY KEY (id)
);
INSERT INTO "role"
VALUES (1, 'admin'),
    (2, 'moderator'),
    (3, 'user');
CREATE TABLE user_type (
    id INT,
    type VARCHAR NOT NULL UNIQUE,
    PRIMARY KEY (id)
);
INSERT INTO user_type
VALUES (1, 'standard'),
    (2, 'premium');
CREATE TABLE "user" (
    id INT,
    role_id INT NOT NULL,
    user_type_id INT NOT NULL,
    email VARCHAR NOT NULL UNIQUE,
    password VARCHAR NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT role_fk FOREIGN KEY (role_id) REFERENCES "role" (id),
    CONSTRAINT user_type_fk FOREIGN KEY (user_type_id) REFERENCES user_type (id)
);
CREATE TABLE setting (
    id INT,
    name VARCHAR NOT NULL UNIQUE,
    PRIMARY KEY (id)
);
CREATE TABLE user_setting (
    id INT,
    user_id INT NOT NULL,
    setting_id INT NOT NULL,
    value VARCHAR NOT NULL UNIQUE,
    PRIMARY KEY (id),
    CONSTRAINT user_fk FOREIGN KEY (user_id) REFERENCES "user" (id),
    CONSTRAINT setting_fk FOREIGN KEY (setting_id) REFERENCES setting (id)
);
CREATE TABLE category (
    id INT,
    name VARCHAR NOT NULL UNIQUE,
    PRIMARY KEY (id)
);
CREATE TABLE subcategory (
    id INT,
    category_id INT NOT NULL,
    subcategory_id INT,
    name VARCHAR NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT section_fk FOREIGN KEY (category_id) REFERENCES category (id)
);
CREATE TABLE game_mode (
    id INT,
    mode VARCHAR NOT NULL,
    PRIMARY KEY (id)
);
CREATE TABLE set_cards (
    id INT,
    game_mode_id INT NOT NULL,
    subcategory_id INT NOT NULL,
    user_id INT NOT NULL,
    name VARCHAR NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT game_mode_fk FOREIGN KEY (game_mode_id) REFERENCES game_mode (id),
    CONSTRAINT category_fk FOREIGN KEY (subcategory_id) REFERENCES subcategory (id),
    CONSTRAINT user_fk FOREIGN KEY (user_id) REFERENCES "user" (id)
);
CREATE TABLE card (
    id INT,
    set_cards_id INT NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT set_cards_fk FOREIGN KEY (set_cards_id) REFERENCES set_cards (id)
);
CREATE TABLE question (
    id INT,
    card_id INT NOT NULL,
    content VARCHAR NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT card_fk FOREIGN KEY (card_id) REFERENCES card (id)
);
CREATE TABLE question_answer (
    id INT,
    question_id INT NOT NULL,
    content VARCHAR NOT NULL,
    is_correct_answer BOOLEAN NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT question_fk FOREIGN KEY (question_id) REFERENCES question (id)
);