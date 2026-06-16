from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="Customer Support Greeting API")

@app.get("/")
def support_greeting():
    
    return {"services": "Customer Support Greeting API",
    "message": "Welcome to our support Service. How can we assist you today?",
    "timestamp": datetime.now().isoformat()}

@app.get("/greet/{customer_name}")
def greet_customer(customer_name: str):
    return {"message": f"Hello, {customer_name}, our support team is ready to help you",
    "timestamp": datetime.now().isoformat()
    }

@app.get("/health")
def health_check():
    return {"status": "OK", "service": "customer-support-api"}
    