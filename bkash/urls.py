from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="bKash Payment API",
        default_version="v1",
        description="""
## 🎓 School Reunion bKash Payment API

This API allows users to register for the school reunion event and pay using the bKash payment gateway. Below is the full flow:

---

### 🦾 1. Register User Data

### Fields Description with Choices:
- **ssc_batch**: SSC passing year.
  - Choices: 1997 to 2025 (e.g., "1997", "1998", ..., "2025")

- **t_shirt_size**: T-shirt size for the attendee.
  - Choices: XS, S, M, L, XL, XXL

- **family_members**: Number of family members attending.
  - Choices:
    - 0: None
    - 1: One
    - 2: Two
    - 3: Three
    - 4: Four

- **cultural_event**: Participation in cultural event.
  - Choices:
    - "" (empty string): No Participation
    - "song": গান
    - "dance": নাচ
    - "comedy": কৌতুক
    - "drama": নাটক
    - "recitation": আবৃত্তি

**Endpoint:** `POST /payment/user-data/create/`  
Create a user entry with personal and payment information.

**Example Request Body:**
```json
{
  "name": "Walid",
  "email": "walid@example.com",
  "phone": "017XXXXXXXX",
  "ssc_batch": "2015",
  "t_shirt_size": "M",
  "family_members": 2,
  "cultural_event": "song",
  "invoice": "INV123456",
  "amount": 1000.00
}
```

---

### 💳 2. Create bKash Payment

**Endpoint:** `POST /payment/create/`  
Initiate a bKash payment session.

**Example Request Body:**
```json
{
  "amount": 1000.00,
  "invoice": "INV123456"
}
```

---

### ✅ 3. Execute bKash Payment

**Endpoint:** `POST /payment/execute/`  
Finalize the payment session after user authorization.

**Example Request Body:**
```json
{
  "paymentID": "abc123token"
}
```

---

### 🔍 4. Query Payment Status

**Endpoint:** `POST /payment/query/`  
Check the current status of a payment.

**Example Request Body:**
```json
{
  "paymentID": "abc123token"
}
```

---

### 🔗 API Endpoints Summary

| Endpoint | Method | Description |
|---------|--------|-------------|
| `/payment/user-data/create/` | POST | Register user data |
| `/payment/user-data/` | GET | List all user data |
| `/payment/create/` | POST | Create a bKash payment |
| `/payment/execute/` | POST | Execute a bKash payment |
| `/payment/query/` | POST | Query a bKash payment |

""",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("payment/", include("payment.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
