# DiffSync between PHPIPAM and Cisco Network Analytics
This repository provides a minimum viable soluition on how you can demonstrate the value of DiffSync. 

Documentation on DiffSync you find [here](https://diffsync.readthedocs.io/en/latest/)

## Requirements
- Python installed in your environment
- [PHPIPAM](https://phpipam.net/) with API enabled
- Custom field in PHPIPAM where you map subnets to Cisco Network Analytics called "Network_Analytics_Pool"
- Cisco Network Analytics

This documentation will not cover how to install PHPIPAM or deploy Cisco Network Analytics. 

## How to get started
- Create a Python virtual environment and activate it
```bash
python3 -m venv venv
source venv/bin/activate
```
- Install the necessary dependencies
```bash
pip install -r requirements.txt
```
- Update your virtual environment with credential variables:
```bash
export USERNAME:yourusername
```




TODO: rest of documentation 