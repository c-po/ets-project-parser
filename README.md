# ETS project parser

A simple Python helper that reads an exported ETS `*.knxproj` file and extract
components which are converted into a Homebridge JSON configuration.

## About

This is a spare time just for fun project - and as beeing a programmer I wan't
to automate my imports from ETS -> Homebridge

## Usage

```
./knxproj.py --knxproj foo.knxproj --debug
== Area ==
{'Address': '0', 'Id': 'P-04FF-0_A-1', 'Name': 'Backbone Bereich', 'Puid': '1'}
  == Line ==
{ 'Address': '0',
  'Id': 'P-04FF-0_L-1',
  'MediumTypeRefId': 'MT-0',
  'Name': 'Bereichslinie',
  'Puid': '2'}
== Area ==
{'Address': '1',
 'CompletionStatus': 'Editing',
 'Id': 'P-04FF-0_A-2',
 'Name': 'EG',
 'Puid': '3'}
  == Line ==
{ 'Address': '0',
  'Id': 'P-04FF-0_L-2',
  'MediumTypeRefId': 'MT-0',
  'Name': 'Hauptlinie',
  'Puid': '4'}
  == Line ==
{ 'Address': '1',
  'Id': 'P-04FF-0_L-3',
  'MediumTypeRefId': 'MT-0',
  'Name': 'Technik',
  'Puid': '5'}
  == Line ==
{ 'Address': '2',
  'Id': 'P-04FF-0_L-9',
  'MediumTypeRefId': 'MT-0',
  'Name': 'Abstell',
  'Puid': '20'}
  == Line ==
{ 'Address': '3',
  'Id': 'P-04FF-0_L-10',
  'MediumTypeRefId': 'MT-0',
  'Name': 'Bad',
  'Puid': '21'}
  == Line ==
{ 'Address': '4',
  'Id': 'P-04FF-0_L-11',
  'MediumTypeRefId': 'MT-0',
  'Name': 'Buero',
  'Puid': '22'}
    == Device ==
{   'Address': '1',
    'ApplicationProgramLoaded': 'true',
    'Comment': '',
    'CommunicationPartLoaded': 'true',
    'Description': '',
    'Hardware2ProgramRefId': 'M-0083_H-2.2E38-1_HP-008A-28-7B00',
    'Id': 'P-04FF-0_DI-20',
    'IndividualAddressLoaded': 'true',
    'IsActivityCalculated': 'true',
    'LastDownload': '2021-10-05T22:35:37.9237565Z',
    'LastModified': '2021-10-05T22:35:07.4462068Z',
    'LastUsedAPDULength': '55',
    'MediumConfigLoaded': 'true',
    'Name': 'Oben BE-GT2Tx.01 Glastaster II Smart mit Temperatursensor',
    'ParametersLoaded': 'true',
    'ProductRefId': 'M-0083_H-2.2E38-1_P-BE.2DGT2Tx.2E01',
    'Puid': '287',
    'ReadMaxAPDULength': '55',
    'SerialNumber': 'AN'}
  == Line ==
{ 'Address': '5',
  'Id': 'P-04FF-0_L-12',
  'MediumTypeRefId': 'MT-0',
  'Name': 'Wohnen',
  'Puid': '23'}
  == Line ==
{ 'Address': '6',
  'Id': 'P-04FF-0_L-13',
  'MediumTypeRefId': 'MT-0',
  'Name': 'Essbereich',
  'Puid': '24'}
  == Line ==
{ 'Address': '7',
  'Id': 'P-04FF-0_L-14',
  'MediumTypeRefId': 'MT-0',
  'Name': 'Kueche',
  'Puid': '25'}
  == Line ==
{ 'Address': '8',
  'CompletionStatus': 'Editing',
  'Id': 'P-04FF-0_L-15',
  'MediumTypeRefId': 'MT-0',
  'Name': 'Flur',
  'Puid': '26'}
    == Device ==
{   'Address': '11',
    'ApplicationProgramLoaded': 'true',
    'Comment': '',
    'CommunicationPartLoaded': 'true',
    'Description': '',
    'Hardware2ProgramRefId': 'M-00A6_H-00000027-1_HP-0026-10-39D6',
    'Id': 'P-04FF-0_DI-4',
    'IndividualAddressLoaded': 'true',
    'IsActivityCalculated': 'true',
    'LastDownload': '2021-09-12T22:17:30.9336462Z',
    'LastModified': '2021-09-12T22:06:45.3018515Z',
    'LastUsedAPDULength': '239',
    'MediumConfigLoaded': 'true',
    'Name': '',
    'ParametersLoaded': 'true',
    'ProductRefId': 'M-00A6_H-00000027-1_P-1152.2D3',
    'Puid': '45',
    'ReadMaxAPDULength': '248',
    'SerialNumber': 'AK'}
    == Device ==
{   'Address': '30',
    'ApplicationProgramLoaded': 'true',
    'Comment': '',
    'CommunicationPartLoaded': 'true',
    'Description': '',
    'Hardware2ProgramRefId': 'M-0009_H-9.20.2F.2F.20TXA306-1_HP-206A-12-E24D',
    'Id': 'P-04FF-0_DI-6',
    'IndividualAddressLoaded': 'true',
    'IsActivityCalculated': 'true',
    'LastDownload': '2021-09-20T22:18:03.9752559Z',
    'LastModified': '2021-09-20T22:17:08.7748682Z',
    'LastUsedAPDULength': '15',
    'MediumConfigLoaded': 'true',
    'Name': '',
    'ParametersLoaded': 'true',
    'ProductRefId': 'M-0009_H-9.20.2F.2F.20TXA306-1_P-TXA306',
    'Puid': '72',
    'SerialNumber': 'A'}
    == Device ==
{   'Address': '40',
    'ApplicationProgramLoaded': 'true',
    'Comment': '',
    'CommunicationPartLoaded': 'true',
    'Description': '',
    'Hardware2ProgramRefId': 'M-0009_H-9.20.2F.2F.20TYA664AN-1_HP-E0A2-10-B6BE',
    'Id': 'P-04FF-0_DI-7',
    'IndividualAddressLoaded': 'true',
    'IsActivityCalculated': 'true',
    'LastDownload': '2021-09-14T22:07:06.6198628Z',
    'LastModified': '2021-09-12T22:03:49.7483917Z',
    'LastUsedAPDULength': '40',
    'MediumConfigLoaded': 'true',
    'Name': '',
    'ParametersLoaded': 'true',
    'ProductRefId': 'M-0009_H-9.20.2F.2F.20TYA664AN-1_P-TYA664AN',
    'Puid': '73',
    'ReadMaxAPDULength': '40',
    'SerialNumber': 'A'}
{   'Address': '20',
    'ApplicationProgramLoaded': 'true',
    'Comment': '',
    'CommunicationPartLoaded': 'true',
    'Description': '',
    'Hardware2ProgramRefId': 'M-0009_H-9.20.2F.2F.20TYA608D-1_HP-500B-01-D868',
    'Id': 'P-04FF-0_DI-15',
    'IndividualAddressLoaded': 'true',
    'IsActivityCalculated': 'true',
    'LastDownload': '2021-09-20T22:18:44.6694366Z',
    'LastModified': '2021-09-20T22:18:30.3400514Z',
    'LastUsedAPDULength': '30',
    'MediumConfigLoaded': 'true',
    'Name': '',
    'ParametersLoaded': 'true',
    'ProductRefId': 'M-0009_H-9.20.2F.2F.20TYA608D-1_P-TYA608D',
    'Puid': '98',
    'ReadMaxAPDULength': '30',
    'SerialNumber': 'AA'}
```
