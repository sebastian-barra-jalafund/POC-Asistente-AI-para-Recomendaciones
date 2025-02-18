from fastapi import FastAPI, Query
import pandas as pd

app = FastAPI()

df = pd.read_csv("businesses.csv")

@app.get("/recommendations/")
def get_recommendations(preference: str = Query(..., title="Tipo de evento")):

    filtered_businesses = df[df['category'].str.contains(preference, case=False, na=False)]
    

    if not filtered_businesses.empty:
        return filtered_businesses.to_dict(orient="records")
    else:
        return {"message": "No se encontraron negocios para esta categoría."}
