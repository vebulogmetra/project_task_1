CREATE TABLE imports (
    import_id INTEGER PRIMARY KEY AUTOINCREMENT,
    import_date DATE NOT NULL,
    file_name VARCHAR NOT NULL
);

CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_code VARCHAR NOT NULL,
    project_name VARCHAR NOT NULL
);

CREATE TABLE data_values (
    value_id INTEGER PRIMARY KEY AUTOINCREMENT,
    import_id INTEGER NOT NULL REFERENCES imports(import_id),
    project_id INTEGER NOT NULL REFERENCES projects(project_id),
    plan_date DATE NOT NULL,
    plan_value NUMERIC,
    fact_date DATE,
    fact_value NUMERIC
);