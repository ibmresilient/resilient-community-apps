# -----------------------------------------------------------------------------
# The 'CustomThreatService' component
# -----------------------------------------------------------------------------
[custom_threat_service]

# Base URL for threat services API
urlbase=/cts

# Whether we support file upload (for "file"-type artifacts)
# upload_file=False

# Retry time indicators
#first_retry_secs=5
#later_retry_secs=60
#max_retries=60

# Cache management
#cache_size=10000
#cache_ttl=600000

# tests can be run with a minimal mock in the [resilient] section,
#resilient_mock=rc_cts.lib.resilient_mock.MyResilientMock

