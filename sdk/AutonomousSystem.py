
class AutonomousSystem():
    """!
    @brief AutonomousSystem class.

    This class represents an autonomous system.
    """
    __asn: int
    __subnets: List[IPv4Network]
    __routers: Dict[str, Node]
    __hosts: Dict[str, Node]
    __nets: Dict[str, Network]
    __name_servers: List[str]

    def getNetworks() -> List[Network]:
        """!
        @brief Get all the networks inside this AS
        """
        return 

    def getRouters() -> List[Router]:
        """!
        @brief Get all the routers inside this AS
        """
        return

    def getHosts() -> List[Host]:
        """!
        @brief Get all the hosts inside this AS
        """
        return

    def getConnectedIXes() -> List[IX]:
        """!
        @brief Get all the Internet Exchanges connected to this AS
        """
        return

    def getNetWorkByName(name: str) -> Network
        """!
        @brief Get the net work inside this AS using its name 
        """
        return 


    def getNodes() -> List[Node]
        """!
        @brief Get the nodes inside this AS
        """
        return 

    def getNodesByNetwork(netName: str)  -> List[Node]
        """!
        @brief Get the nodes on a network
        """
        return 
     
    def getNodeByName(hostname: str)   -> Node
        """!
        @brief Get the node inside this AS using its name
        """
        return 

    def createHost(name: str, image: str):
        """!
        @brief create a new host inside the AS, and start it
        """
        return 

    def createNetwork(name: str, prefix: str):
        """!
        @brief create a network inside the AS 
        """
        return 

    def createRouter(name: str, image: str):
        """!
        @brief create a router inside the AS 
        """
        return 
    
    def removeNode(name: str):
        """!
        @brief remove a node from the AS 
        """
        return 

    def removeNetwork(name: str):
        """!
        @brief remove a network from the AS 
        """
        return 


