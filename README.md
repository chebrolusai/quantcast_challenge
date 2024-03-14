<h1 align="center">Quantcast Coding Challenge</h1>

A command line program in python which processes files and returns the most active cookie for a specified day.

<h5>Built with: </h5>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">

### About

Given a log file in the format `cookie,timestamp` , the program parses the log file and returns token/tokens which have the most occurances on a specific day. The date and the file to process are given as input to the program through CLI.

### Prerequisites

- python installed

### Project Structure

- <b>most_active_cookie</b> : The main python file to execute
- <b>util</b> : A helper/utility file for the main
- <b>data_integrity</b> : A basic file for error reporting
- <b>tests </b>: A directory with unit tests scripts for the main file

### Usage

Depending on the Operating System:

```sh
python3 most_active_cookie.py <file_path> -d <date>
```

or

```sh
python most_active_cookie.py <file_path> -d <date>
```
