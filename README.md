# SE221Microservices

### How to start the app

1. **Get an API Key:**

    - Sign up for an API key from OpenAQ.
    - Once you have your API key, create a `.env` file in the root directory of your project and add the following line to it:
    
    ```env
    OPENAQ_KEY=your_openaq_api_key
    ```

2. **Create a virtual environment:**

    ```sh
    python3 -m venv venv
    ```

3. **Activate the virtual environment:**

    - **For Bash:**
    
        ```sh
        source venv/bin/activate
        ```

    - **For PowerShell:**
    
        ```sh
        .\venv\bin\Activate.ps1
        ```

4. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

5. **Run the app:**

    ```sh
    python main.py
    ```

6. **Test the app:**

    Open your browser or use a tool like `curl` or `Postman` to make a GET request to:

    ```
    http://127.0.0.1:5000/air-quality?city=<city_name>
    ```

    Replace `<city_name>` with the name of the city you want to check the air quality for. Not every city has a station, you could test e.g., Tampere, Helsinki or Kolkata. You can find all stations from https://explore.openaq.org