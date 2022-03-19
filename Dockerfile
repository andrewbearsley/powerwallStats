FROM ubuntu
LABEL author: Andrew Bearsley version: 0.1
WORKDIR tesla_powerwall_checker
RUN apt update && apt install git vim wget python3 python3-pip -y 
ENV PYTHONPATH="$HOME/.local/bin:$PYTHONPATH"
ENV PATH="$HOME/bin:$HOME/.local/bin:$PATH"
RUN pip3 install requests protobuf python-dotenv
RUN git clone https://github.com/jasonacox/pypowerwall.git
COPY powerwallStats.py .
COPY .env .
CMD ["python3", "powerwallStats.py"]


