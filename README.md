# powerwallStats
Docker container to interface with Tesla Energy Gateway for Powerwall Stats

## Description
This docker container uses the excellent pyPowerwall repo (https://github.com/jasonacox/pypowerwall) to produce statistics and troubleshooting information for Tesla powerwall batteries.

## Build 

Build the docker container
`docker build -t powerwallstats .`

Create `.env` file in folder `powerwallStats` to store credentials       
```python
TESLA_PW_HOST="192.168.20.25"  
TESLA_PW_EMAIL="customer.name@gmail.com"   
TESLA_PW_PASSWORD="ABCDE"
TESLA_PW_TIMEZONE="Australia/Melbourne"
```

## Run 
Run the docker container
`docker run -t powerwallstats`

## Credits and References
pyPowerwall - https://github.com/jasonacox/pypowerwall
