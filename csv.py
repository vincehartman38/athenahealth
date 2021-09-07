# Generate CSV Upload for Appointments
import pandas as pd

def create_sch_df():
  sch_columns = ['ApptId',
           'ApptDateTime',
           'LocationId',
           'Location',
           'Event',
           'MRN',
           'PatientFirstName',
           'PatientLastName',
           'EmailAddress',
           'CellPhone',
           'CurrentGender',
           'DateOfBirth',
           'ProviderId',
           'Provider']
  df = pd.DataFrame(columns=sch_columns)
  return df

# Convert JSON to Pandas datafram for CSV
def convert_to_pandas(appts, depts_mapping, provs_mapping):
  df = create_sch_df()
  for i, appt in enumerate(appts):
    if 'patient' not in appt:
      continue
    df.loc[i, 'ApptId'] = appt['appointmentid']
    df.loc[i, 'ApptDateTime'] = appt['date'] + ' ' + appt['starttime']
    df.loc[i, 'LocationId'] = appt['departmentid']
    df.loc[i, 'Location'] = depts_mapping.get(int(appt['departmentid']), np.NaN)
    df.loc[i, 'Event'] = appt['appointmenttype']
    df.loc[i, 'MRN'] = appt['patient']['patientid']
    df.loc[i, 'PatientFirstName'] = appt['patient']['firstname']
    df.loc[i, 'PatientLastName'] = appt['patient']['lastname']
    df.loc[i, 'EmailAddress'] = appt['patient'].get('email', np.NaN)
    df.loc[i, 'CellPhone'] = appt['patient'].get('mobilephone', np.NaN)
    df.loc[i, 'CurrentGender'] = appt['patient'].get('sex', 'U')
    df.loc[i, 'DateOfBirth'] = appt['patient']['dob']
    df.loc[i, 'ProviderId'] = appt['providerid']
    df.loc[i, 'Provider'] = provs_mapping.get(int(appt['providerid']), np.NaN)
  return df
