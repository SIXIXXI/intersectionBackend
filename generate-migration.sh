#! /usr/bin/env bash

# Description: Generate new alembic migration version with a custom name

# Prompt the user for the migration name
echo "Enter the name for the new migration:"
read -r migration_name

# Check if the input is empty
if [ -z "$migration_name" ]; then
  echo "Migration name cannot be empty. Exiting."
  exit 1
fi

# Auto generate migrations
alembic revision --autogenerate -m "$migration_name"

# Notify the user
echo "Migration '$migration_name' has been created successfully."