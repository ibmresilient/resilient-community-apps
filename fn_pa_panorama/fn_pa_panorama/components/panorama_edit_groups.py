import requests, time
from bs4 import BeautifulSoup as BS

rule_path = "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/rulebase/security/rules"
sample_rule = """
<uid-message>
  <type>update</type>
  <payload>
    <groups>
      <entry name="group1">
        <members>
          <entry name="user1"/>
          <entry name="domain\user2"/>
        </members>
      </entry>
      <entry name="group2">
        <members>
          <entry name="user3"/>
        </members>
      </entry>
    </groups>
  </payload>
</uid-message>
"""

# try:
#     response = requests.get("https://192.168.1.104/api/?type=keygen&user=admin&password=admin", verify=False, timeout=5)
#     response.raise_for_status()
# except requests.exceptions.RequestException as e:
#     print(e)
# # except requests.exceptions.HTTPError as httperr:
# #     print(httperr)
# # except requests.exceptions.Timeout as timeouterr:
# #     print(timeouterr)
# # except requests.exceptions.ConnectionError as connerr:
# #     print(connerr)
# # except requests.exceptions.ConnectTimeout as conntimeout:
# #     print(conntimeout)
#
# try:
#     soup = BS(response.content, 'html.parser')
#     key = soup.find('key').text
# except AttributeError as ae:
#     print("Error while parsing response:", ae)

key = "LUFRPT0rZjBWbXJ4Skd5R21KVTM3TEhNakhBMXdtZ0U9M0NCZkhWTFhSK3lmaTk4SEc3bXE0UjdGekY2NlB2NEVQOG5FMENuTzlTYz0="

try:
    r = requests.post(
        "https://9.70.194.108/api/?type=config&action=set&key={}&xpath={}&element={}".format(key, rule_path,
                                                                                              sample_rule),
        verify=False, timeout=5)
    r.raise_for_status()
except requests.exceptions.RequestException as e:
    print(e)
# except requests.exceptions.HTTPError as httperr:
#     print(httperr)
# except requests.exceptions.Timeout as timeouterr:
#     print(timeouterr)
# except requests.exceptions.ConnectionError as connerr:
#     print(connerr)
# except requests.exceptions.ConnectTimeout as conntimeout:
#     print(conntimeout)
time.sleep(3)

try:
    commit_response = requests.post("https://9.70.194.108/api/?type=commit&key={}&cmd=<commit></commit>".format(key),
                                    verify=False, timeout=5)
    commit_response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(e)
# except requests.exceptions.HTTPError as httperr:
#     print(httperr)
# except requests.exceptions.Timeout as timeouterr:
#     print(timeouterr)
# except requests.exceptions.ConnectionError as connerr:
#     print(connerr)
# except requests.exceptions.ConnectTimeout as conntimeout:
#     print(conntimeout)