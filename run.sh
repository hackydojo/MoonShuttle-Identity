#!/usr/bin/env bash

cd src
uvicorn app.main:app --reload
cd ..