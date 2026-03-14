# Week 1 Log

## What I installed
- Miniconda
- Conda environment: `embodied`
- Jupyter Notebook inside the `embodied` environment

## What worked
- `python3 --version` worked before Conda
- `git --version` worked
- `code --version` worked
- `jupyter notebook --version` worked
- Miniconda installed successfully
- Conda activated correctly
- `python` worked after activating Conda
- Project folders and research log were created

## What broke
- `python` command was missing before Conda
- `conda` was not installed at first
- Terminal started showing `(base)` after Miniconda install, which was confusing

## What I am confused about
- Difference between `python` and `python3`
- Difference between system Python and Conda Python
- What it means to create a Conda environment
- Why `python` started working after activating Conda
- What silent mode means
- What dry run means

## Concise answers

### Difference between `python` and `python3`
- `python3` explicitly runs Python 3
- `python` runs whatever executable named `python` is currently available
- On my machine, `python3` worked before Conda, but `python` did not
- After activating Conda, `python` worked because Conda provided its own Python executable

### Difference between system Python and Conda Python
- System Python is the Python already available on the machine
- Conda Python is a separate Python installed inside a Conda environment
- Conda Python is isolated, so packages for one project do not interfere with other projects

### What it means to create a Conda environment
- It means making a separate Python workspace for one project
- That workspace has its own Python version and its own installed packages

### Why `python` started working after activating Conda
- Activating Conda changed the shell so it used the Python inside the Conda environment
- That environment includes a `python` executable

### What silent mode means
- Run an installer or command with little or no prompts
- Usually it asks fewer questions and shows less output

### What dry run means
- Simulate an action without actually making changes
- Useful for checking what a command would do before running it for real

### Why we used Miniconda instead of Anaconda
- Miniconda is smaller and cleaner
- Anaconda installs many extra packages by default
- For a simple research setup, Miniconda is easier to control