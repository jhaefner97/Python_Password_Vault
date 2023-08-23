CREATE TABLE IF NOT EXISTS Password (
    PasswordID INTEGER PRIMARY KEY,
    AccountID_FK INTEGER,
    PasswordHash BLOB,
    FOREIGN KEY (AccountID_FK) REFERENCES Account (AccountID)
);