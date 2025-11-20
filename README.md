# DAP - Data Analytics Pipeline CLI

A command-line interface for managing and streamlining data analytics projects.

## Getting Started

### Prerequisites

- Python 3.8+

### Installation

Clone the repository and install the package in editable mode:

```bash
git clone https://github.com/your-username/da-pipeline.git
cd da-pipeline
pip install -e .
```

## Usage

### Create a New Project

To create a new data analytics project, use the `dap new` command:

```bash
dap new my-awesome-project
```

This will create a new directory named `my-awesome-project` inside a `projects/` directory with the following structure:

```
projects/
└── my-awesome-project/
    ├── README.md
    ├── config/
    │   └── .gitkeep
    ├── data/
    │   └── .gitkeep
    ├── notebooks/
    │   └── .gitkeep
    └── src/
        └── .gitkeep
```
