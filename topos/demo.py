from mininet.topo import Topo

class Demo( Topo ):
    def __init__( self ):
        Topo.__init__( self )

        switch = self.add_switch('switch0')

        for i in range(100):
          host = self.add_host('host%s' % i)
          self.add_link(host, switch)

topos = { 'demo': ( lambda: Demo() ) }
