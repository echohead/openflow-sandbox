from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class Switch (object):
  def __init__ (self, connection):
    self.connection = connection
    connection.addListeners(self)

    self.mac_to_port = {}


  def resend_packet (self, packet_in, out_port):
    msg = of.ofp_packet_out()
    msg.data = packet_in

    action = of.ofp_action_output(port = out_port)
    msg.actions.append(action)

    self.connection.send(msg)

  def act_like_switch (self, packet, packet_in):
    src = str(packet.src)
    dst = str(packet.dst)

    self.mac_to_port[src] = packet_in.in_port

    if dst in self.mac_to_port:
      log.debug("installing flow: %s %s %i" % (src, dst, packet_in.in_port))

      msg = of.ofp_flow_mod()
      msg.match.dl_dst = packet.dst
      msg.match.dl_src = packet.src
      msg.idle_timeout = 15
      msg.hard_timeout = 30
      msg.actions.append(of.ofp_action_output(port = self.mac_to_port[dst]))
      self.connection.send(msg)
      self.resend_packet(packet_in, self.mac_to_port[dst])

    else:
      log.debug('unknown dst mac: ' + str(packet.dst))
      self.resend_packet(packet_in, of.OFPP_ALL)

  def _handle_PacketIn (self, event):
    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return
    packet_in = event.ofp # The actual ofp_packet_in message.
    self.act_like_switch(packet, packet_in)


def launch ():
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Switch(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
