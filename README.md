
## Features

- Predicts Bangalore home prices based on input features (location, area, BHK, etc.)
- Trained using a dataset of real Bangalore property listings
- Web app interface for easy predictions
- REST API backend using Flask

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

1. Clone the repository.
2. Navigate to `Prediction App/server/`.
3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
   *(Create `requirements.txt` if not present, with Flask, numpy, pandas, scikit-learn, etc.)*

### Running the Server

```sh
cd "Prediction App/server"
python server.py
