# Apollo Contacts Export

This project reads and processes contact data from the `apollo-contacts-export.csv` file.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up the project, ensure you have Python installed. You can install any required dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

To read the contacts from the CSV file, you can use the following code snippet:

```python
import csv

with open('apollo-contacts-export.csv', 'r') as file:
    csvreader = csv.reader(file)
    
    # Read the header
    header = next(csvreader)
    print("Header:", header)
    
    # Read each row
    for row in csvreader:
        print(row)
```

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
