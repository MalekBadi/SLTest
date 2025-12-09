# Temperature Converter 🌡️

A simple Streamlit web application for converting temperatures between Fahrenheit and Celsius.

## Features

- Convert Fahrenheit to Celsius
- Convert Celsius to Fahrenheit
- Real-time conversion as you type
- Clean and intuitive user interface

## Requirements

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) for package management

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd SLTest
```

2. Install dependencies using uv:
```bash
uv sync
```

## Usage

Run the Streamlit app:
```bash
uv run streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`

## Project Structure

```
SLTest/
├── main.py           # Main Streamlit application
├── pyproject.toml    # Project dependencies and metadata
├── uv.lock          # Lock file for reproducible builds
└── README.md        # This file
```

## License

MIT

