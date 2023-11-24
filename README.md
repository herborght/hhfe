# hhfe

## Getting Started

Follow these steps to set up and run the Tonality Test repository:

### Prerequisites

Make sure you have Python installed on your system.

### 1. Create a Virtual Environment

To manage project dependencies, it's recommended to create a virtual environment. Run the following command:

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

Activate the virtual environment:

```bash
./venv/Source/activate
```

### 3. Install Required Packages

Install the required Python packages specified in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

Create a .env file to securely store your API keys for OpenAI and SerpAPI. Different methods for Windows/Linux/macOS:

### Windows

```bash
New-Item -ItemType File .env
```

### Unix/Linux/macOS

```
touch .env
```

Edit the .env file and add your API keys as follows:

```plaintext
OPENAI_API_KEY=your_openai_api_key
SERPAPI_API_KEY=your_serpapi_api_key
```

### 5. Run the Streamlit Frontend

Start the Streamlit frontend interface with the following command:

```
streamlit run analyse.py
```

### 6. Upgrade packages 

To update dependencies and the pip env: 

```
pip install -r requirements.txt -U 
```


### Optinal: When finished, enable venv

To disable virtual environment simply type 

``` 
deactivate
```

To delete the virtual environment

```
rm -r venv  
```