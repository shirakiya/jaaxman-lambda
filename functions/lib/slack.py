import slackweb


class Slack(object):

    COLOR_GOOD = 'good'
    COLOR_WARNING = 'warning'
    COLOR_DANGER = 'danger'

    def __init__(self, incoming_webhook_url):
        self.slackweb = slackweb.Slack(url=incoming_webhook_url)

    def _notify(self, payload):
        self.slackweb.notify(**payload)

    def notify(self, job_name, message, color='good'):
        payload = {
            'username': 'Jaaxman',
            'channel': '#dev_notifications',
            'icon_emoji': ':jaaxman:',
            'attachments': [{
                'title': f'job ({job_name})',
                'text': message,
                'color': color,
                'mrkdwn_in': ['text', 'pretext'],
            }],
        }
        return self._notify(payload)
