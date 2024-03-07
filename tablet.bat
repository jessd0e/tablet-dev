@ECHO OFF

echo Hello World!
::"C:\Users\Jessica Doe\Documents\Python\tablet-dev.venv\Scripts\activate.bat" "C:\Users\Jessica Doe\Documents\Python\tablet-dev.venv\" & streamlit run "C:\Users\Jessica Doe\Documents\Python\tablet-dev\app\app.py" --server.port 8501
call "C:\Users\jessi\tablet-dev\venv\Scripts\activate.bat"
streamlit run "C:\Users\jessi\tablet-dev\app\app.py" --server.headless true --server.port 8501
