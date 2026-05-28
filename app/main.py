from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import os

app = FastAPI(title="Autonomous SRE Backend API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "backend-api",
        "timestamp": datetime.utcnow().isoformat(),
        "environment": os.environ.get("ENVIRONMENT", "unknown"),
    }


@app.get("/api/status")
def status():
    return {
        "status": "healthy",
        "message": "Python FastAPI running on ECS Fargate",
        "service": "backend-api",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0",
    }


@app.get("/api/info")
def info():
    return {
        "project": "autonomous-sre",
        "stack": ["Next.js", "FastAPI", "ECS Fargate", "ALB", "Terraform"],
        "repos": [
            {"name": "repo1-base-infra", "role": "VPC, Subnets, ECS Cluster"},
            {"name": "repo2-app-infra", "role": "ALB, Task Definitions, ECR"},
            {"name": "repo3-frontend", "role": "Next.js frontend"},
            {"name": "repo4-backend", "role": "Python API (this service)"},
        ],
    }
