CREATE TABLE project_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at INTEGER DEFAULT 0
);