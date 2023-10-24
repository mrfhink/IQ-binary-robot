# IQ Option Binary Bot

This little robot gets open assets from IQ Option and runs a strategy based on ADX, MACD and EMAs. It buys and sells automatically.

## Installation

### 1. Setup the virtual enviroment

In order to work with IQ-Binary-Bot application I recommend you to create a virtual enviroment. 

`python -m venv venv`.

### 2. Clone this repository

1. Run `git clone https://github.com/mrfhink/IQ-binary-bot`.

2. Activate the virtual enviroment `source venv/bin/activate`.

### 3. Install requirements

1. Run `cd IQ-binary-bot`.

2. Run `pip install -r requirements.txt`.

3. Make sure to install this package too [IQ Option API](https://github.com/iqoptionapi/iqoptionapi).

## Usage

Just run `python main.py` inside the `src` folder.

## TODO

- <s>Some way to calculate the asset's trend in order to open position in that direction only.</s>

- A few more strategies and a way to select which one to use.

- ?

## Author Info

- Twitter - [@BarajasAldair](https://twitter.com/BarajasAldair)
- LinkedIn - [Aldair Barajas](https://www.linkedin.com/in/aldair-barajasaldana)
