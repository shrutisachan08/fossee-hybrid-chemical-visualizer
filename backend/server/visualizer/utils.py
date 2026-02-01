import pandas as pd

def analyze_csv(file):
    df = pd.read_csv(file)
    df.columns = df.columns.str.strip().str.lower()

    return {
        "total_equipment": len(df),
        "avg_flowrate": round(df["flowrate"].mean(), 2),
        "avg_pressure": round(df["pressure"].mean(), 2),
        "avg_temperature": round(df["temperature"].mean(), 2),
       "type_distribution": df["type"].value_counts().to_dict(),
        "table_data": df.to_dict(orient="records")
    }
