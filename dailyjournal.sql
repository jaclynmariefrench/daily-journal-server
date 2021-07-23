CREATE TABLE `journal_entries` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `time` TIMESTAMP,
    `concept` TEXT NOT NULL,
    `entry` TEXT NOT NULL,
    `mood_id` INTEGER NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `moods`(`id`)
); 

CREATE TABLE `moods` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label` TEXT NOT NULL
);
INSERT INTO `journal_entries`
VALUES (
        NULL,
        1626967489,
        'Python Server',
        'I am realizing I do not know completely what I am doing with python yet',
        2
    );

INSERT INTO `journal_entries`
VALUES (
        NULL,
        1626967925,
        'React',
        'I have a lot of bugs to work thru with my React code.',
        3
    );

INSERT INTO `journal_entries`
VALUES (
        NULL,
        1626967998,
        'SQL',
        'I feel really good about creating tables in SQL.',
        1
    );

INSERT INTO `moods` 
VALUES (NULL, 'happy');

INSERT INTO `moods` 
VALUES (NULL, 'fine');

INSERT INTO `moods` 
VALUES (NULL, 'potato');

