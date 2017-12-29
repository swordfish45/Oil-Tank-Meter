#!/bin/bash
sqlite3 fuellevel.db "BEGIN; CREATE TABLE level (timestamp DATETIME, level NUMERIC);COMMIT;"
