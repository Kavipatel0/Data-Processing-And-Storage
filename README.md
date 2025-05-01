# In-Memory Database with Transaction Support

This project implements an in-memory key-value database in Python that supports transactions, as described in the Extra Credit Data Processing and Storage Assignment.

## How to Run

1. Ensure you have Python 3 installed.  
2. Save the code into a file named `DataProcessing.py`.  
3. Open a terminal, navigate to the correct directory, and run the following command:

```bash
python3 DataProcessing.py
```

This will execute the database operations and print the results based on the assignment's expected behavior.

## Assignment Improvements

To make this an official assignment in the future, several improvements could be made to enhance clarity and grading efficiency. Including a few sample test cases would help students verify their output and understand whether their program is functioning correctly. The instructions should explicitly confirm that the `get()` function must not return uncommitted changes, as this detail may be unclear to some students. Additionally, the assignment documentation would benefit from adopting the format used in previous assignments. This would help ensure consistency throughout the course and make the requirements easier to follow. Overall, this assignment serves as a valuable introduction to transaction handling in an in-memory database.
