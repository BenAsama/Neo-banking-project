from fastapi import FastAPI

class user:
  user_id: int
  first_name : str
  last_name : str
  other_names: str
  email: str #validate the email is a type of email and 
              #also validate the email in the signup with a code if possible
  mobile_number: int #with country code in the front end
  gender: str
  address: str
  country: str 
  state: str
  city: str
  nationality: str
  occupation: str
  date_of_birth: str
  marital_status: str

  password: str
  signature: id

  account_number: int
  account_balance: float
  account_password: str

