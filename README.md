# Employee Task Tracker API Script

This Python script interfaces with the JSON Placeholder API to fetch and display the task completion status of employees based on their ID. It provides a quick overview of how many tasks each employee has completed out of the total assigned tasks.

## Features

- Fetches data from the JSON Placeholder API.
- Outputs the task completion status for a specified employee.
- Exits gracefully if no data is found for the given employee ID.

## Installation

### Prerequisites

Before running this script, ensure you have Python installed on your system. Python 3.6 or higher is recommended. You can download it from [python.org](https://www.python.org/downloads/).

### Dependencies

This project requires the `requests` library to send HTTP requests. You can install this package using pip:

pip install requests

## Usage

To run the script, use the following command in the terminal:

python employee_tasks.py <employee_id>


Replace `<employee_id>` with the actual ID of the employee whose task status you want to check.

### Example

python employee_tasks.py 4


This command will output the task completion status of the employee with ID 4.

## Output Format

The output format of the script is as follows:

Employee <employee_name> is done with tasks(<completed_tasks>/<total_tasks>):
<task_title_1>
<task_title_2>
...


Each completed task will be listed under the summary.


## Author

- Javier Ferrer

## Acknowledgments

- JSON Placeholder for providing a free API to use for this project.
