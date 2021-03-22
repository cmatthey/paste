DROP DATABASE pb;
CREATE DATABASE pb;
CREATE USER pb WITH PASSWORD 'xxx';
ALTER ROLE pb SET client_encoding TO 'utf8';
ALTER ROLE pb SET default_transaction_isolation TO 'read committed';
ALTER ROLE pb SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE pb TO pb;
ALTER USER pb CREATEDB;
