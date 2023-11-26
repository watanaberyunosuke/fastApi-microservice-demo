# FastAPI Microservice Demo

## Overview
This project is a FastAPI service designed to manage fish data for an Animal Crossing-like application. It provides RESTful endpoints to create, retrieve, update, and delete fish information.

## Features
- Read operations for fish data.
- Integration with SQLAlchemy for database interactions.
- Pydantic models for request and response validation.

## Technology Stack
- FastAPI: Modern, fast web framework for building APIs with Python 3.7+.
- SQLAlchemy: SQL toolkit and ORM for Python.
- Uvicorn: ASGI server for FastAPI.

## Usage
To run the FastAPI server:

```bash
uvicorn main:app --reload
```
This will start the gateway FastAPI application on `http://127.0.0.1:8000`.
Please also start the service application, the default service application starts at `http://127.0.0.1:8081`

## Endpoints
- `GET /fish/{fish_id}`: Retrieve a fish by its ID.