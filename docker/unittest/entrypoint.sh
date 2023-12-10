#!/bin/bash
echo "entrypoint executed"
export DISPLAY=:1

Xorg -noreset +extension GLX +extension RANDR +extension RENDER -logfile ./xdummy.log -config /etc/X11/xorg.conf :1 >/dev/null 2>&1  & 

# uncomment echo for debug purpose
# echo "$@"
# execute default CMD or overridden CMD
exec "$@"