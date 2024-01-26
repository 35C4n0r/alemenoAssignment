# Alemeno Assignment

## Info
I have used Django, Celery & Redis in this application. I have dockerized the entire thing.

```shell
docker-compose up --build
```
Then go to `http://localhost:8000/celery`

## Endpoints

    'celery/' --> 'Run this initially, this will ingest the xlsx data to postgres'
    'register/' --> Register user
    'check-eligibility/' --> Checks if a customer is eligible for loan
    'create-loan/' --> Create a new loan for a customer
    'view-loan/<int:loan_id>/' --> Check the info of specific loan
    'view-loans/<int:customer_id>' --> See the loan of all the customer