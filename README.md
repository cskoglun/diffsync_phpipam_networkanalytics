# DiffSync between phpIPAM and Cisco Network Analytics
This repository provides a minimum viable soluition on how you can demonstrate the value of DiffSync. DiffSync is a utility library that can be used to compare and synchronize different datasets. For example, it can be used to compare a list of devices from 2 inventory systems and, if required, synchronize them in either direction. 

Documentation on DiffSync you find [here](https://diffsync.readthedocs.io/en/latest/)

In this example, we use DiffSync in order to investigare if the Host Pools in Cisco Network Analytics are updated with the subnets that are registered in the ipam system phpIPAM. 

[Cisco Network Analytics](https://www.cisco.com/c/en/us/solutions/analytics.html) provides advanced AI-enabled analytics available across all Cisco network platforms. It provides the high-quality visibility and fast remediation that you need to help assure service, from user to applications.

## Requirements
- Python installed in your environment
- [phpIPAM](https://phpipam.net/) installed with API enabled
- Custom field in phpIPAM where you map subnets to Cisco Network Analytics called "Network_Analytics_Pool"
- [Cisco Network Analytics](https://www.cisco.com/c/en/us/solutions/analytics.html) solution deployed

This documentation will not cover how to install phpIPAM or deploy Cisco Network Analytics. 

## How to get started
- Create a Python virtual environment and activate it
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```
- Install the necessary dependencies
```bash
(venv) $ pip install -r requirements.txt
```
- Pull this repository to your local environment
```bash
(venv) $ git pull https://github.com/cskoglun/diffsync_phpipam_networkanalytics.git
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

Initializing load phpIPAM

2023-03-30 15:27.21 [debug    ] Diff calculation between these two datasets will involve 49 models dst=<Backend B "phpIPAM"> flags=<DiffSyncFlags.NONE: 0> src=<Backend A "Network Analytics">
2023-03-30 15:27.21 [info     ] Beginning diff calculation     dst=<Backend B "phpIPAM"> flags=<DiffSyncFlags.NONE: 0> src=<Backend A "Network Analytics">
2023-03-30 15:27.21 [info     ] Diff calculation complete      dst=<Backend B "phpIPAM"> flags=<DiffSyncFlags.NONE: 0> src=<Backend A "Network Analytics">

 '  custom_field: test_value_1 MISSING in Network Analytics\n'
 '    subnets\n'
 '      subnets: 11.1.1.0/24 MISSING in Network Analytics\n'
 ...
 ...
 ...
```

##TODO: rest of documentation 

## Contributing
This code is developed by Christina Skoglund (cskoglun@cisco.com) with inspiration from https://github.com/networktocode/diffsync

## DISCLAIMER:
Please note: This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use. You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.