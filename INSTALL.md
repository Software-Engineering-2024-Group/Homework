# Installation Instructions for SE24 Fall Homeworks Project
## Prerequisites

Before you begin, ensure you have the following software installed:

- [Git](https://git-scm.com/) (version control system)
- [Python](https://www.python.org/downloads/) (version 3.7 or above)
- [pip](https://pip.pypa.io/en/stable/) (Python package installer)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/) (optional but recommended for isolating dependencies)

## Step 1: Clone the Repository

1. Open your terminal or command prompt.
2. Clone the project repository using the following command:

   ```bash
   git clone https://github.com/Software-Engineering-2024-Group/Homework.git
## Step 2: (Optional) Set Up a Virtual Environment

Setting up a virtual environment ensures project dependencies are isolated.

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

3. To deactivate the virtual environment later, use:
   ```bash
   deactivate
   ```
## Step 3: Install Dependencies

To install all necessary dependencies, run the following command:

```bash
pip install -r requirements.txt

## Step 4: Running the Project

Once dependencies are installed, you can run the project. For example:

```bash
python main.py

## Troubleshooting

If you encounter any issues, consider the following:

- Ensure all prerequisites are installed.
- Verify that you are in the correct virtual environment by running:
  ```bash
  which python
  ```

- Re-run the installation commands if dependencies were not installed correctly.
