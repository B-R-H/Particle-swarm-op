# Prticle swarm optimisation

Project to run particle swarms using docker swam.


## Contents
* [What is PSO](#PSO)
* [Run instructions](#Run_instructions)
  - [Docker swarm](#RDS)
  - [Docker compose](#RDC)
* [Project brief](#PB)
* [User stories](#User_Stories)

<a name="PSO"></a>
## What is PSO

PSO is a machine learning technique that is used to optmise functions. It does this by realising a load of particles into the function space to exsplore it. The particles are initlised randomly with random velosities. After all of the particles have moved they asses the value of the function at the poit in space where they reside. All of the evaluations are compared and then the particles adjust their velosity such that they head slightly more towards the global maximum. As the number of iteratios increses the particle shold give a progressively better aproximation for the global max.

This is typicaly used to asses complex functions in multilple dimetions where it is doesn't make sense to calculate all the values of the function to assess it. Some use cases are optimising the inputs for nuclear reactors or as an altenertive way to train neural networks.

<a name="Run_instructions"></a>
## Run instructions

There are two ways to deploy the app using docker swarm and docker compose. The compsose has a more stable front end but the swarm deploy has a better algorhthm efficency.

All run methods end up with the app front end acessable from port 5000 on the machine that is run on.
<a name="RDS"></a>
### Docker swarm
To deploy using docker swarm you will have to export all of the varibles from the docker swarm yaml.The DATABASE_URI is in the form "mysql+pymysql://root:"MYSQL_ROOT_PASWORD"@psodb/psodata".The MYSQL_ROOT_PASSWORD can be anthing that you want. All of the vrsions are work with "v1". The logic, graphing, particles, and front end have v2's avalible.

Once all the varibles are initilised the comand you will need to run is\
```docker stack deploy --compose-file docker-swarm.yaml pso```.

<a name="RDC"></a>
### Docker Compose
To run using docker compose you will need to export the DATABASE_URI and the MYSQL_ROOT_PASSWORD again but then all that is need is\
```docker-compose up -d```.

<a name="PB"></a>
## Project brief
* Produce a service based flask aplication that is deployed using docker.
* Spead the deployment of the aplication across multiple VMs using docker swarm.
* Have the VMs set up using an ansible script.
* Aproch the project in an adgile manner.
* Have the project fully documented.

<a name="User_Stories"></a>
## User stories
* As a user I want to be able to find the optimal value of a function using Particle swarm optmisation.
* As a user I want to be able to see the progress of my optimsation using a web interface.
* As a user I want to be able to be able to reset my simulation to check that the outcome is consistant.
* As a user I want to be able to pasue the simulation so that I can observe that itteration.


