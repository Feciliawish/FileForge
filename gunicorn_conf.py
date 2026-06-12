import multiprocessing

# Optimized for 2-core 2GB server
bind = "127.0.0.1:5000"
workers = 2
threads = 4
worker_class = "gthread"

# Performance
max_requests = 2000
max_requests_jitter = 200
worker_connections = 1000
timeout = 600
graceful_timeout = 30
keepalive = 5

# Limit request size
limit_request_line = 0
limit_request_fields = 100
limit_request_field_size = 0

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Preload app for faster worker startup
preload_app = True
