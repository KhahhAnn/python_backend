from pydantic import BaseModel

class VnpayPaymentResponse(BaseModel):
    status: str
    message: str
    URL: str