def try_decorate(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        return f(*args, **kwargs)
    return decorated

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = session.get(c.auth, None)
        if auth:
            return f(*args, **kwargs)
        else:
            return authenticate()
    return decorated

def db_handle(f):
    @wraps(f)
    def handleException(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except py.errors.DuplicateKeyError as e:
            return dict({c.stat: c.s_dk})
        except py.errors.AutoReconnect:
            return dict({c.stat: 'mongodb replicaset down'})
        except: 
            return dict({c.stat: c.s_no})
    return handleException
