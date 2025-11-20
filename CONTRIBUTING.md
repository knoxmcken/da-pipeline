# Contributing to DAP

We welcome contributions to the Data Analytics Pipeline (DAP) CLI app!
To contribute, please follow these guidelines.

## Setting up Your Development Environment

1.  **Fork the repository:** Fork the `da-pipeline` repository on GitHub.
2.  **Clone your fork:**
    ```bash
    git clone https://github.com/your-username/da-pipeline.git
    cd da-pipeline
    ```
3.  **Create a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```
4.  **Install dependencies:**
    ```bash
    pip install -e .
    pip install -r requirements-dev.txt # (assuming we'll create this later)
    ```

## Coding Style and Conventions

*   We use `ruff` for linting and formatting. Please ensure your code passes `ruff check` and `ruff format`.
*   Follow the existing code style.
*   Write clear, concise, and well-documented code.

## Running Tests

To run the test suite, use `pytest`:
```bash
pytest
```

## Submitting Bug Reports and Feature Requests

Please use the GitHub issue tracker to report bugs or suggest new features.

## Pull Request Process

1.  Create a new branch for your changes:
    ```bash
    git checkout -b feature/your-feature-name
    ```
    or
    ```bash
    git checkout -b bugfix/your-bug-fix
    ```
2.  Make your changes and commit them with descriptive commit messages.
3.  Ensure all tests pass and your code adheres to our style guidelines.
4.  Push your branch to your fork.
5.  Open a pull request to the `main` branch of the upstream repository.
