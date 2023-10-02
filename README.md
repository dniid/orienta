## Pre-requisites :

Clone the Repo

```bash
git clone https://github.com/dniid/orienta.git

cd orienta
```

Have Docker installed in your machine

Instructions available at (https://docs.docker.com/desktop/)

## Running the program

To start the minesweeper bot simply do the following command

``` bash
docker-compose  up
```

This will start a selenium grid server running a chrome instance.
To see what's going on inside the browser you can go to the following link
http://localhost:7900/?autoconnect=1&resize=scale&password=secret


## Notes

The minesweeper bot is pretty unstable right now.
It sometimes gets lost and doesn't know what to do so it just stops.

You might want to restart the container if that happens.

Also, there's a scrapped bot that automates the 2048 game.
To take a look at what the bot can do for now, you can uncomment the 'auto2048' service inside the 'docker-compose.yml' file and commenting the 'autominesweeper' service inside there.
After that, you can go through the same process and access the browser to check on the bot's progression.

