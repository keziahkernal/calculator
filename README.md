# Calculator
A Python 3 calculator used from the Terminal, built step by step in SCCM4910.
## What it will do
Add, subtract, multiply and divide two numbers; display the result.
## How to run it
run: ./run.sh
Enter the first number, operator (+ - * /), then second number.
The program prints Result: followed by the answer.
## Testing
includes local tests, to run tests set up SCCM4910 env by 
source /opt/python-venv/sccm-4910/bin/activate then run ./check.sh in terminal
check exit status using echo $?, should return 0 to show all tests passed