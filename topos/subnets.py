"""
  h1 ---|          |     |          |--- h4
  h2 ---| switch 1 |-----| switch 2 |--- h5
  h3 ---|          |     |          |
"""

from mininet.topo import Topo

class Subnets( Topo ):

    def __init__( self ):
        Topo.__init__( self )

        sw1 = self.add_switch('s1')
        sw2 = self.add_switch('s2')
        self.add_link(sw1, sw2)

        h1 = self.add_host('h1')
        self.add_link(h1, sw1)

        h2 = self.add_host('h2')
        self.add_link(h2, sw1)

        h3 = self.add_host('h3')
        self.add_link(h3, sw1)

        h4 = self.add_host('h4')
        self.add_link(h4, sw2)

        h5 = self.add_host('h5')
        self.add_link(h5, sw2)

topos = { 'subnets': ( lambda: Subnets() ) }
