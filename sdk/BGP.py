
class BGP():
    """!
    @brief Represent the entire BGP infrastructure (similar to the BGP layers) in the emulator.
    """

    def addPrivatePeering(self, ix: int, a: int, b: int, abRelationship: PeerRelationship = PeerRelationship.Peer) -> BGP:
        """!
        @brief @brief Setup private peering between two ASes in IX.
        """
        return self

    def addRsPeer(self, ix: int, peer: int) -> Ebgp:
        """!
        @brief Set up RS peering for an AS.
        """
        return self




