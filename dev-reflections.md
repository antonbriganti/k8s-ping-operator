## techincal points of interest 
- TTL is not provided in pingtest results
    - the library I was using didn't support TTL and I've only noticed when trying to bring as many features from  `ping` to the solution on the final onceover
- right now, you need to actually publish the docker image for the deployment to pull it in
    - I couldn't figure out if there was a way to make it pull from a local repo instead
- running the operator locally requires super user permissions so it can create sockets for ICMP
    - not sure how often this would come up - running locally means you don't have to push to dockerhub for every change you want to make but it isn't really a good way to run an operator
- as part of the error handling in the operator, I'm using a catch all exception. this isn't great but I thought it'd be best to cast a wide net to get everything. I don't know if I feel the same way at the end of all of this

## personal reflections
- I should have done this using git. it wasn't according to spec so I went without but now at the end of it I wish I had done it properly.
- unit testing was my biggest challenge and in retrospect I really should have done this in a TDD fashion
    - the exploratory work started to blend into the actual solution and I had to retrofit tests in
    - I was ad-hoc testing while I went along so I knew it work, but proving it in a replicable manner is important

this was first time I've made an operator from scratch, and it was a really interesting problem to try and solve. the RBAC stuff was a challenge to learn on a level deep enough to really understand why things were working, but by the end of it all, it all made sense.
