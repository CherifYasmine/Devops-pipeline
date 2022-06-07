# Devops-pipeline

- I integrated a CI/CD pipeline using GitHub Actions, Docker and Amazon ECS.
- The main workflow consists of 3 jobs :
    1. Test
       - 3 parallel jobs: Tests on python 3.8, 3.9 and 3.10
    2. Build
       - A docker image is built and pushed to [Docker Hub](https://hub.docker.com/u/yasminecherif)
    3. Deploy
        - The image is deployed to ECS with a service of 3 tasks and exposed on port 5000.
  
    ### Pipeline:
    ![image](https://user-images.githubusercontent.com/59792971/172463353-6f6c614f-1fb5-4054-b964-655ccc58b999.png)
