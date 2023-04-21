# Rick and Morty

### Requirements:
1. Endpoint, which return random character from the world of Rick and Morty series.
2. Endpoint get `search_string` as an argument and return list of all characters, 
   who contains the `search_string` in the name.
3. On regular basis, app downloads data from external service to inner DB.
4. Requests of implemented API should work with local DB
   (Take data from DB not from Rick & Morty API).

### Technologies to use:
1. Public API: https://rickandmortyapi.com/documentation.
2. Use Celery as task scheduler for data synchronization for Rick & Morty API.
3. Python, Django/Flask/FastAPI, ORM, PostgreSQL, Git.
4. All endpoints should be documented via Swagger.

### How to run:
- Copy .env.sample -> .env and populate with all required data
- `docker-compose up --build`
- Create admin user & Create schedule for running sync in DB
