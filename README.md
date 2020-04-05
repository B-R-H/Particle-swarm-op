# Prticle-swarm-op

Project to run particle swarms using docker swam.


## Contents
* [Run instructions](#Run_instructions)
  - [Docker swarm](#RDS)
  - [Docker compose](#RDC)
<a name="Run_instructions"></a>
## Run instructions

There are two ways to deploy the app using docker swarm and docker compose. The compsose has a more stable front end but the swarm deploy has a better algorhthm efficency.
<a name="RDS"></a>
### Docker swarm
To deploy using docker swarm you will have to export all of the varibles from the docker swarm yaml.The DATABASE_URI is in the form "mysql+pymysql://root:"MYSQL_ROOT_PASWORD"@psodb/psodata".The MYSQL_ROOT_PASSWORD can be anthing that you want. All of the vrsions are work with "v1". The logic, graphing, and front end have v2's avalible.

Once all the varibles are initilised the comand you will need to run is 

```docker stack deploy --compose-file docker-swarm.yaml pso```

<a name="RDC"></a>
### Docker Compose
To run using docker compose you will need to export the DATABASE_URI and the MYSQL_ROOT_PASSWORD again but then all that is need is

```docker-compose up -d```.


