PPyOrthanc
=========
Python library that "purely" wraps the Orthanc REST API and facilitates the manipulation
of data with several cool utilities.

This is a fork of pyorthanc that avoids raising errors for failing requests.

Installation
------------
```sh
$ pipenv install git+https://github.com/dnlcrl/pyorthanc-pure#egg=ppyorthanc
```

Example of usage
----------------
Be sure that Orthanc is running. The default URL (if running locally) is `http://localhost:8042`.

#### Getting access to patients, studies, series and instances information:

```python
from ppyorthanc import Orthanc

orthanc = Orthanc('http://localhost:8042', username='username', password='password')

# To get patients identifier and main information
patients_identifiers = orthanc.get_patients().json()

for patient_identifier in patients_identifiers:
   # To get patient information
   patient_info = orthanc.get_patients_id(patient_identifier).json()

   patient_name = patient_info['MainDicomTags']['PatientName']
   ...
   study_identifiers = patient_info['Studies']

# To get patient's studies identifier and main information
for study_identifier in study_identifiers:
   # To get Study info
   study_info = orthanc.get_studies_id(study_identifier).json()

   study_date = study_info['MainDicomTags']['StudyDate']
   ...
   series_identifiers = study_info['Series']

# To get study's series identifier and main information
for series_identifier in series_identifiers:
   # Get series info
   series_info = orthanc.get_series_id(series_identifier).json()

   modality = series_info['MainDicomTags']['Modality']
   ...
   instance_identifiers = series_info['Instances']

# and so on ...
for instance_identifier in instance_identifiers:
   instance_info = orthanc.get_instances_id(instance_identifier).json()
   ...
```

#### Find patients with certain characteristics in an Orthanc instance:
Each patient is a tree. Layers in each tree have the following structure 
`Patient` -> `Study` -> `Series` -> `Instance`
that correspond to the provided filter functions.

```python
from pyorthanc import find

patients = find(
    orthanc_url='http://localhost:8042/',
    auth=('username', 'password'),
    series_filter=lambda s: s.modality == 'RTDOSE'  # Optional: filter with pyorthanc.Series object
)

for patient in patients:
   patient_info = patient.get_main_information()
   patient.id_   # Access PatientID
   patient.name  # Access PatientName
   
   patient.get_zip() # DICOM files' content in bytes
   
   anonymized_patient_1_resp = patient.anonymize()  # New patient that was anonymized by Orthanc
   anonymized_patient_1 = Patient(anonymized_patient_1_resp["PatientID"], client=patient.client)
   anonymized_patient_2_resp = patient.anonymize(
      keep=['PatientName'],   # You can keep/remove/replace the DICOM tags you want
      replace={'PatientID': 'TheNewPatientID'},
      remove=['ReferringPhysicianName'],
      force=True  # Needed when changing PatientID/StudyInstanceUID/SeriesInstanceUID/SOPInstanceUID
   )  
   anonymized_patient_2 = Patient(anonymized_patient_2_resp["PatientID"], client=patient.client)

   ...

   for study in patient.studies:
      study.date  # Date as a datetime object
      study.referring_physician_name
      ...

      for series in study.series:
         series.modality  # Should be 'RTDOSE' because of the series_filter parameters
         ...
```


#### Upload DICOM files to Orthanc:

```python
from pyorthanc import Orthanc

orthanc = Orthanc('http://localhost:8042', 'username', 'password')

with open('A_DICOM_INSTANCE_PATH.dcm', 'rb') as file:
   orthanc.post_instances(file.read())
```

#### Getting list of connected remote modalities:
```python
from pyorthanc import Orthanc

orthanc = Orthanc('http://localhost:8042', 'username', 'password')

orthanc.get_modalities()
```

#### Query (C-Find) and Retrieve (C-Move) from remote modality:

```python
from pyorthanc import RemoteModality, Orthanc

orthanc = Orthanc('http://localhost:8042', 'username', 'password')

modality = RemoteModality(orthanc, 'modality')

# Query (C-Find) on modality
data = {'Level': 'Study', 'Query': {'PatientID': '*'}}
query_response = modality.query(data=data)

answer = modality.get_query_answers()[query_response['ID']]
print(answer)

# Retrieve (C-Move) results of query on a target modality (AET)
modality.move(query_response['ID'], {'TargetAet': 'target_modality'})
```

#### Anonymize patient:
```python
from pyorthanc import Orthanc, Patient

orthanc = Orthanc('http://localhost:8042', 'username', 'password')

patient_identifier = orthanc.get_patients().json()[0]

anonymized_patient = Patient(patient_identifier, orthanc).anonymize(
    keep=['PatientName'],   # You can keep/remove/replace the DICOM tags you want
    replace={'PatientID': 'TheNewPatientID'},
    remove=['ReferringPhysicianName'],
    force=True  # Needed when changing PatientID/StudyInstanceUID/SeriesInstanceUID/SOPInstanceUID
)
# Or directly with
orthanc.post_patients_id_anonymize(patient_identifier).json()

# result is: (you can retrieve DICOM file from ID)
# {'ID': 'dd41f2f1-24838e1e-f01746fc-9715072f-189eb0a2',
#  'Path': '/patients/dd41f2f1-24838e1e-f01746fc-9715072f-189eb0a2',
#  'PatientID': 'dd41f2f1-24838e1e-f01746fc-9715072f-189eb0a2',
#  'Type': 'Patient'}
```

## Citation
If you publish using PyOrthanc, we kindly ask that you credit us. PyOrthanc can be found on Zenodo :
https://zenodo.org/record/7086219 .


## Contributing
You can contribute to this project with the following steps:
1. First, fork the project on Github 
2. Clone the project
   ```shell
   git clone https://github.com/<your-github-username>/pyorthanc
   cd pyorthanc
   ```
3. Enter the project and create a poetry environment 
   (this project use the [poetry](https://python-poetry.org/) for dependency management)
   ```shell
   peotry install 
   ```
4. Make a new git branch where you will apply the changes
   ```shell
   git checkout -b your-branch-name
   ```
   Now you can make your changes
5. Once done, `git add`, `git commit` and `git push` the changes.
6. Make a Pull Request from your branch to the https://github.com/ulaval-rs/pyorthanc.
