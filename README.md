# IncriminaTor
The [Tor Project](https://www.torproject.org/) has a tool for finding a node's uptime given an IP and a date, called [ExonaraTor](https://metrics.torproject.org/exonerator.html). My plan for IncriminaTor is to build a web service with a similar lookup feature that will find Tor node uptimes for IPs in some published blacklists. The source of blacklists is [Apility](https://apility.io/), which aggregates several sources of blacklisted IPs along with their associated domains, networks, and geographic information.

How to use IncriminaTor
 - Input an IP address and date
 - Click `Let's dive in`
 - After a few seconds of making requests, the server will redirect you to a new page containing the following information:
   - Whether the given IP was found to be operating a Tor node on the given date
   - Whether the given IP was found in a blacklist, and a JSON string describing the blacklist(s) in which it was found
   - Geographic information pinpointing the IP address

Why I built IncriminaTor:

I was  interested in 1. learning more about the Tor project and 2. learning how to use IP blacklist services and what they can be used for.

Overall, I've learned that IP blacklist services often keep lists of Tor nodes. This actually makes a lot of sense, since web services would benefit from knowing when a given user is untrackable.

Along with that, I've learned more about how to build RESTful services in Python, and how to write unit tests for these services.

Technologies:
 - Python
   - Django
   - Curl/Python Requests
 - ExoneraTor
  - ExoneraTor does not have an API, so I implemented my detector by sending a GET request to the ExoneraTor site and parsing it for a positive search result. Details can be found in `/incriminator/incriminator/exonerator.py`
 - Apility.io
   - Web API
   - Implementation in `/incriminator/incriminator/apilty.py`

I was planning on using VueJS to implement this project, but I realized upon trying to send GET requests that Javascript is not the best language for server-side interactions, and that all of my API calls would simpler and less hacky if moved to the service layer. Aside from that, I could not find any benefits that VueJS would provide to the service due to its simplicity, so I cut it. Please tell me if there are benefits that I overlooked, because I would love to hear about them.

How to set it up:
 1. Clone the repo: `git clone https://github.com/TheodorJ/IncriminaTor`
 2. Acquire an API key from [apility.io](apility.io). You will need this for IP blacklist and GeoLocation lookups
 3. cp `apility-api-key.txt.template` to `apility-api-key.txt`, and copy your API key into it
 4. Install Python3: `sudo apt-get install python3 python3-pip` on Ubuntu
 5. Install Python requirements: `sudo pip3 install -r incriminator/requirements.txt`
 6. cd into the `incriminator` directory
 7. Run `python3 manage.py runserver 8000`
 8. Navigate to `localhost:8000` in a web browser. You should see the index page, with a form to enter an IP and date. The setup is complete

Running unit tests:
 1. From root directory, cd into `incriminator`
 2. Run `python3 manage.py test`

Currently there are only two unit tests, since there are only three ways for the client to interact with the server and one of them requires an API key. More may be added in the future as the service expands.
