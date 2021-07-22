CREATE TABLE `journal_entries` (
    `id` INTEGER NOT NULL, PRIMARY KEY AUTOINCREMENT,
    `time` TIMESTAMP,
    `concept` TEXT NOT NULL,
    `entry` TEXT NOT NULL,
    `mood_id` INTEGER NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `moods`(`id`)
)

CREATE TABLE `moods` (
    `id` INTEGER NOT NULL, PRIMARY KEY AUTOINCREMENT,
    `happy` INTEGER NOT NULL,
    `fine` INTEGER NOT NULL,
    `sad` INTEGER NOT NULL,
)