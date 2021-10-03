CREATE TABLE "role"
(
    id            INT,

    role          VARCHAR NOT NULL UNIQUE,

    PRIMARY KEY (id)
);

INSERT INTO "role"
VALUES (1, 'admin'),
       (2, 'moderator'),
       (3, 'user');

CREATE TABLE user_type
(
    id            INT,

    type          VARCHAR NOT NULL UNIQUE,

    PRIMARY KEY (id)
);

INSERT INTO user_type
VALUES (1, 'standard'),
       (2, 'premium');

CREATE TABLE "user"
(
    id            INT,
    role_id       INT     NOT NULL,
    user_type_id  INT     NOT NULL,

    email         VARCHAR NOT NULL UNIQUE,
    password      VARCHAR NOT NULL,

    PRIMARY KEY (id),
    CONSTRAINT role_fk
        FOREIGN KEY (role_id)
            REFERENCES "role" (id),
    CONSTRAINT user_type_fk
        FOREIGN KEY (user_type_id)
            REFERENCES user_type (id)
);

CREATE TABLE category
(
    id            INT,
    name          VARCHAR NOT NULL UNIQUE,

    PRIMARY KEY (id)
);

CREATE TABLE subcategory
(
    id            INT,
    category_id   INT     NOT NULL,

    name          VARCHAR NOT NULL,

    PRIMARY KEY (id),
    CONSTRAINT section_fk
        FOREIGN KEY (category_id)
            REFERENCES category (id)
);

CREATE TABLE game_mode
(
    id            INT,

    mode          VARCHAR NOT NULL,

    PRIMARY KEY (id)
);

CREATE TABLE set_fiches
(
    id            INT,
    game_mode_id  INT      NOT NULL,
    category_id   INT      NOT NULL,
    user_id       INT,

    name         VARCHAR  NOT NULL,

    PRIMARY KEY (id),
    CONSTRAINT game_mode_fk
        FOREIGN KEY (game_mode_id)
            REFERENCES game_mode (id),
    CONSTRAINT category_fk
        FOREIGN KEY (category_id)
            REFERENCES category (id),
    CONSTRAINT user_fk
        FOREIGN KEY (user_id)
            REFERENCES "user" (id)
);

CREATE TABLE card
(
    id            INT,
    set_fiches_id INT      NOT NULL,

    PRIMARY KEY (id),
    CONSTRAINT set_fiches_fk
        FOREIGN KEY (set_fiches_id)
            REFERENCES set_fiches (id)
);

CREATE TABLE issue
(
    id            INT,
    card_id       INT      NOT NULL,

    content       VARCHAR  NOT NULL,

    PRIMARY KEY (id),
    CONSTRAINT card_fk
        FOREIGN KEY (card_id)
            REFERENCES card (id)
);

CREATE TABLE issue_answer
(
    id            INT,
    issue_id      INT      NOT NULL,

    content       VARCHAR  NOT NULL,

    PRIMARY KEY (id),
    CONSTRAINT issue_fk
        FOREIGN KEY (issue_id)
            REFERENCES issue (id)
);