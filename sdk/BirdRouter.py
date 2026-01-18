
class BirdRouter(Router):
    """!
    @brief Represent a Bird router. It subclasses the Node class.

    Contains two types of APIs: (1) peering APIs, (2) bird interaction APIs
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


    def createContainer(self): 
        """!
        @brief Create a container for this node

        Use the fixed docker image 
        """
        return


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
        @brief Peer with a router server in an IX (for ebgp).
        """
        return self.
 
    def peerWithRR(self, rr):
        """!
        @brief Peer with a router reflector (for ibgp).
        """
        return self.
 
 
    def getPeers(self, type='ebgp'):
        """!
        @brief Return a list of peers (ebgp or ibgp)
        """
        return self. 
 
    # The following APIs are for bird commands. 
    # Since BIRD doesn't provide native JSON, if we want to get the JSON output, 
    # the best way is to write out own "birdc" program to connect directly to the 
    # Unix Domain Socket (usually located at /run/bird/bird.ctl).
    def bird_show_protocols(self)  # Run "birdc show protocols ..."
    def bird_show_interfaces(self) # Run "birdc show interfaces"
    def bird_show_route(self)      # Run "birdc show routes ..."
    def bird_configure(self)       # Reloads the configuration file without restarting the daemon
    def bird_enable_protocol(self)  # Enable a protocol
    def bird_disable_protocol(self) # Disable a protocol
 
