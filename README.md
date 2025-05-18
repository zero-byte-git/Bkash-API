How To Run:
- Clone the Repository
- Create python environment by giving this command   Windows:python -m venv env Linux:python3 -m venv env
- Activate the environment by giving this command Windows: env/Scripts/activate  Linux: source env/bin/activate
- Install the requirements.txt file  pip install -r requirements.txt
- Create a .env file consisting these things.

* BKASH_APP_KEY=Use yours
* BKASH_APP_SECRET=Use yours
* BKASH_USERNAME=Use yours
* BKASH_PASSWORD=Use yours
* BKASH_BASE_URL=https://tokenized.sandbox.bka.sh/v1.2.0-beta
* BKASH_CALLBACK_URL=https://740e-118-179-44-184.ngrok-free.app/payment/callback/   This is a local development envrionment thus we are using ngrok for callback


-Open Postman
-Try this endpoint
-http://127.0.0.1:8000/payment/create/
-Request Body
{
  "amount": "50.00",
  "invoice": "INV-1006"
}
-You should get a response like this.
{
    "paymentID": "TR0011RsjP3mX1747579752377",
    "bkashURL": "https://sandbox.payment.bkash.com/?paymentId=TR0011RsjP3mX1747579752377&hash=Ymnp!W*MhlwsNf2mE6T8yitwcpWU5dFezqHZu41Zbuizr7lSyl9zPhJ!yxZ1rwUkuMPR_UF!o4A7ATHPmTyFF1Y3iJoPRkd-R6.X1747579752377&mode=0011&apiVersion=v1.2.0-beta/",
    "callbackURL": "https://740e-118-179-44-184.ngrok-free.app/payment/callback/",
    "successCallbackURL": "https://740e-118-179-44-184.ngrok-free.app/payment/callback/?paymentID=TR0011RsjP3mX1747579752377&status=success&signature=jLN0zbOpph",
    "failureCallbackURL": "https://740e-118-179-44-184.ngrok-free.app/payment/callback/?paymentID=TR0011RsjP3mX1747579752377&status=failure&signature=jLN0zbOpph",
    "cancelledCallbackURL": "https://740e-118-179-44-184.ngrok-free.app/payment/callback/?paymentID=TR0011RsjP3mX1747579752377&status=cancel&signature=jLN0zbOpph",
    "amount": "50.00",
    "intent": "sale",
    "currency": "BDT",
    "paymentCreateTime": "2025-05-18T20:49:12:377 GMT+0600",
    "transactionStatus": "Initiated",
    "merchantInvoiceNumber": "INV-1005",
    "statusCode": "0000",
    "statusMessage": "Successful"
}

-Copy the bkashURL from the response body and try to create a succesfull payment. We are getting failed after giving the PIN. The phone number and OTP are going through succesfully.

-After that try this endpoint
-http://127.0.0.1:8000/payment/execute/

{
  "paymentID": "TR0011RsjP3mX1747579752377"
}
-We are getting this in the response body
{
    "statusCode": "2056",
    "statusMessage": "Invalid Payment State"
}

