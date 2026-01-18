
class Node():
    """!
    @brief Node base class.

    This class represents a generic node. It is a superclass for Hosts, Routers, etc.
    """

    __interfaces: List[(str, str)] # List of the (interface, network) tuples
    __containerName: str   # The corresponding container name


    def runCommand(cmd: str) -> str: call docker::exec_run():
        """!
        @brief Run a command on the node.

        @return Return the status of the command.
        """
        return 
        

    def start(): 
        """!
        @brief Start the container.
        """
        return 

    def stop():
        """!
        @brief Stop the container.
        """
        return

    def restart():
        """!
        @brief Restart the container. 
        """
        return 

    def joinNetwork(network:str):
        """!
        @brief Let the node container join a network. 

        This can be done while the container is still running.
        """
        return 

    def getIpAddresses() -> Dict[interface, ip]: 
        """!
        @brief Get the IP addresses of all the interfaces
        """
        return 
    
    def captureTraffic(interface: str, duration: int, file_path: str):
        """!
        @brief Start the traffic capture program (running tcpdump). 

        The captured data (pcap file) will be saved, and can be retrieved later.
        Note: we might want to use tshark, instead of tcpdump; its primary advantage 
        over tcpdump is its ability to extract specific protocol fields (like HTTP URLs, 
        DNS queries, or OSPF states) directly into structured formats.


        @return Return the status of the command
        """
        return 
        

    def addStaticRoute(destination: str, gateway: str): int 
        """!
        @brief Add a static route to the node's routing table

        @return Return the status of the command
        """
        return 

    def getRoutingTable(format='json', details=True) -> str
        """!
        @brief Get the result of 'ip -j --route' command (-j means JSON output)

        @return Return the JSON string (by default) or the normal output (without -j) 
        """
        return 

    def setLatency(interface: str, delay_ms: int, jitter_ms: int = 0):
        """!
        @brief Set the network latency on an interface 
        """
        return 

    def setPacketLoss(interface: str, percentage: float):
        """!
        @brief Set the packet loss on a network 
        """
        return 

    def setBandwidth(interface: str, limit: str):
        """!
        @brief Set the network bandwidth
        """
        return 

    def getQoSConfig(interface: str) -> Dict:
        """!
        @brief Get the OoS setup on the interface (latency, delay, and bandwith)
        """ 

    def clearTrafficControlRules(interface: str):
        """!
        @brief Clean the traffic control rules 
        """


