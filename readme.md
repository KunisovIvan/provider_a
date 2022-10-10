# Simple Provider A Service


## Virtual Environment

0. Create Virtual Environment

    ```
    $ sudo apt install python3-pip python3-venv
    $ python3 -m venv .venv
    ```

1. Activate Virtual Environment

    ```
    source .venv/bin/activate
    ```

2. Install requirements

    ```
    (.venv)$ pip3 install --upgrade pip
    (.venv)$ pip install -r requirements.txt
    ```

## Run


Run the app with:

```
(.venv) $ uvicorn main:app --reload --port {APP_PORT}
```