<h1 align="center">Result Extractor</h1>

# What it does?

I made result extractor using Python and Selenium WebDriver Kit to fetch the results of all the students in one go, within a few minutes, and then export that to a clean tabular form into a CSV file.


## How to use it?
- Install Selenium WebDriver Kit into your PC and specify it's PATH in system environment variables if using Windows, or bash the command below in terminal if using MacOS.
```bash
pip install selenium
```
- Open the `data_2023.csv` and update the **Enrollment Number** and **Faculty Number** of the students in Comma Separated Values format. Save it.
- Open `main.py` and run the command as given below.
```bash
python3 main.py
```
- Let the automation do it's progress, and it'll automatically terminate after all the data has been extracted, and the following message will be displayed in the terminal.
```bash
Results have been extracted!
```
- The results will be exported in the `results_2023.csv` file, which can be later on converted into pdf format and viewed on any device.
