from ipaddress import IPv4Network, IPv4Address

class Network():
    """!
    @brief The network class.

    This class represents a network.
    """
    __type: NetworkType
    __prefix: IPv4Network
    __name: str
    __scope: str

    __connected_nodes: List['Node']

    __d_latency: int       # in ms
    __d_bandwidth: int     # in bps
    __d_drop: float        # percentage

    __mtu: int


    def getNodes() -> List[str]:
        """!
        @brief Get the list of containers on the network.

        Use command: docker network inspect <network-id> --format='{{range .Containers}}{{.Name}} {{end}}'

        @return Return the list of container ids.
        """
        return 

    def setMtu(self, mtu: int) -> Network:
        """!
        @brief Set MTU of this network.

        @param mtu MTU.

        @returns self, for chaining API calls.
        """
        self.__mtu = mtu

        return self

    def setDefaultLinkProperties(self, latency: int = 0, bandwidth: int = 0, packetDrop: float = 0) -> Network:
        """!
        @brief Set default link properties of interfaces attached to the network.

        These settings will be applied to all the network interfaces connected to this network.
        If an individual node sets its own link properties, it will not refelct here. 

        @param latency (optional) latency to add to the link in ms, default 0. Note that this will be
        apply on all interfaces, meaning the rtt between two hosts will be 2 * latency.
        @param bandwidth (optional) egress bandwidth of the link in bps, 0 for unlimited, default 0.
        @param packetDrop (optional) link packet drop as percentage, 0 for unlimited, default 0.

        @returns self, for chaining API calls.
        """
        assert latency >= 0, 'invalid latency'
        assert bandwidth >= 0, 'invalid bandwidth'
        assert packetDrop >= 0 and packetDrop <= 100, 'invalid packet drop'

        self.__d_latency = latency
        self.__d_bandwidth = bandwidth
        self.__d_drop = packetDrop

        return self

    def getDefaultLinkProperties(self) -> Tuple[int, int, float]:
        """!
        @brief Get default link properties.

        @returns tuple (latency, bandwidth, packet drop)
        """
        return (self.__d_latency, self.__d_bandwidth, self.__d_drop)

    def getName(self) -> str:
        """!
        @brief Get name of this network.

        @returns name.
        """
        return self.__name

    def getType(self) -> NetworkType:
        """!
        @brief Get type of this network.

        @returns type.
        """
        return self.__type

    def getPrefix(self) -> IPv4Network:
        """!
        @brief Get prefix of this network.

        Use 'docker network inspect <docker id>' returns structured data.  
        Docker also provides a built-in way to extract specific fields using Go Templates
        Example: docker network inspect bridge --format='{{range .IPAM.Config}}{{.Subnet}}{{end}}'

        @returns prefix.
        """
        return self.__prefix


    def getDefaultRouter(self) -> IPv4Address:
        """!
        @brief Get default router for this network.

        @returns default router.
        """
        return 







