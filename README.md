<p align="center">
  <img src="https://logos-world.net/wp-content/uploads/2024/10/Bkash-Logo.jpg" height="380" />
</p>


---

# bKash Payment Integration: Quick Start Guide

Welcome! This guide will help you set up and test the bKash payment flow in your local environment.
**Estimated setup time:** 5-10 minutes

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/zero-byte-git/Bkash-API.git
```
```bash
cd Bkash-API
```


---

## 2️⃣ Create a Python Virtual Environment

| Platform | Command |
| :-- | :-- |
| 🪟 Windows | `python -m venv env` |
| 🐧 Linux | `python3 -m venv env` |


---

## 3️⃣ Activate the Environment

| Platform | Command |
| :-- | :-- |
| 🪟 Windows | `env\Scripts\activate` |
| 🐧 Linux | `source env/bin/activate` |


---

## 4️⃣ Install Project Dependencies

```bash
pip install -r requirements.txt
```


---

## 5️⃣ Configure Environment Variables

1. Create a `.env` file in your project root.
2. Add the following (replace placeholders with your credentials):
```env
BKASH_APP_KEY=your_app_key
BKASH_APP_SECRET=your_app_secret
BKASH_USERNAME=your_username
BKASH_PASSWORD=your_password
BKASH_BASE_URL=https://tokenized.sandbox.bka.sh/v1.2.0-beta
BKASH_CALLBACK_URL=https://740e-118-179-44-184.ngrok-free.app/payment/callback/
```

> ⚠️ **Note:**
> - This example uses [ngrok](https://ngrok.com/) for local callback URLs.
> - Update the callback URL if your ngrok address changes.

---

## 6️⃣ Initiate a Payment (Using Postman)

- **Endpoint:**
`POST http://127.0.0.1:8000/payment/create/`
- **Request Body:**

```json
{
  "amount": "50.00",
  "invoice": "INV-1006"
}
```

- **Sample Success Response:**

```json
{
  "paymentID": "TR0011RsjP3mX1747579752377",
  "bkashURL": "https://sandbox.payment.bkash.com/?paymentId=TR0011RsjP3mX1747579752377&hash=...&mode=0011&apiVersion=v1.2.0-beta/",
  "callbackURL": "https://740e-118-179-44-184.ngrok-free.app/payment/callback/",
  "successCallbackURL": "...",
  "failureCallbackURL": "...",
  "cancelledCallbackURL": "...",
  "amount": "50.00",
  "intent": "sale",
  "currency": "BDT",
  "paymentCreateTime": "2025-05-18T20:49:12:377 GMT+0600",
  "transactionStatus": "Initiated",
  "merchantInvoiceNumber": "INV-1005",
  "statusCode": "0000",
  "statusMessage": "Successful"
}
```


---

## 7️⃣ Complete the Payment in Browser

1. Copy the `bkashURL` from the response.
2. Open it in your browser.
3. Follow the payment steps:
    - Enter phone number and OTP (should succeed).
    - Enter PIN (sandbox may fail here; this is expected).

---

## 8️⃣ Execute the Payment

- **Endpoint:**
`POST http://127.0.0.1:8000/payment/execute/`
- **Request Body:**

```json
{
  "paymentID": "TR0011RsjP3mX1747579752377"
}
```

- **Error Response (We are encountering this error in the response body):**

```json
{
  "statusCode": "2056",
  "statusMessage": "Invalid Payment State"
}
```
