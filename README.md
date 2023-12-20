## Features
- Auth (register, login, password reset, verify user, get access tokens)
- Search (elastic search)
- Bookmarking 
- Follow / unfollow
- Responses
- Update profile

## Frameworks
1. Backend: Django, Django Rest Framework
2. CICD: Dockerfile (multistage builds)

docker-compose -f .\docker-compose.yaml config
docker-compose -f .\docker-compose.yaml up -d --build --remove-orphans
