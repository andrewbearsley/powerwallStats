# powerwallStats
Docker container to interface with Tesla Energy Gateway for Powerwall Stats

## Description
This docker container uses the excellent pyPowerwall repo (https://github.com/jasonacox/pypowerwall) to produce statistics and troubleshooting information for Tesla powerwall batteries.

## Setup
### Step 1.
Clone this repo.  

### Step 2. Create .env file to store credentials    
    TESLA_PW_HOST="192.168.20.25"  
    TESLA_PW_EMAIL="customer.name@gmail.com"  
    TESLA_PW_PASSWORD="ABCDE"  
    TESLA_PW_TIMEZONE="Australia/Melbourne"  

### Step 3. Build the docker container
    docker build -t powerwallStats .

### Step 3. Run the docker container
    docker run -t powerwallStats
## Credits and References

pyPowerwall - https://github.com/jasonacox/pypowerwall
