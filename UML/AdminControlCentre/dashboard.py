from typing import Dict, List, Optional
from datetime import datetime

class Dashboard:
    """
    Admin dashboard displaying live statistics, event overview, and pending tasks.
    """
    
    def __init__(self):
        self.admin_id = None
        self.last_refresh = datetime.now()
        self.live_stats = {}
        self.event_overview = {}
        self.recent_bookings = []
        self.pending_tasks = []
        self.navigation_menu = [
            "Dashboard", "Event Configuration", "User Management",
            "Exhibitors", "Bookings", "Reports", "Settings"
        ]
        
    def load_live_stats(self) -> Dict:
        """Load real-time statistics for the event."""
        pass
        
    def get_event_overview(self) -> Dict:
        """Get current event overview and summary."""
        pass
        
    def fetch_recent_bookings(self, limit: int = 10) -> List:
        """Fetch most recent booking activities."""
        pass
        
    def get_pending_tasks(self) -> List:
        """Retrieve all pending administrative tasks."""
        pass
        
    def refresh_dashboard(self) -> None:
        """Refresh all dashboard components with latest data."""
        pass
        
    def navigate_to_section(self, section: str) -> None:
        """Navigate to a specific admin section."""
        pass