-- comment

CREATE TABLE IF NOT EXISTS schetovod (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    namepay TEXT NOT NULL,
    price REAL NOT NULL,
    timepoint DATE NOT NULL,
    count INTEGER NOT NULL DEFAULT 1 
)
