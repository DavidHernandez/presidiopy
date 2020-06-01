import unittest
from presidiopy import PresidioPy
from unittest import mock

class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

def mocked_requests_analyze(*args, **kwargs):
    if args[0] != 'http://127.0.0.1:8080/api/v1/projects/presidiopy/analyze':
        return MockResponse(None, 404)

    json = kwargs.get('json')
    if json is None:
        return MockResponse(None, 404)

    if 'AnalyzeTemplateId' in json and json['AnalyzeTemplateId'] == 'template_id':
        return MockResponse(['ok'], 200)

    elif 'analyzeTemplate' in json and 'fields' in json['analyzeTemplate']:
        return MockResponse(['ok'], 200)

    return MockResponse([], 200)

def mocked_requests_recognizers(*args, **kwargs):
    if not args[0].startswith('http://127.0.0.1:8080/api/v1/analyzer/recognizers/'):
        return MockResponse(None, 404)

    return MockResponse([], 200)

def mocked_requests_field_types(*args, **kwargs):
    if not args[0].startswith('http://127.0.0.1:8080/api/v1/fieldTypes'):
        return MockResponse(None, 404)

    return MockResponse([], 200)

def mocked_requests_error(*args, **kwargs):
    return MockResponse(None, 404)

class TestPresidioPy(unittest.TestCase):
    def setUp(self):
        self.sample_ip = '127.0.0.1'
        self.project = 'presidiopy'

    def test_url_construction(self):
        api = PresidioPy(self.sample_ip, self.project)
        self.assertEqual(api.base_url, 'http://127.0.0.1:8080/api/v1/')

    def test_support_for_port_parameter(self):
        api = PresidioPy(self.sample_ip, self.project, port="8081")
        self.assertEqual(api.base_url, 'http://127.0.0.1:8081/api/v1/')

    def test_support_for_ssl_parameter(self):
        api = PresidioPy(self.sample_ip, self.project, ssl=True)
        self.assertEqual(api.base_url, 'https://127.0.0.1:8080/api/v1/')

    def test_can_generate_analyze_url(self):
        api = PresidioPy(self.sample_ip, self.project)
        self.assertEqual(api.analyze_url, 'http://127.0.0.1:8080/api/v1/projects/presidiopy/analyze')

    def test_hability_to_change_project(self):
        api = PresidioPy(self.sample_ip, self.project)
        api.change_project('ql')
        self.assertEqual(api.analyze_url, 'http://127.0.0.1:8080/api/v1/projects/ql/analyze')

    @mock.patch('requests.post', side_effect=mocked_requests_analyze)
    def test_can_request_an_analysis(self, mock):
        api = PresidioPy(self.sample_ip, self.project)
        output = api.analyze('text')
        self.assertEqual(output, [])

    @mock.patch('requests.post', side_effect=mocked_requests_analyze)
    def test_can_request_an_analysis_with_a_template(self, mock):
        api = PresidioPy(self.sample_ip, self.project)
        output = api.analyze('text', template = 'template_id')
        self.assertEqual(output, ['ok'])

    @mock.patch('requests.post', side_effect=mocked_requests_analyze)
    def test_can_request_an_analysis_with_defined_field(self, mock):
        api = PresidioPy(self.sample_ip, self.project)
        output = api.analyze('text', analyzeTemplate={"fields": [{"name": "field_name"}]})
        self.assertEqual(output, ['ok'])

    @mock.patch('requests.post', side_effect=mocked_requests_recognizers)
    def test_can_insert_field_type(self, mock):
        api = PresidioPy(self.sample_ip, self.project)
        field = {
            'value': {
                'entity': 'ROCKET',
                'language': 'en-us',
                'patterns': [
                    {
                        'name': 'rocket-recognizer',
                        'regex': '\\W*(rocket)\\W*',
                        'score': 1,
                    }
                ]
            }
        }
        output = api.add_field_type(field)
        self.assertEqual(output, [])

    def test_can_generate_recognizers_url(self):
        api = PresidioPy(self.sample_ip, self.project)
        self.assertEqual(api.recognizers_url, 'http://127.0.0.1:8080/api/v1/analyzer/recognizers/')

    @mock.patch('requests.get', side_effect=mocked_requests_error)
    def test_raises_error_when_presidio_is_not_available(self, mock):
        api = PresidioPy(self.sample_ip, self.project)
        with self.assertRaises(Exception):
            api.retrieve_recognizers()

    @mock.patch('requests.get', side_effect=mocked_requests_recognizers)
    def test_can_get_recognizers(self, mock):
        api = PresidioPy(self.sample_ip, self.project)
        self.assertEqual(api.retrieve_recognizers(), [])

    @mock.patch('requests.get', side_effect=mocked_requests_recognizers)
    def test_can_get_recognizer(self, mock):
        api = PresidioPy(self.sample_ip, self.project)
        self.assertEqual(api.retrieve_recognizers('recognizer_name'), [])

    @mock.patch('requests.get', side_effect=mocked_requests_field_types)
    def test_can_retrieve_field_types(self, mock):
        api = PresidioPy(self.sample_ip, self.project)
        self.assertEqual(api.retrieve_field_types(), [])
