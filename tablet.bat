@ECHO OFF

call "C:\Users\jessi\tablet-dev\venv\Scripts\activate.bat"
streamlit run "C:\Users\jessi\tablet-dev\app\app.py" --server.headless true --server.port 8501
