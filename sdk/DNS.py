
class DNS:
    """!
    @brief Represent the entire DNS infrastructure
    """

    def getDNSServers(zone) -> List[Node], the first is master
    def getResolvers()-> List[Node], return the list of DNS resolvers (local DNS servers)

    
    def addZoneServer(zone, nameserver, master=True): 
        """!
        @brief Create a container and uses it to host a zone 
        """
        return

    def getZoneServerNames(self, domain: str) -> List[(str, int)]:
        """!
        @brief Get the names of servers hosting the given zone. 

        @param domain domain.

        @returns list of tuple of (node name, asn)
        """


    __servers: List[DNSServer]  # List of DNS servers 

