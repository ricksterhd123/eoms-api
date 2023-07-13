#!/bin/bash
set -e

# CREATE USER eoms PASSWORD '$POSTGRES_PASSWORD';
# GRANT ALL PRIVILEGES ON DATABASE eoms TO eoms;

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" << cat emos.sql
