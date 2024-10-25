# Bitstring Generator and Filter

## Description
A Python tool for generating and filtering binary bitstrings. Users can specify a bitstring length, generate all possible binary combinations, and apply custom filters to refine the generated set. This tool is ideal for anyone needing to work with binary sequences or test algorithms that involve binary data patterns.

### Requirements
- Python 3.10 or later

## Features
- Generate Bitstrings: Quickly generate all possible bitstrings of a specified length.
- Flexible Filtering Options:
    - Filter by Start: Remove bitstrings starting with a specified prefix.
    - Filter by End: Remove bitstrings ending with a specified suffix.
    - Filter by Subset: Remove bitstrings containing any specified binary pattern as a subset.

## Usage

1. Clone the repository
```
git clone https://github.com/Lee959/Bitstring-Generator.git
cd bitstring-generator-filter
```

2. Run the program
```
python main.py
```

### Main Menu
1. Generate bitstring:
2. Filter bitstring
    - Filter by Start
    - Filter by End
    - Filter by Subset
3. Exit program

### Example
```
Main Menu:
1. Generate bitstring
2. Filter bitstring
3. Exit program

Choose an option: 1
Enter the length of Bitstring: 3

Output:
B_3 = {0, 0, 0}, {0, 0, 1}, {0, 1, 0}, {0, 1, 1}, {1, 0, 0}, {1, 0, 1}, {1, 1, 0}, {1, 1, 1}
|B_3| = 8
```

> #### **Note**  
> Avoid using large numbers for bitstring length, as it will result in an exponential growth of possible combinations. Large bitstring lengths (e.g., 20 or above) may cause performance issues or excessive memory usage.
