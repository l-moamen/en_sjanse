Just a hacky fast API implemntation hosted on replit for an MVP, don't take it too seriously 

Project structure
EnSjanse/  
├── app/  
│   ├── __init__.py  
│   ├── main.py                 # Entry point, routes only    
│   ├── routers/                # All API routes grouped together  
│   │   ├── __init__.py  
│   │   ├── auth_router.py      # Routes for authentication  
│   │   ├── profiles_router.py  # Routes for profile management  
│   │   ├── content_router.py   # Routes for content service  
│   │   ├── search_router.py    # Routes for search functionality  
│   │   ├── events_router.py    # Routes for event management  
│   │   ├── social_router.py    # Routes for social interactions  
│   │   ├── ticketing_router.py # Routes for ticketing  
│   │   ├── subscriptions_router.py # Routes for subscription management  
│   │   └── admin_router.py     # Routes for admin service  
│   ├── services/               # Business logic grouped together  
│   │   ├── __init__.py  
│   │   ├── auth_service.py     # Logic for authentication  
│   │   ├── profiles_service.py # Logic for profile management  
│   │   ├── content_service.py  # Logic for content aggregation  
│   │   ├── search_service.py   # Logic for search operations  
│   │   ├── events_service.py   # Logic for event booking flow  
│   │   ├── social_service.py   # Logic for comments, reviews, and engagement  
│   │   ├── ticketing_service.py # Logic for ticketing and payments  
│   │   ├── subscriptions_service.py # Logic for subscription plans and billing  
│   │   └── admin_service.py    # Logic for admin-level operations  
│   ├── models/                 # Pydantic models grouped together  
│   │   ├── __init__.py  
│   │   ├── auth_models.py      # Models for authentication    
│   │   ├── profiles_models.py  # Models for profile data  
│   │   ├── content_models.py   # Models for content service  
│   │   ├── search_models.py    # Models for search functionality  
│   │   ├── events_models.py    # Models for event management  
│   │   ├── social_models.py    # Models for social interactions  
│   │   ├── ticketing_models.py # Models for ticketing  
│   │   ├── subscriptions_models.py # Models for subscriptions  
│   │   └── admin_models.py     # Models for admin operations  
│   ├── utils/                  # Common utilities and helpers  
│   │   ├── __init__.py  
│   │   ├── validators.py       # Custom validators    
│   │   ├── config.py           # Configuration loader  
│   │   └── logger.py           # Centralized logging  
├── data/                       # Data storage layer  
│   ├── venues.json  
│   └── other_datasets.json  
├── tests/                      # Test suite  
│   ├── __init__.py  
│   ├── test_auth.py  
│   ├── test_profiles.py  
│   ├── test_content.py         # Tests for the Content Service  
│   ├── test_search.py  
│   └── ...                     # Other test modules  
├── pyproject.toml              # Dependency management  
└── README.md                   # Project documentation  



run app: uvicorn app.main:app --reload --port 8000  

todos: find venue by type, performer by type or supported genre, we'll see  
