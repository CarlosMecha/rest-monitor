
import bottle
import psutil
import os

TOKEN = os.getenv('MONITOR_ACCESS_TOKEN')
if not TOKEN:
    print 'WARN: Token not specified, using the test one.'
    TOKEN = 'TEST_TOKEN'

def get_system_info():
    """
    Returns a dictionary with a bunch of monitoring data.
    It's a slow call, so be careful.
    """
    return {
        'cpu': psutil.cpu_percent(interval=1, percpu=True),
        'mem': psutil.virtual_memory().percent,
        'swap': psutil.swap_memory().percent,
        'disk': psutil.disk_usage('/').percent
    }

def valid_request(request):
    """
    Validates the current request.
    """
    return TOKEN == request.get_header('Auth-Token')

@bottle.route('/')
def index():
    """
    Sends the info as a JSON object.
    """
    if valid_request(bottle.request):
        return get_system_info()
    else:
        bottle.response.status = '403 Forbidden'
        return {}

if __name__ == '__main__':
    bottle.run(host='0.0.0.0', port=3344)

