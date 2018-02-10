import os
import requests
from lib.slack import Slack
from lib.exceptions import NotDefinedEnvironmentVariableError
from lib.logger import logger


DEFAULT_URL = 'http://localhost:8000/api/jobs/fetchrss'
TIMEOUT = 280


def getenv(name):
    try:
        return os.environ[name]
    except KeyError:
        raise NotDefinedEnvironmentVariableError(f'Environ variable "{name}" is not found.')


def get_slack():
    slack_url = getenv('SLACK_URL')
    return Slack(slack_url)


def get_headers():
    token = getenv('TOKEN')

    return {
        'Authorization': f'Bearer {token}',
    }


def get_stage():
    return os.getenv('STAGE', 'fetchrss-dev')


def get_url():
    stage = get_stage()

    return getenv('URL') if stage == 'production' else DEFAULT_URL


def lambda_handler():
    slack = get_slack()

    headers = get_headers()
    url = get_url()
    body = {}

    try:
        res = requests.post(url, json=body, headers=headers, timeout=TIMEOUT)

        if res.status_code == requests.codes.ok:
            job_finish_message = res.json()['message']
            slack.notify('fetchrss', job_finish_message)

            logger.info(job_finish_message)
        else:
            raise res.raise_for_status()
    except Exception as e:
        slack.notify('fetchrss', str(e), Slack.COLOR_DANGER)
        raise


if __name__ == '__main__':
    lambda_handler()
