#!/bin/bash
set -e

psql "postgresql://$POSTGRES_USER@:5432/$POSTGRES_DB" -v ON_ERROR_STOP=1 <<-EOSQL
  CREATE USER {{cookiecutter.project_short_name}}_dev WITH PASSWORD '';
  CREATE DATABASE {{cookiecutter.project_short_name}}_dev;
  GRANT ALL PRIVILEGES ON DATABASE {{cookiecutter.project_short_name}}_dev TO {{cookiecutter.project_short_name}}_dev;
EOSQL

psql -v ON_ERROR_STOP=1 "postgresql://$POSTGRES_USER@:5432/{{cookiecutter.project_short_name}}_dev" <<-EOSQL
  CREATE EXTENSION IF NOT EXISTS pgcrypto;
  SELECT gen_random_uuid();
EOSQL
