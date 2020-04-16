# Prticle swarm optimisation

Project to run particle swarms using docker swam.

## Contents
* [What is PSO](#PSO)
* [Run instructions](#Run_instructions)
  - [Docker swarm](#RDS)
  - [Docker compose](#RDC)
  - [Kubernetes](#k8)
* [Services](#services)
  - [Mysql](#mysql)
  - [Nginx](#nginx)
  - [Front end](#frontend)
  - [Graphing](#graphing)
  - [Logic](#logic)
  - [Particle](#particle)
* [Project brief](#PB)
* [User stories](#User_Stories)
* [Project mangement](#PM)
* [Use cases](#Use_cases)
* [Risk analysis](#Risk)
* [Design](#Design)
* [Testing](#Testing)
* [CI pipline](#CI)
* [Conclusion](#Conclusion)

<a name="PSO"></a>
## What is PSO

PSO is a machine learning technique that is used to optmise functions. It does this by realising a load of particles into the function space to exsplore it. The particles are initlised randomly with random velosities. After all of the particles have moved they asses the value of the function at the poit in space where they reside. All of the evaluations are compared and then the particles adjust their velosity such that they head slightly more towards the global maximum. As the number of iteratios increses the particle shold give a progressively better aproximation for the global max.

This is typicaly used to asses complex functions in multilple dimetions where it is doesn't make sense to calculate all the values of the function to assess it. Some use cases are optimising the inputs for nuclear reactors or as an altenertive way to train neural networks.

[Extra reading.](https://en.wikipedia.org/wiki/Particle_swarm_optimization)

<a name="Run_instructions"></a>
## Run instructions

There are two ways to deploy the app using docker swarm and docker compose. The compsose has a more stable front end but the swarm deploy has a better algorhthm efficency.

The kuberneties and docker compose deployment end up with the app acessable over port 80. The docker swarm deployment has the front end acessable on port 5000 and the figure acessable on 5001. The swarm deploy is set up to be configurred with a seprate VM acting as a load ballencer.

When the app is up and running correctly you shoud see somthing like this.
![alt text](Media/web_app.png)

<a name="RDS"></a>
### Docker swarm
To deploy using docker swarm you will have to export all of the varibles from the docker swarm yaml.The DATABASE_URI is in the form "mysql+pymysql://root:"MYSQL_ROOT_PASWORD"@psodb/psodata".The MYSQL_ROOT_PASSWORD can be anthing that you want. The FIG_IP has to be the IP adress of the nginx load ballencer to allow for the figure to display correctly. All of the vrsions are work with "v1".

Once all the varibles are initilised the comand you will need to run is\
```docker stack deploy --compose-file docker-swarm.yaml pso```.

<a name="RDC"></a>
### Docker Compose
To run using docker compose you will need to export the DATABASE_URI and the MYSQL_ROOT_PASSWORD again but then all that is need is\
```docker-compose up -d```.

<a name="k8"></a>
### Kubernetes
To deploy using Kubernetes you will need a cluster configured that you have acess to. To then deploy you will need to run\ 
```kubectl apply -f k8```\
from the root of the file system. You will then need to get the public IP of the nginx service and insert that IP int the value for the FIG_IP in the frontend.yaml file. Once this is done you will have to apply again to update that deployment. You can either reaply the whole folder or just the frontend.yaml. This step allows to the image to displayed on the service correctly.  

<a name="services"></a>
## Services
<details>
	<summary>Deatails of all of the services.</summary>
	<a name="mysql"></a>
	### Mysql
	Simple Mysql container with the data structure needed already confiured to track the progression of the itterations. Also contains all of the flags that crontrool the run flags.

	<a name="nginx"></a>
	### Nginx
	Nginx container to act as a load ballencer to the various other services only exposing the front end and pade that the figure is displayed on so it can be pulled by the html code.

	<a name="frontend"></a>
	### Front end
	Faslk aplication that displays the progress of the algorythm along with 3 buttons. These provide start, stop, and reset functionality.

	<a name="graphing"></a>
	### Graphing service
	Service that uses [numpy](https://numpy.org) and [matplotlib](https://matplotlib.org) to generate a base contoure plot of the function being used. The location of the particles and their veloicites are recived in a post request from the particle service once it has completed an itteration. This data is then used to overlay the particles onto the contour plot and serve this up as a png file on the \figure page.

	<a name="logic"></a>
	### Logic
	Service to asess the overal progress of the algroythim. It recives the locations of all the particels in a json from the particle service. Once recived the function is evaluated at the location of all of the particles. These values are compared to the current global maximum pulled from the databse. If a value is greater the value of the database is updated to reflect that if not the previous value is entered again. At the end of iterating through the particles the current postion of the global maximum is sent back to the particle service.

	<a name="particle"></a>
	### Particle
	This is the core service of the algorythm. It controls all of the logic for the particles. Once triggered the service checks to see if the particles for the dimulation have been generated correctly and if they haven't it generates them. Once the particles have been sucessfully genrated a run loop is entered that is dependent on a flag stored in the database. In this loop the particles are moved and then their values are sent off the relevant services. When the global max location is recived the veloicity of all of the particles is updated to move slightly more towards it. This loop will contiue untill the run flag is updated in the databse. As the itterations increase all of the particles should converge on the global maximum found by the algorythm due to the drag on the particles.

</details>

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

<a name="PM"></a>
## Project mangement
For this project I predominatly used the github projects to organise my work. I had 3 seprate project boards one for base python functionality, one for containers and services, and one to handle the devops side of the project (CI pipline automatic deployment ect...). When I had a new bit of functionality I wanted to add or a bug I needed to fix I added it as an isue and then assigned it to the releveat board.
![alt text](Media/Git%20project.png)

<a name="Use_Cases"></a>
## Use cases
In it's current state the application only asses two functions that are stored in different images. The first is a noisy 3D wave form to try and trap the algorthm at local maxima. The second is a simple 3D perabola that was used in the initial testing of the app.

<a name="Risk"></a>
## Risk analysis
![alt text](Media/Screenshot%202020-04-06%20at%2008.28.14.png)

<a name="Design"></a>
## Design
The app is made up of five containers. Four of wich contain python logic and one that contains a mysql instance. The services comunicate using a varity of methods. The statring and stopping of the algorythm is done using simple get requests. The particle container passes and recives information from the logic container in jsons and purley sends jsons to the graphing container. The front end recives a full png file in a request from the graphing containerand the mysql container is used by the particle container to store imformation about the run state of the algorythm.
![alt text](Media/Service%20layout.png)

The project is deployed across two VMs with a third acting as an nginx load balencer and fourth to house jenkins.

![alt text](Media/VM%20layout.png)
<a name="Testing"></a>
## Testing
The base functionality of the app was built in a test driven development manner using pytest to check that the logic was firing correctly.
![alt text](Media/particle%20test.png)
![alt text](Media/logic%20test.png)

To test the containers, as the logic was taken from the base modules, I used postman instead of an automated testing method as it allowd for quicker trobuleshoting.
![alt text](Media/Postman.png)

<a name="CI"></a>
## CI pipline 
For this project I tried to use a pipeline job. I have a very simple script at the moment that just does a docker stack deploy depending on the git webhook. If there was more time to work on this I would look into building in the functonality to test and build the images in the jenkins job.

<a name="Conclusion"></a>
## Conclusion
The actual functionality of the app I am very happy with. The web interface shows what is going on and the algorythm achives its goal of getting an optmal value. It could be improved by adding functionality to add custom functions and getting a better sycronised start across the particle containers.

The complexity of the app however meant that it took up a significant amount of time to develop and that left less time for the CI piplene and continous deployment part of the project wich lead to it being rushed.
