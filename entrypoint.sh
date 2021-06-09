#!/usr/bin/env bash
#
#echo "*************** creating database ****************"
#alembic create schema example_json if not exists

echo "_______________running autogenerate_______________"
alembic revision --autogenerate -m "Create User Table"

echo "_______________executing migrations_______________"
alembic upgrade head

echo "_______________running fastapi_______________"
uvicorn main:app --host 0.0.0.0 --port 8000 --reload