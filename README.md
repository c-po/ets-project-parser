# ETS project parser

A simple Python helper that reads an exported ETS `*.knxproj` file and extract
components which are converted into a Homebridge JSON configuration.

## About

This is a spare time just for fun project - and as beeing a programmer I wan't
to automate my imports from ETS -> Homebridge

## Usage

```
$ knxproj.py --knxproj project.knxproj --knxd-ip 1.1.1.1
Area: {'Id': 'P-04FF-0_A-1', 'Address': '0', 'Name': 'Backbone Bereich', 'Puid': '1'}
      {'Id': 'P-04FF-0_L-1', 'Address': '0', 'Name': 'Bereichslinie', 'MediumTypeRefId': 'MT-0', 'Puid': '2'}
Area: {'Id': 'P-04FF-0_A-2', 'Address': '1', 'Name': 'EG', 'CompletionStatus': 'Editing', 'Puid': '3'}
      {'Id': 'P-04FF-0_L-2', 'Address': '0', 'Name': 'Hauptlinie', 'MediumTypeRefId': 'MT-0', 'Puid': '4'}
      {'Id': 'P-04FF-0_L-3', 'Address': '1', 'Name': 'Technik', 'MediumTypeRefId': 'MT-0', 'Puid': '5'}
      {'Id': 'P-04FF-0_L-9', 'Address': '2', 'Name': 'Abstell', 'MediumTypeRefId': 'MT-0', 'Puid': '20'}
      {'Id': 'P-04FF-0_L-10', 'Address': '3', 'Name': 'Bad', 'MediumTypeRefId': 'MT-0', 'Puid': '21'}
      {'Id': 'P-04FF-0_L-11', 'Address': '4', 'Name': 'Buero', 'MediumTypeRefId': 'MT-0', 'Puid': '22'}
      {'Id': 'P-04FF-0_L-12', 'Address': '5', 'Name': 'Wohnen', 'MediumTypeRefId': 'MT-0', 'Puid': '23'}
      {'Id': 'P-04FF-0_L-13', 'Address': '6', 'Name': 'Essbereich', 'MediumTypeRefId': 'MT-0', 'Puid': '24'}
      {'Id': 'P-04FF-0_L-14', 'Address': '7', 'Name': 'Kueche', 'MediumTypeRefId': 'MT-0', 'Puid': '25'}
      {'Id': 'P-04FF-0_L-15', 'Address': '8', 'Name': 'Flur', 'MediumTypeRefId': 'MT-0', 'CompletionStatus': 'Editing', 'Puid': '26'}
```
