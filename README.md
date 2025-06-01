# Daxa - Python Edition

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<!-- Add build status, coverage badges etc. once CI is set up -->
<!-- ![Build Status](...) -->

![Daxa Logo](./assets/logo.png) <!-- Assuming logo.png is in assets -->

**Daxa: The Ultimate Data Storage Language & Virtual File System (Python Implementation)**

This repository contains the Python implementation of Daxa, a powerful data storage language designed for flexibility, human-readability, and efficient data representation. This version also introduces **DexFS**, a virtual file system built on top of Daxa, allowing structured data and arbitrary file content to be organized within Daxa files.

Crafted with ❤️ by **Lion** ([@lionxlover](https://github.com/lionxlover)).
Connect with me: [Telegram](https://t.me/lionxlover) | [Instagram](https://www.instagram.com/lionxlover)

## Features

*   **Rich Type System:** Supports primitives (integers, floats, bool, string, bytes, datetime, UUID), structs, enums, arrays, maps, and an `any` type for maximum flexibility.
*   **Schema Definition:** Define data structures with a clear, concise Daxa schema syntax.
    *   Field constraints: `@minLength`, `@maxLength`, `@minValue`, `@maxValue`, `@pattern`.
    *   Type aliasing for cleaner schemas.
    *   Optional fields and default values.
*   **Text Format (`.daxa`):** Human-readable and editable.
    *   Clear separation of schema and data blocks.
    *   Support for comments and simple attributes.
*   **Binary Format (`.dax`):** Stubbed for future high-performance, compact storage (serialization logic to be fully implemented).
    *   Conceptual support for compression (Zstd, LZ4) and encryption (AES-256-GCM).
*   **Diagramming Capabilities:**
    *   Embed diagram definitions directly within Daxa files.
    *   Support for `source_dsl` (e.g., Mermaid, Graphviz DOT) and `structured_data` for diagrams.
    *   Renderers for Graphviz and Mermaid (via Pyppeteer).
*   **DexFS - Daxa Virtual File System:**
    *   Store hierarchical file and directory structures within a Daxa dataset.
    *   Files in DexFS can hold any `DaxaValue` as their payload (text, binary, complex Daxa structs).
    *   POSIX-like metadata (permissions, timestamps, owner - simplified).
    *   API and CLI for VFS operations (ls, mkdir, cat, put, rm, mv, stat).
*   **Command-Line Interface (CLI):**
    *   `daxa info`: Display summary of Daxa files.
    *   `daxa validate`: Validate data against schema.
    *   `daxa convert`: Convert between Daxa text and (eventually) binary formats, and to/from other formats (JSON, YAML).
    *   `daxa diagram render`: Render embedded diagrams to various output formats (SVG, PNG).
    *   `daxa fs ...`: A suite of commands to interact with DexFS instances.
    *   (Planned: `daxa query`, `daxa schema export`)
*   **Graphical User Interface (GUI):**
    *   Built with PyQt6 for a modern, cross-platform experience.
    *   Schema Explorer: Navigate struct, enum, and type alias definitions.
    *   Data Viewer: Inspect top-level datasets (raw text, JSON-like tree for complex data).
    *   Diagram Viewer: Display rendered diagrams.
    *   DexFS Browser: Navigate and manage files/directories within DexFS instances.
    *   Property Editor: View details of selected schema items, data entries, or FS nodes.
    *   Console Output: For logs, validation errors, and messages.
    *   Theming support (basic light/dark themes via QSS).
    *   Background threading for responsive UI during file loading and other long operations.
    *   Application preferences and window state persistence.
*   **Database Utilities (Conceptual):**
    *   Stubs for mapping Daxa schemas to SQL DDL or ORM models.
    *   Stubs for exporting Daxa data to database-friendly formats.

## Project Structure

(A brief overview of the tree view from the previous prompt, focusing on `daxa/core`, `daxa/fs`, `daxa/cli`, `daxa/gui`)

```
daxa_python/
├── daxa/              # Main Daxa package
│   ├── core/          # Language core (parser, schema, value, validator, writers)
│   ├── fs/            # DexFS virtual file system logic
│   ├── cli/           # Command-line interface
│   ├── gui/           # Graphical user interface
│   ├── renderers/     # Diagram rendering engines
│   ├── db_utils/      # Database utilities (stubs)
│   └── ...
├── assets/            # Icons, logos, stylesheets
├── examples/          # Example .daxa files
├── tests/             # Unit and integration tests
└── ...
```

## Getting Started

### Prerequisites

*   Python 3.9+
*   Graphviz (for diagram rendering - install system-wide: `apt-get install graphviz` or `brew install graphviz`)
*   A Chromium-based browser (for Mermaid rendering via Pyppeteer, will be downloaded by Pyppeteer if not found/configured).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/lionxlover/daxa_python.git # Replace with your actual repo URL
    cd daxa_python
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Install Daxa in editable mode:**
    This makes the `daxa` CLI and `daxa-gui` scripts available in your environment.
    ```bash
    pip install -e .
    ```

### Usage

#### Command-Line Interface (CLI)

Show help:
```bash
daxa --help
daxa fs --help
```

Inspect a Daxa file:
```bash
daxa info examples/my_virtual_fs.daxa
```

Validate a Daxa file:
```bash
daxa validate examples/my_virtual_fs.daxa
```

Render a diagram from a Daxa file:
```bash
# Assuming simple_diagram.daxa has a diagram dataset named 'my_flow'
daxa diagram render examples/simple_diagram.daxa my_flow -o output_flow.svg
```

**DexFS CLI Examples:**

Initialize a new DexFS within `new_fs.daxa` under the dataset name `main_fs`:
```bash
daxa fs init new_fs.daxa::main_fs --label "My Main VFS" --save
```

List root of `main_fs` in `new_fs.daxa`:
```bash
daxa fs ls new_fs.daxa::main_fs::/
```

Create a directory:
```bash
daxa fs mkdir new_fs.daxa::main_fs::/documents --save
```

Put a local file into DexFS:
```bash
echo "Hello DexFS" > local_hello.txt
daxa fs put local_hello.txt new_fs.daxa::main_fs::/documents/hello.txt --type string --save
```

Cat a file from DexFS:
```bash
daxa fs cat new_fs.daxa::main_fs::/documents/hello.txt
```

Remove a file:
```bash
daxa fs rm new_fs.daxa::main_fs::/documents/hello.txt --save
```

#### Graphical User Interface (GUI)

Launch the Daxa GUI:
```bash
daxa-gui
```
Or, if the `gui_scripts` entry point isn't working (e.g., during development without full install):
```bash
python -m daxa.gui.main_window
```
The GUI allows opening `.daxa` files, exploring their schema, viewing data, rendering diagrams, and browsing embedded DexFS instances.

## Development

*   **Type Checking:** `mypy daxa/ tests/`
*   **Linting/Formatting:** `ruff check . && ruff format .` (or your preferred tools like Black, Flake8)
*   **Testing:** `pytest`

(Details on how to run tests would go here.)

## Roadmap & Future Enhancements

This Python implementation is a comprehensive foundation. Future work could include:

*   **Full Binary Format Implementation:** Complete serialization/deserialization for `.dax` files.
*   **Advanced Parser:** Replace the regex/state-based text parser with a robust parser generator library (e.g., Lark) for better error handling, performance, and maintainability with complex Daxa syntax.
*   **Performance Optimization:** For large file handling, parsing, and VFS operations.
*   **Enhanced DexFS Features:**
    *   Permissions model refinement.
    *   Symbolic links.
    *   Efficient search/indexing within DexFS.
    *   Snapshotting capabilities.
*   **Schema Evolution/Migration Tools:** For managing changes to Daxa schemas over time.
*   **Full Database Utility Implementation:** Concrete DDL/ORM generation and data import/export tools.
*   **Daxa Language Server Protocol (LSP):** For IDE integration (syntax highlighting, auto-completion, validation in editors like VS Code).
*   **Plugin System:** Allow extending Daxa with custom renderers, validators, or data handlers.
*   **Web Interface/API:** For accessing and managing Daxa data and DexFS instances over HTTP.
*   **Advanced GUI Features:** True data editing, schema design tools, collaborative features (ambitious).

## Contributing

Contributions are welcome! If you're interested in contributing, please feel free to:
1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes.
4.  Add tests for your changes.
5.  Ensure all tests pass and linters/formatters are happy.
6.  Submit a pull request with a clear description of your changes.

(Consider adding a `CONTRIBUTING.md` file for more detailed guidelines).

## License

Daxa Python Edition is licensed under the [MIT License](./LICENSE).

---

*This project is a labor of love and an exploration into building a comprehensive data language and virtual file system. Your feedback and contributions are highly appreciated!*

**Lion ([@lionxlover](https://github.com/lionxlover))**