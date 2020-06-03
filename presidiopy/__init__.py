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

    @property
    def field_types_url(self):
        return self.base_url + 'fieldTypes'

    def change_project(self, project):
        self.project = project

    def add_field_type(self, field, **kwargs):
        name = field['value']['entity']
        return self.request('post', self.recognizers_url + name, json=field, **kwargs)

    def delete_field_type(self, recognizer_name):
        return self.request('delete', self.recognizers_url + recognizer_name)

    def analyze(self, text, **kwargs):
        data = {
            'text': text
        }

        template = kwargs.get('template')
        analyzeTemplate = kwargs.get('analyzeTemplate')
        if template is not None:
            data['AnalyzeTemplateId'] = template
            data['analyzeTemplate'] = analyzeTemplate
        else:
            data['analyzeTemplate'] = analyzeTemplate if analyzeTemplate is not None else {'allFields': True}

        return self.request('post', self.analyze_url, json=data)

    def retrieve_recognizers(self, *args):
        url = self.recognizers_url
        if len(args) > 0:
            url += str(args[0])
        return self.request('get', url)

    def retrieve_field_types(self):
        url = self.field_types_url
        return self.request('get', url)

    def request(self, method, url, **kwargs):
        if method == 'get':
            response = requests.get(url)
        elif method == 'delete':
            response = requests.delete(url)
        else:
            response = requests.post(url, **kwargs)

        if response.status_code != 200:
            raise Exception('Error: ' + str(response.status_code))

        return response.json()
