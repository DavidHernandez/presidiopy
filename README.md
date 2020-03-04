# PresidioPY

PresidioPY is a wrapper around requests library to interact with [Microsoft Presidio](https://github.com/microsoft/presidio).

## Installation

`pip install presidiopy`

## Current support

### V1

| Path                                               | Method          | Supported |
| -------------------------------------------------- | --------------- | --------- |
| /api/v1/fieldTypes                                 | GET             | YES       |
| /api/v1/templates/:project/:action/:id             | GET             | NO        |
| /api/v1/templates/:project/:action/:id             | POST            | NO        |
| /api/v1/templates/:project/:action/:id             | PUT             | NO        |
| /api/v1/templates/:project/:action/:id             | DELETE          | NO        |
| /api/v1/projects/:project/analyze                  | POST            | YES       |
| /api/v1/projects/:project/anonymize                | POST            | NO        |
| /api/v1/projects/:project/anonymize-image          | POST            | NO        |
| /api/v1/projects/:project/schedule-scanner-cronjob | POST            | NO        |
| /api/v1/projects/:project/schedule-streams-job     | POST            | NO        |
| /api/v1/analyzer/recognizers                       | GET             | YES       |
| /api/v1/analyzer/recognizers/:id                   | GET             | YES       |
| /api/v1/analyzer/recognizers/:id                   | POST            | NO        |
| /api/v1/analyzer/recognizers/:id                   | PUT             | NO        |
| /api/v1/analyzer/recognizers/:id                   | DELETE          | NO        |

## Releasing new version

1. Increase version on setup.py
2. Clean `/dist` folder.
3. Generate new distribution files: `python3 setup.py sdist bdist_wheel`
4. Push it to PyPi: `python3 -m twine upload dist/*`

Check the documentation in case it is necessary: https://packaging.python.org/tutorials/packaging-projects/

## Development sponsor

The development of this library is sponsored by [QueryLayer](https://www.querylayer.com/): The next generation of Data-Sharing.
