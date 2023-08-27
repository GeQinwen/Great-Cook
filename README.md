# Great Cook

The `Great Cook` is a simple web application built on Streamlit and OpenAI. It aims to provide cooking method suggestions and recipe recommendations based on the ingredients input by the user.

## Features

- **Ingredient Input**: Allows users to input the ingredients they have on hand.
  
- **Cooking Method Generation**: Based on the ingredients provided by the user, the app generates potential cooking methods.
  
- **Recipe Generation**: Using the same ingredient input, the app suggests recipes that can be made.

## Requirements

- Python 3.x
- Streamlit
- Langchain library (for OpenAI interactions)

## Setup & Installation

1. **Clone the Repository**: 
   
   ```bash
   git clone https://github.com/GeQinwen/Great-Cook.git
   cd Great-Cook
   ```

2. **Install the Dependencies**:

   ```bash
   pip install streamlit langchain
   ```

3. **Run the App**:

   ```bash
   streamlit run great_cook.py
   ```

   This will open a new browser window/tab with the application running.

## Usage

1. In the application's main interface, you'll find a text area to input your ingredients.
   
2. After inputting your ingredients, the application will automatically generate cooking methods and recipes that utilize the given ingredients.

3. Browse through the suggestions and get cooking!

## Contributions

Feel free to fork this project and make your own changes. If you have any suggestions or improvements, pull requests are always welcome!

