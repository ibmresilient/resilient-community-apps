# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_randori"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_randori when called by `resilient-circuits config [-c|-u]`
    """
    config_data = None

#    config_data = u"""[fn_randori]
api_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpZCI6ImM0MWI3NzBhLTdkZTAtNDFiMy1hOWFjLTViOWIwMmNhYjZhMiIsInVzZXJuYW1lIjoiYXBpLWRyb3lAcmFuZG9yaS5jb20iLCJsYWJlbCI6IlFSYWRhciBTT0FSIERldmVsb3BtZW50Iiwidmlld19vcmciOiI5MjNhZjVkZC01MGNlLTRkODAtYTU1Zi03MDdkZmUwODQxMWUiLCJ0eXBlIjoiYXBpIiwicGVybXMiOlsibWlzc2luZy1hZmZpbGlhdGUiLCJhdXRoZW50aWNhdGVkIiwibW9kaWZ5LWRhdGEiLCJ1bmFmZmlsaWF0ZS1lbnRpdHkiLCJyZWFkLWRhdGEiLCJ0YWctd3JpdGUiXSwicGVybWlkcyI6WyJkZDYyNGI0NC0wNTIxLTQ4NTctODY5NC03ODljODM5M2ZkNzkiLCI1ZTIzOTAzMi1jYWNiLTQ3NjUtYjAyYS1iYTVhY2MxZjM3ZWQiLCJhNzNhY2NiOC0zYjI5LTQyMDctOTc2MC0yYTBmZjQ0MTIxZWMiLCI2N2NmN2Y3MC1hZTZjLTRjZTQtODRiOS1kZWI3ZDZiODgzZjgiLCIwZWQzMmM4NS03YjA5LTQxM2ItOWZlNy01NmQwZGEwYTQzNDQiLCJiNzJhNTc0OS05NGY0LTRiOGUtOTUzZi0yM2Q3MDI4MzM1MzEiXSwiaWF0IjoxNjY0ODM3NjUyLCJhbGciOiJSUzI1NiIsImp0aSI6ImVmN2EzZWM5LThiNjYtNDYyOC04NGZiLTZiMjkwZTM2YmU1NiJ9.msepALp71lEu5Se7XSgaNhwWuB83LyQGFj_WOAzPmozhg4TBi4DTbO-CkpLvpUqZVVwCiy_PU_KVJxQOWza7DNyHSPac0--cTYHZWvWlis4VldEyAqdDgCcpyrJgDqVTGA9D-oYsDtrqJ-k0jV2zKl3bpOQqbl937qv_3iu_VpCFUB6Hl6Hr87BwmxhkKJT-lOl7ox_e63QXDZVQOsq6dFIneJ3RqkX8r-mvWOEWJj3q2Pn5-SA5Rbn1xYxLPOvDKj8NFz5uDS4e7749ueyJeTTaxX_wopa4JL0ulf70xtiCHZgD2PRRttkEmpy2c-x0jF_rqpL33LPh0zRN61PfKg
endpoint_url=https://app.randori.io
# Number of seconds between poller cycles. A value of 0 disables the poller
polling_interval=60
# Number of minutes to lookback for queries the first time the poller runs.
polling_lookback=120
verify = false | /path/to/cafile.crt
# """
    return config_data
