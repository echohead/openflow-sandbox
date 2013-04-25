openflow-sandbox
================

A sandbox for playing with openflow controllers
written in python using pox.

install system dependencies:
```bash
bin/install-dependencies
```

install pox and custom topos / controllers:
```bash
bin/install-pox
```

start a mininet network from a topo name:
```bash
bin/mininet <simple|linear|subnets|...>
```

start a controller by name:
```bash
bin/start <switch|...>
```

show currently-configured flows:
```bash
bin/dp-dump
```



### mininet notes
useful commands:
`nodes` `pingall` `iperf`

#### reference controllers
`controller ptcp:`
`pox.py log.level --DEBUG misc.of_tutorial`
