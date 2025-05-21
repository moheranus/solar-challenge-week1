MoonLight Energy Solutions Dashboard

Overview

This Streamlit dashboard visualizes solar potential across Benin, Sierra Leone, and Togo, based on cleaned solar radiation datasets. It includes interactive features to compare GHI across countries and display top regions by average GHI.

Folder Structure





app/: Contains the Streamlit application.





main.py: Main Streamlit script for the dashboard.



utils.py: Utility functions (not implemented in this version).



data/: Stores cleaned CSVs (not committed, listed in .gitignore).



scripts/: Contains this README and other scripts.

Setup Instructions





Clone the repository:

git clone <repository_url>
cd <repository_name>



Install dependencies:

pip install streamlit pandas plotly



Run the Streamlit app:

streamlit run app/main.py



Deploy to Streamlit Community Cloud:





Push the repository to GitHub.



Connect to Streamlit Community Cloud, select app/main.py as the main script.



Ensure data/ contains benin-malaville_clean.csv, sierraleone-bumbubuna_clean.csv, and togo-dapaong-qc_clean.csv.

Usage





Country Selection: Use the sidebar to select one or more countries (Benin, Sierra Leone, Togo).



Visualizations:





GHI Boxplot: Displays GHI distribution by country.



Top Regions Table: Shows average GHI per country, sorted in descending order.



Navigation: Intuitive interface with clear labels and interactive widgets.

Notes





Ensure data/ is in .gitignore to avoid committing sensitive CSV files.



The app assumes cleaned CSVs are available locally in data/.



Commit message: git commit -m "feat: basic Streamlit UI".