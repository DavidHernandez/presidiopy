import requests

class PresidioPy():
    def __init__(self, ip, project, **kwargs):
        self.ip = ip
        self.project = project
        self.port = 8080
        self.http = 'http://'

        for key, value in kwargs.items():
            if key == 'port':
                self.port = value
            if key == 'ssl' and value == True:
                self.http = 'https://'

    @property
    def base_url(self):
        return self.http + self.ip + ':' + str(self.port) + '/api/v1/'

    @property
    def analyze_url(self):
        return self.base_url + 'projects/' + self.project + '/analyze'

    @property
    def recognizers_url(self):
        return self.base_url + 'analyzer/recognizers/'

    def change_project(self, project):
        self.project = project

    def analyze(self, text, **kwargs):
        data = {
            'text': text
        }

        template = kwargs.get('template')
        if template is not None:
            data['AnalyzeTemplateId'] = template
        else:
            data['analyzeTemplate'] = {'allFields': True}

        return self.request('post', self.analyze_url, json=data)

    def retrieve_recognizers(self, *args):
        url = self.recognizers_url
        if len(args) > 0:
            url += str(args[0])
        return self.request('get', url)

    def request(self, method, url, **kwargs):
        if method is 'get':
            response = requests.get(url)
        else:
            response = requests.post(url, **kwargs)

        if response.status_code is not 200:
            raise Exception('Error: ' + str(response.status_code))

        return response.json()
