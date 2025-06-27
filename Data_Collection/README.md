# Assessment: Data Collection
This directory contains my work toward the data collection assessment.

# How to run
Start Docker.
`docker compose up -d --build`
This should start both the front end and the backend.
You can access the frontend at http://localhost:3000
The backend is on port 5002.

# Takeaways / Discussion
To make the backend scalable for including other NOAA products, I created an API 
class that has a base URL and a dedicated function for hitting the RTSW endpoint.
More functions can be added easily to reach other endpoints.
I used Flask to handle creating the backend because it's lightweight and doesn't
require a lot of overhead to spin up. More endpoints can easily be added for the
frontend to display future data. 

To address persistance, the RTSW endpoint will look for the optional parameter
"persist". If it is set to true, the data will be stored in a SQLite database.
I chose SQLite because the current product only needed something simple in its
current state. I chose a SQLite database over simply writing to a file for scalability.

I containerized the backend and frontend with Docker to make starting up the product
easier.

I chose React as the frontend framework because I only built a simple, one-page
website and did not feel it required something as comprehensive as Angular.

I did some web research on solar storm prediction, and found that speeds over `500 km/s`
and density over `10 p/cm^3` could possibly indicate solar storms. This is what I
based the warnings off of. 