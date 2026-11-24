
# CyberSage AI

An AI-powered Cyber Threat Intelligence platform using
fine-tuned IBM Granite Small Language Models, Model Context
Protocol (MCP), and Retrieval-Augmented Generation (RAG).

## Project Objective

CyberSage AI aims to automate and improve the analysis of
written cybersecurity threat intelligence reports.

The platform will extract Indicators of Compromise (IOCs),
analyse attacker behaviours, map evidence-supported behaviours
to MITRE ATT&CK, and generate structured intelligence reports.

## Core Capabilities

- IBM Granite SLM fine-tuning using LoRA/QLoRA
- Cyber Threat Intelligence report analysis
- IOC extraction and categorisation
- MITRE ATT&CK mapping
- RAG-based cybersecurity knowledge retrieval
- MCP clients and servers
- External threat intelligence enrichment
- AI safety guardrails
- Benchmarking and comparative evaluation
- Analyst-facing web application

## Technology Stack

- Python
- FastAPI
- IBM Granite
- Hugging Face Transformers
- PEFT / LoRA
- Model Context Protocol
- Retrieval-Augmented Generation
- Next.js and TypeScript
- PostgreSQL and pgvector
- Docker

## Project Structure

- `ai-engine/` - Dataset preparation, training, inference and evaluation
- `backend/` - API and AI orchestration
- `mcp-servers/` - MCP server implementations
- `frontend/` - Analyst-facing web application
- `infrastructure/` - Containerisation and deployment
- `docs/` - Project and architecture documentation
- `benchmarks/` - Model evaluation and comparisons
- `tests/` - Automated testing

## Development Status

Initial repository and backend foundation.

## Research Focus

Investigate whether parameter-efficient fine-tuning of a
small general-purpose language model improves its performance
on cybersecurity threat intelligence analysis tasks.
