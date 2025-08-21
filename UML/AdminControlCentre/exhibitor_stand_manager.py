from typing import List, Dict, Optional

class ExhibitorStandManager:
    """
    Manages exhibitor stands, assignments, and expo map configuration.
    """
    
    def __init__(self):
        self.stands = []
        self.exhibitors = []
        self.view_mode = "table"  # table or visual
        self.expo_map = None
        self.pending_assignments = []
        
    def create_new_stand(self, stand_id: str, location: str) -> Dict:
        """Create a new exhibitor stand."""
        pass
        
    def edit_stand(self, stand_id: str, updates: Dict) -> bool:
        """Edit existing stand details."""
        pass
        
    def assign_exhibitor(self, stand_id: str, exhibitor_id: str) -> bool:
        """Assign an exhibitor to a stand."""
        pass
        
    def unassign_exhibitor(self, stand_id: str) -> bool:
        """Remove exhibitor assignment from a stand."""
        pass
        
    def get_stand_status(self, stand_id: str) -> str:
        """Get current status of a stand (available/pending/occupied)."""
        pass
        
    def toggle_view_mode(self) -> str:
        """Toggle between table and visual map view."""
        pass
        
    def publish_expo_map(self) -> bool:
        """Publish the expo map for attendees."""
        pass
        
    def save_changes(self) -> None:
        """Save all pending stand changes."""
        pass
        
    def get_exhibitor_list(self) -> List[Dict]:
        """Get list of all exhibitors and their assigned stands."""
        pass
        
    def import_stands(self, file_path: str) -> int:
        """Import stand configuration from file."""
        pass