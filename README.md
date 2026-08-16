# Student Result Prediction

This repository contains a Streamlit app (`App.py`) that predicts student exam scores using a pre-trained model (`best_model.pkl`).

Quick steps to publish to GitHub and deploy on Streamlit Community Cloud:

1. Initialize git and commit your files (run from the project folder):

```bash
git init
git add .
git commit -m "Initial commit: add Streamlit app and model"
```

2. Create a GitHub repository (via web) and follow the instructions to add the remote, for example:

```bash
git remote add origin https://github.com/<your-username>/<repo-name>.git
git branch -M main
git push -u origin main
```

3. Ensure `best_model.pkl` is included in the repository (it's required by `App.py`).

4. On Streamlit Community Cloud:
- Sign in at https://share.streamlit.io
- Click **New app** → select your GitHub repo and branch (`main`)
- Set the main file to `App.py` and deploy

5. If you need to update dependencies, edit `requirements.txt` and push changes — Streamlit will rebuild.

Local run (for testing):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run App.py
```

If you want, I can create the Git history locally and show the exact git commands to run. Let me know if you want me to do that.
