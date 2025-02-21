# JSON Toolkit

A versatile Python toolkit for working with JSON data. It includes features for streaming large JSON files, filtering and transforming data, converting to different formats, exporting data, and performing advanced JSON analysis.

## Features

- **Streaming**: Efficiently stream large JSON files without loading everything into memory.
- **Filtering**: Filter JSON data based on keys or key-value pairs.
- **Conversion**: Convert JSON data to various formats like CSV and XML.
- **Export**: Export JSON data to multiple formats including CSV and XML.
- **Analysis**: Analyze JSON data for statistical insights and more.

### Installation
 

1. Clone the repository:
    ```bash
    git clone https://github.com/Jenderal92/json_toolkit.git
    cd json_toolkit
    ```

2. Install the package:
    ```bash
    pip install .
    ```

## Usage

### Stream Large JSON

```python
from json_toolkit import JSONStreamer

def process_large_json(file_path):
    streamer = JSONStreamer(file_path)
    for data in streamer.stream():
        # Process each chunk of JSON data
        print(data)

process_large_json('large_data.json')
```

### Convert JSON to CSV

```python
from json_toolkit import JSONConverter

def convert_json_to_csv(json_data):
    JSONConverter.json_to_csv(json_data, 'output.csv')

data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
convert_json_to_csv(data)
```

### Filter JSON Data

```python
from json_toolkit import JSONFilter

def filter_json_by_key(json_data, key):
    return JSONFilter.filter_by_key(json_data, key)

data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
filtered_data = filter_json_by_key(data, 'name')
print(filtered_data)
```

## Development

To set up the development environment:

1. Clone the repository:
    ```bash
    git clone https://github.com/Jenderal92/json_toolkit.git
    cd json_toolkit
    ```

2. Set up the environment:
    ```bash
    ./scripts/setup_env.sh
    ```

3. Install development dependencies:
    ```bash
    pip install -r requirements-dev.txt
    ```

4. Run tests:
    ```bash
    ./scripts/run_tests.sh
    ```

## Contributing

We welcome contributions to this project. If you'd like to contribute, please fork the repository, create a new branch, and submit a pull request. Make sure to follow the code style guidelines, write tests, and update the documentation as necessary.

For detailed instructions, please see [CONTRIBUTING.md](docs/CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by various open-source JSON processing tools.
- Thanks to all contributors and the open-source community.


---

This `README.md` includes the following sections:

1. **Project Overview**: A brief description of what the toolkit does.
2. **Features**: Highlights the main functionalities.
3. **Installation**: Instructions for installing the toolkit from PyPI or from source.
4. **Usage**: Examples of how to use different features of the toolkit (streaming, conversion, filtering).
5. **Development**: Guidelines for setting up a development environment and running tests.
6. **Contributing**: Encouragement for external contributions.
7. **License**: Information about the project's license (MIT License in this case).

Feel free to modify or add any other sections as needed!
