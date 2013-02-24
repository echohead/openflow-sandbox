"""
  h1 ---|          |     |          |--- h4
  h2 ---| switch 1 |-----| switch 2 |--- h5
  h3 ---|          |     |          |
"""

from mininet.topo import Topo

class Subnets( Topo ):

    def __init__( self ):
        Topo.__init__( self )

        sw1 = self.addSwitch('s1')
        sw2 = self.addSwitch('s2')
        self.addLink(sw1, sw2)

        h1 = self.addHost('h1')
        self.addLink(h1, sw1)

        h2 = self.addHost('h2')
        self.addLink(h2, sw1)

        h3 = self.addHost('h3')
        self.addLink(h3, sw1)

        h4 = self.addHost('h4')
        self.addLink(h4, sw2)

        h5 = self.addHost('h5')
        self.addLink(h5, sw2)

topos = { 'subnets': ( lambda: Subnets() ) }
