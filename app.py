from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the trained model using pickle
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# FastAPI app initialization
app = FastAPI()

# Define the request body model
class ShipmentData(BaseModel):
    Warehouse_block: int
    Mode_of_Shipment: int
    Customer_care_calls: int
    Customer_rating: int
    Cost_of_the_Product: float
    Prior_purchases: int
    Product_importance: int
    Gender: int
    Discount_offered: float
    Weight_in_gms: float

# Predict endpoint
@app.post("/predict")
def predict_shipment(data: ShipmentData):
    try:
        # Convert incoming data into a format the model expects
        input_data = [list(data.model_dump().values())]  # Use model_dump to extract values as list

        # Make prediction
        prediction = model.predict(input_data)

        # Return result as On-Time or Delayed
        result = "On-Time" if prediction[0] == 1 else "Delayed"

        return {"prediction": result}
    except Exception as e:
        # Log the error and raise HTTPException
        logger.error(f"Prediction failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Prediction failed")

