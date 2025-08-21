from typing import List, Dict, Optional

class ExhibitorBrowser:
    """
    Browse and view exhibitor information, sessions, and contact details.
    """
    
    def __init__(self):
        self.exhibitor_list = []
        self.selected_exhibitor = None
        self.exhibitor_logo = None
        self.exhibitor_name = ""
        self.about_text = ""
        self.sessions_list = []
        self.contact_email = ""
        self.website_url = ""
        self.social_links = {}
        self.booth_location = ""
        
    def load_exhibitors(self) -> List[Dict]:
        """Load all exhibitors for the event."""
        pass
        
    def view_exhibitor_details(self, exhibitor_id: str) -> Dict:
        """View detailed information about an exhibitor."""
        pass
        
    def get_exhibitor_sessions(self, exhibitor_id: str) -> List[Dict]:
        """Get all sessions by this exhibitor."""
        pass
        
    def get_contact_information(self, exhibitor_id: str) -> Dict:
        """Get exhibitor contact details."""
        pass
        
    def bookmark_exhibitor(self, exhibitor_id: str) -> bool:
        """Bookmark an exhibitor for quick access."""
        pass
        
    def search_exhibitors(self, query: str) -> List[Dict]:
        """Search exhibitors by name or category."""
        pass
        
    def filter_by_category(self, category: str) -> List[Dict]:
        """Filter exhibitors by category."""
        pass
        
    def get_booth_location(self, exhibitor_id: str) -> str:
        """Get physical booth location for exhibitor."""
        pass
        
    def schedule_meeting(self, exhibitor_id: str, time_slot: str) -> bool:
        """Schedule a meeting with exhibitor."""
        pass
        
    def export_exhibitor_info(self, exhibitor_id: str) -> str:
        """Export exhibitor information as PDF or vCard."""
        pass