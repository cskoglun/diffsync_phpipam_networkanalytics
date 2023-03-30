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
- Update your the credentials.yaml file with your credentials and ip information to the systems
```yaml
credentials:
     username_na: UPDATE
     username_pi: UPDATE
     password_na: UPDATE
     password_pi: UPDATE
     host_na: UPDATE
     host_pi: UPDATE
```
- If everything is setup correctly, you should now be able to run the main.py file
```bash
(venv) $ python main.py
```
and the output should be looking like this: 
```bash
(venv) $ python main.py 

Initializing load from Network Analytics

Initializing load PHPIPAM

2023-03-30 15:27.21 [debug    ] Diff calculation between these two datasets will involve 49 models dst=<Backend B "PHPIPAM"> flags=<DiffSyncFlags.NONE: 0> src=<Backend A "Network Analytics">
2023-03-30 15:27.21 [info     ] Beginning diff calculation     dst=<Backend B "PHPIPAM"> flags=<DiffSyncFlags.NONE: 0> src=<Backend A "Network Analytics">
2023-03-30 15:27.21 [info     ] Diff calculation complete      dst=<Backend B "PHPIPAM"> flags=<DiffSyncFlags.NONE: 0> src=<Backend A "Network Analytics">

 '  custom_field: test_value_1 MISSING in Network Analytics\n'
 '    subnets\n'
 '      subnets: 11.1.1.0/24 MISSING in Network Analytics\n'
 ...
 ...
 ...
```

##TODO: rest of documentation 

## Contributing
This code is developed by Christina Skoglund with inspiration from https://github.com/networktocode/diffsync