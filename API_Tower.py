from urllib.error import HTTPError, URLError
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import json
#def make_request(url, headers=None):
def make_request(url, headers=None, data=None):
    #request = Request(url, headers=headers or {})
    request = Request(url, headers=headers or {}, data=data)
    try:
        with urlopen(request, timeout=10) as response:
            print(response.status)
            return response.read(), response
    except HTTPError as error:
        print(error.status, error.reason)
    except URLError as error:
        print(error.reason)
    except TimeoutError:
        print("Request timed out")
token = "ZMBOTRjBnGDmFoeJryIfmjnjCLPnz9"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
post_dict = {"extra_vars": {"vmname": "bal3551tst016", "osgroup": "rhel8_test","location":"ba_onprem" }}
json_string = json.dumps(post_dict)
post_data = json_string.encode("utf-8")
print(post_data)
tower_url = "https://tower.elc.internationalairlinesgroup.com/api/v2/job_templates/SCM_provision++SCM_SEC_TOOL/launch/"
resp = make_request(tower_url, headers, post_data)
print(resp)