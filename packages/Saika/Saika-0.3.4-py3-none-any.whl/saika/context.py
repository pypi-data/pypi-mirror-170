from flask import request, session, g, current_app

from saika import hard_code


class Context:
    request = request
    session = session
    current_app = current_app
    g = g

    @staticmethod
    def g_set(k, v):
        keys = Context.g_get(hard_code.GK_KEYS)
        if keys is None:
            keys = []
            setattr(g, hard_code.GK_KEYS, keys)

        keys.append(k)
        setattr(g, k, v)

    @staticmethod
    def g_get(k, default=None):
        return getattr(g, k, default)

    @staticmethod
    def g_all():
        r = {}
        for k in Context.g_get(hard_code.GK_KEYS, []):
            r[k] = Context.g_get(k)
        return r

    @staticmethod
    def get_view_function(endpoint=None):
        if endpoint is None:
            endpoint = request.endpoint
        f = current_app.view_functions.get(endpoint)
        f = getattr(f, '__func__', f)

        return f

    @staticmethod
    def get_real_ip():
        ip_addr = Context.request.remote_addr
        headers = dict([(str(k).lower(), str(v)) for k, v in Context.request.headers.items() if v])
        forward_ips = headers.get('X-Forwarded-For'.lower())  # type: str
        if forward_ips:
            real_ip = forward_ips.split(',').pop(0).strip()
            if real_ip:
                ip_addr = real_ip
        return ip_addr
