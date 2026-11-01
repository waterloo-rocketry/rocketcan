# gen_parsley

A code generator that reads the `../rocketcan.yaml` CAN message definition and produces TypeScript 

## Setup

You must have the [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager installed to run `gen_parsley`.

From repo root:

```bash
cd gen_parsley
uv sync
```

This creates `.venv/` and installs locked dependencies.

## Running

From the repo root:

```bash
uv run --project gen_parsley gen_parsley/main.py
```

Or from inside `gen_parsley/`:

```bash
cd gen_parsley
uv run main.py
```

