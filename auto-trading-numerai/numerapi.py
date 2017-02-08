'''
File from https://github.com/atreichel/NumerAPI
It used to interact with numer.ai web page
'''
import requests
import zipfile
from datetime import datetime, timedelta

class NumerAPI(object):
    def __init__(self, email, password):
        self._login_url = 'https://api.numer.ai/sessions'
        self._auth_url = 'https://api.numer.ai/upload/auth'
        self._dataset_url = 'https://api.numer.ai/competitions/current/dataset'
        self._submissions_url = 'https://api.numer.ai/submissions'
        self._payload = {'email':email, 'password':password}

    def download_current_dataset(self, dest_path='.', unzip=True):
        now = datetime.now().strftime('%Y%m%d')
        file_name = 'numerai_dataset_{0}.zip'.format(now)
        dest_file_path ='{0}/{1}'.format(dest_path, file_name)

        r = requests.get(self._dataset_url)
        if r.status_code!=200:
            return r.status_code

        with open(dest_file_path, "wb") as fp:
            for byte in r.content:
                fp.write(byte)

        if unzip:
            with zipfile.ZipFile(dest_file_path, "r") as z:
                z.extractall(dest_path)
        return r.status_code



    def login(self):
        r = requests.post(self._login_url, data=self._payload)
        if r.status_code!=201:
            return (None, None, None, r.status_code)

        rj = r.json()
        return(rj['accessToken'], rj['refreshToken'], rj['id'], r.status_code)



    def authorize(self, file_path):
        accessToken, refreshToken, id_, status_code = self.login()
        if status_code!=201:
            return (None, None, None, status_code)

        headers = {'Authorization':'Bearer {0}'.format(accessToken)}

        r = requests.post(self._auth_url,
                    data={'filename':file_path.split('/')[-1], 'mimetype': 'text/csv'},
                    headers=headers)
        if r.status_code!=200:
            return (None, None, None, r.status_code)

        rj = r.json()
        return (rj['filename'], rj['signedRequest'], headers, r.status_code)



    def get_current_competition(self):
        now = datetime.now()
        tdelta = timedelta(microseconds=55296e5)
        dt = now - tdelta
        dt_str = dt.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

        url = 'https://api.numer.ai/competitions?{ leaderboard :'
        url += ' current , end_date :{ $gt : %s }}'
        r = requests.get((url % (dt_str)).replace(' ', '%22'))
        if r.status_code!=200:
            return (None, None, r.status_code)

        rj = r.json()
        for c in rj:
            start_date = datetime.strptime(c['start_date'], '%Y-%m-%dT%H:%M:%S.%fZ')
            end_date = datetime.strptime(c['end_date'], '%Y-%m-%dT%H:%M:%S.%fZ')
            if start_date < now < end_date:
                return (c['dataset_id'], c['_id'], r.status_code)



    def upload_prediction(self, file_path):
        filename, signedRequest, headers, status_code = self.authorize(file_path)
        if status_code!=200:
            return status_code

        dataset_id, comp_id, status_code = self.get_current_competition()
        if status_code!=200:
            return status_code

        with open(file_path, 'rb') as fp:
            r = requests.Request('PUT', signedRequest, data=fp.read())
            prepped = r.prepare()
            s = requests.Session()
            resp = s.send(prepped)
            if resp.status_code!=200:
                return resp.status_code

        r = requests.post(self._submissions_url,
                    data={'competition_id':comp_id, 'dataset_id':dataset_id, 'filename':filename},
                    headers=headers)

        return r.json()
