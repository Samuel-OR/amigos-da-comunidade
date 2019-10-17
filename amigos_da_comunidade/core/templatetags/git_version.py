from django.template import Library

register = Library()

import os
import subprocess

# Return the git revision as a string
@register.simple_tag
def git_version():
    def _minimal_ext_cmd(cmd):
        # construct minimal environment
        env = {}
        for k in ['SYSTEMROOT', 'PATH']:
            v = os.environ.get(k)
            if v is not None:
                env[k] = v
        # LANGUAGE is used on win32
        env['LANGUAGE'] = 'C'
        env['LANG'] = 'C'
        env['LC_ALL'] = 'C'
        out = subprocess.Popen(cmd, stdout = subprocess.PIPE, env=env).communicate()[0]
        return out

    try:
        out = _minimal_ext_cmd(['git', 'tag']).strip()
        # split('v') quebra a string em list, e o [-1] pego sempre o ultimo elemento
        GIT_REVISION = out.strip().decode('ascii').split('v')[-1]
    except OSError:
        GIT_REVISION = "Unknown"

    return GIT_REVISION
