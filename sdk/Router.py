
class Router(Node):
    """!
    @brief Represent a router. It subclass the Node class.
    """

    # Because we need to dynamically construct BGP entries, we need to 
    # know its table names. The default names are those used when we 
    # construct the emulator.


    __ebgp_entry_prefix: str = 'ebgp_'
    __ibgp_entry_prefix: str = 'ibgp_'
    __ospf_table: str        = 't_ospf'
    __bgp_table: str         = 't_bgp'
    __direct_table: str      = 't_direct'
    __bgp_local_pref: int    = 30

    __is_border_router: bool


   def peerWithEbgp(self, peer: Router, relationship) -> Router: 
       """!
       @brief Peer with a EBGP router

       Make sure these two routers are directly connected.
       Add bgp entries to their BIRD include folder /etc/bird/include/
       """
       return self

   def peerWithIbgp(self, peer: Router) -> Router: 
       """!
       @brief Peer with an IBGP router

       Make sure these two routers belong to the same AS.
       Add ibgp entries to their BIRD include folder /etc/bird/include/
       """
       return self 

   def peerWithRs(self, ix, rs):
       """!
       @brief Peer with a router server in an IX.
       """
       return self.


   def getPeers(self, type='ebgp'):
       """!
       @brief Return a list of peers (ebgp or ibgp)
       """
       return self. 


