import subprocess

if __name__ == "__main__":
    subprocess.Popen(["uvicorn", "src.api:app", "--reload"])
    subprocess.Popen(["streamlit", "run", "src/ui.py"])