CREATE TABLE imports (
    import_id SERIAL PRIMARY KEY,
    import_date DATE NOT NULL,
    file_name VARCHAR NOT NULL
);

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    project_code VARCHAR NOT NULL,
    project_name VARCHAR NOT NULL
);

CREATE TABLE data_values (
    value_id SERIAL PRIMARY KEY,
    import_id INTEGER NOT NULL,
    project_id INTEGER NOT NULL,
    plan_date DATE NOT NULL,
    plan_value DECIMAL,
    fact_date DATE,
    fact_value DECIMAL,
    FOREIGN KEY (import_id) REFERENCES imports(import_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);
