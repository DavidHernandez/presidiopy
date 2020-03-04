# PresidioPY

PresidioPY is a wrapper around requests library to interact with [Microsoft Presidio](https://github.com/microsoft/presidio).

## Installation

`pip install presidiopy`

## Current support

### V1

| Path                                               | Method | Supported |
| /api/v1/fieldTypes                                 | GET    | NO        |
| /api/v1/templates/:project/:action/:id             | GET    | NO        |
| /api/v1/templates/:project/:action/:id             | POST   | NO        |
| /api/v1/templates/:project/:action/:id             | PUT    | NO        |
| /api/v1/templates/:project/:action/:id             | DELETE | NO        |
| /api/v1/projects/:project/analyze                  | POST   | YES       |
| /api/v1/projects/:project/anonymize                | POST   | NO        |
| /api/v1/projects/:project/anonymize-image          | POST   | NO        |
| /api/v1/projects/:project/schedule-scanner-cronjob | POST   | NO        |
| /api/v1/projects/:project/schedule-streams-job     | POST   | NO        |
| /api/v1/analyzer/recognizers                       | GET    | YES       |
| /api/v1/analyzer/recognizers/:id                   | GET    | YES       |
| /api/v1/analyzer/recognizers/:id                   | POST   | NO        |
| /api/v1/analyzer/recognizers/:id                   | PUT    | NO        |
| /api/v1/analyzer/recognizers/:id                   | DELETE | NO        |
