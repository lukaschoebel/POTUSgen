# POTUSgen

As an assistant for the lecture [*Techniques in Artificial Intelligence*](https://campus.tum.de/tumonline/wbLv.wbShowLVDetail?pStpSpNr=950430848&pSpracheNr=2) (IN2062) at the Technical University of Munich, the objective of this project was to teach students the concepts of probabilistic modeling through the implementation of a word generator which is based on a Markov Model.

## Content
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Getting Started](#getting-started)
- [Docker & Troubleshooting](#docker--troubleshooting)
- [Requirements](#requirements)
- [License](#license)
- [Acknowledgements](#acknowledgements)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Getting Started

<!-- TODO: Add Starting Guide -->
- Unzip data set

## Docker & Troubleshooting

If you need to install other Python libraries or frameworks in order to run your notebook or Python script, it's always a good choice to use Docker to wrap your application. In general, these steps are applicable to all usecases. 

First things first: Install Docker and get an account at [DockerHub](https://hub.docker.com/) which provides you with a `<USERNAME>` (important for the steps below).
Subsequently, set up a Dockerfile and a requirements.txt as provided. While the `Dockerfile` is necessary to generate a Docker image, the latter file specifies all necessary requirements for the script. In `requirements.txt` you simply list all the frameworks you need and if you utilize a special version just type e.g. `tensorflow==1.0.0`.

After you have done this, execute the following commands in the terminal. `<USERNAME>` is your DockerHub user name and in `<EXERCISE NAME>` you can assign to your image. Check if you can run the image by copying the `docker run` command. If everything's runnin smoothly, proceed to login and pushing your Docker image to DockerHub. Yay!

```bash
# Tagging and building the image
docker build -t <USERNAME>/<EXERCISE NAME> .

# Running to ensure that it is working
docker run -it --rm --name <EXERCISE NAME> <USERNAME>/<EXERCISE NAME>

# Push image to DockerHub
docker login && docker push <USERNAME>/<EXERCISE NAME>
```

`ARTEMIS Specific` Since ARTEMIS is based on Bamboo Build Plans, you have to simply connect the set up hosted DockerHub image with Bamboo. This is achieved by inserting `<DOCKER USRNAME>/<EXERCISE NAME>` to the provided option in Bamboo which can be found via `Actions > Configure Plan > Stages > Default Job > Docker`.

## Requirements

<!-- TODO: Define Pyhton version -->
- `Python` 3.6
- `selenium`
- `tweepy`

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/lukaschoebel/POTUSgen/blob/develop/LICENSE) file for details.

## Acknowledgements

- TUM [Artemis](https://github.com/ls1intum/Artemis)
