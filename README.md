# translator-backend
Django Rest APIs for translator project. The backend was deployed on AWS EC2 instance using Ubuntu 18.04, Nginx, Gunicorn running on port 8000.

The apis can be visited through this URL:　http://52.87.247.76:8000

## API ENDPOINTS
| Method | Endpoint | Purpose |
|--|--|--|
| GET | /restapi/translate/ | Returns an array of all the translation history. |
| GET | /restapi/translate/{id} | Returns an target translation record. |
| POST | /restapi/translate/ | Create a new translation; Save in the translation history table. Input param: {"input_text"} |
