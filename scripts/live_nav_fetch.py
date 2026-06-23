import requests
import pandas as pd

scheme_ids = {
    "HDFC_Top_100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, scheme_id in scheme_ids.items():
    url = f"https://api.mfapi.in/mf/{scheme_id}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        nav_data = pd.DataFrame(data["data"])

        nav_data.to_csv(
            f"data/raw/{name}_nav.csv",
            index=False
        )

        print(f"Saved {name}")