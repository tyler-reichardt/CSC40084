from typing import List, Dict, Optional
from datetime import datetime

class SessionAssignments:
    """
    Manage moderator's assigned sessions and availability.
    """
    
    def __init__(self):
        self.moderator_id = None
        self.assigned_sessions = []
        self.upcoming_talks = []
        self.confirmed_sessions = []
        self.pending_confirmations = []
        self.availability_status = {}
        
    def get_assigned_sessions(self) -> List[Dict]:
        """Get all sessions assigned to moderator."""
        pass
        
    def get_upcoming_talks(self) -> List[Dict]:
        """Get list of upcoming talks to moderate."""
        pass
        
    def confirm_availability(self, session_id: str) -> bool:
        """Confirm availability for a session."""
        pass
        
    def decline_session(self, session_id: str, reason: str) -> bool:
        """Decline moderation assignment with reason."""
        pass
        
    def get_session_details(self, session_id: str) -> Dict:
        """Get detailed information about assigned session."""
        pass
        
    def request_reassignment(self, session_id: str, reason: str) -> bool:
        """Request reassignment of a session."""
        pass
        
    def update_availability(self, date: datetime, available: bool) -> None:
        """Update availability for specific dates."""
        pass
        
    def get_session_materials(self, session_id: str) -> List[Dict]:
        """Get materials for session preparation."""
        pass
        
    def join_session(self, session_id: str) -> bool:
        """Join a live session for moderation."""
        pass
        
    def get_speaker_info(self, session_id: str) -> Dict:
        """Get information about session speaker."""
        pass
        
    def get_moderation_guidelines(self) -> Dict:
        """Get moderation guidelines and policies."""
        pass
        
    def export_schedule(self, format: str = "ics") -> bytes:
        """Export moderation schedule."""
        pass