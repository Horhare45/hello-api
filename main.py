from fastapi import FastAPI, Request
from datetime import datetime
from logging_config import get_logger, generate_request_id

app = FastAPI(title="Customer Support Greeting API")

logger = get_logger("customer-support-service")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_id = generate_request_id()
    logger.info(f"[{request_id}] Incomming request: {request.method} {request.url}")
    
    response = await call_next(request)
    
    logger.info(f" [{request_id}] Response status:  {response.status_code}")

                   
    return response

@app.get("/")
def support_greeting():
    
    return {"services": "Customer Support Greeting API",
    "message": "Welcome to our support Service. How can we assist you today?",
    "timestamp": datetime.now().isoformat()}

@app.get("/greet/{customer_name}")
def greet_customer(customer_name: str):
    return {
        "message": f"Hello, {customer_name}, our support team is ready to help you",
        "timestamp": datetime.utcnow().isoformat()
    }

    

    

@app.get("/health")
def health_check():
    logger.info("Health check called")
    return {"status": "OK", "service": "customer-support-api"}
    
