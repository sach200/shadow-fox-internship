import pandas as pd
import numpy as np
from datetime import datetime
import json

class CricketFieldingAnalyzer:
    def __init__(self):
        self.fielding_data = []
        self.performance_matrix = {}
        
    def add_fielding_event(self, match_no, innings, team, player_name, ball_count, 
                          position, description, pick_type, throw_type, runs, 
                          over_count, venue):
        """Add a fielding event to the dataset"""
        event = {
            'Match_No': match_no,
            'Innings': innings,
            'Team': team,
            'Player_Name': player_name,
            'Ball_Count': ball_count,
            'Position': position,
            'Short_Description': description,
            'Pick': pick_type,
            'Throw': throw_type,
            'Runs': runs,
            'Over_Count': over_count,
            'Venue': venue,
            'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.fielding_data.append(event)
        
    def calculate_performance_matrix(self, player_name):
        """Calculate performance metrics for a specific player"""
        player_data = [event for event in self.fielding_data if event['Player_Name'] == player_name]
        
        if not player_data:
            return None
            
        total_events = len(player_data)
        clean_picks = sum(1 for event in player_data if event['Pick'] == 'clean pick')
        catches = sum(1 for event in player_data if event['Pick'] == 'catch')
        drops = sum(1 for event in player_data if event['Pick'] == 'drop catch')
        run_outs = sum(1 for event in player_data if event['Throw'] == 'run out')
        missed_run_outs = sum(1 for event in player_data if event['Throw'] == 'missed run out')
        
        total_runs_saved = sum(event['Runs'] for event in player_data if event['Runs'] > 0)
        total_runs_conceded = sum(abs(event['Runs']) for event in player_data if event['Runs'] < 0)
        
        performance = {
            'Player': player_name,
            'Total_Events': total_events,
            'Clean_Picks': clean_picks,
            'Catches': catches,
            'Drops': drops,
            'Catch_Success_Rate': round((catches / (catches + drops) * 100) if (catches + drops) > 0 else 0, 2),
            'Run_Outs': run_outs,
            'Missed_Run_Outs': missed_run_outs,
            'Run_Out_Success_Rate': round((run_outs / (run_outs + missed_run_outs) * 100) if (run_outs + missed_run_outs) > 0 else 0, 2),
            'Runs_Saved': total_runs_saved,
            'Runs_Conceded': total_runs_conceded,
            'Net_Runs_Impact': total_runs_saved - total_runs_conceded,
            'Fielding_Efficiency': round((clean_picks / total_events * 100) if total_events > 0 else 0, 2)
        }
        
        return performance
    
    def get_team_fielding_summary(self, team_name):
        """Get fielding summary for entire team"""
        team_data = [event for event in self.fielding_data if event['Team'] == team_name]
        players = list(set(event['Player_Name'] for event in team_data))
        
        team_summary = []
        for player in players:
            performance = self.calculate_performance_matrix(player)
            if performance:
                team_summary.append(performance)
                
        return sorted(team_summary, key=lambda x: x['Net_Runs_Impact'], reverse=True)
    
    def export_to_csv(self, filename='fielding_data.csv'):
        """Export fielding data to CSV"""
        df = pd.DataFrame(self.fielding_data)
        df.to_csv(filename, index=False)
        print(f"Data exported to {filename}")
        
    def generate_report(self, players=None):
        """Generate comprehensive fielding report"""
        if players is None:
            players = list(set(event['Player_Name'] for event in self.fielding_data))
            
        report = {
            'Match_Summary': {
                'Total_Events': len(self.fielding_data),
                'Players_Analyzed': len(players),
                'Generated_At': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            },
            'Player_Performances': []
        }
        
        for player in players:
            performance = self.calculate_performance_matrix(player)
            if performance:
                report['Player_Performances'].append(performance)
                
        return report

# Sample data for demonstration
def load_sample_data():
    analyzer = CricketFieldingAnalyzer()
    
    # Sample T20 match data - India vs Australia
    sample_events = [
        # Virat Kohli fielding events
        (1, 1, "India", "Virat Kohli", 3, "Cover", "Sharp fielding, direct hit attempt", "clean pick", "missed run out", -2, 5, "Melbourne Cricket Ground"),
        (1, 1, "India", "Virat Kohli", 6, "Cover", "Brilliant catch off fast bowler", "catch", "", 0, 8, "Melbourne Cricket Ground"),
        (1, 1, "India", "Virat Kohli", 2, "Point", "Quick pickup and throw", "clean pick", "run out", 4, 12, "Melbourne Cricket Ground"),
        (1, 1, "India", "Virat Kohli", 4, "Cover", "Fumbled the ball", "fumble", "", -1, 15, "Melbourne Cricket Ground"),
        
        # Ravindra Jadeja fielding events  
        (1, 1, "India", "Ravindra Jadeja", 1, "Point", "Lightning quick pickup and throw", "clean pick", "run out", 6, 3, "Melbourne Cricket Ground"),
        (1, 1, "India", "Ravindra Jadeja", 5, "Mid-wicket", "Spectacular diving catch", "catch", "", 0, 7, "Melbourne Cricket Ground"),
        (1, 1, "India", "Ravindra Jadeja", 3, "Point", "Direct hit from boundary", "clean pick", "run out", 8, 11, "Melbourne Cricket Ground"),
        (1, 1, "India", "Ravindra Jadeja", 2, "Cover", "Good fielding effort", "clean pick", "", 2, 16, "Melbourne Cricket Ground"),
        
        # Hardik Pandya fielding events
        (1, 1, "India", "Hardik Pandya", 4, "Long-on", "Dropped a sitter", "drop catch", "", -4, 6, "Melbourne Cricket Ground"),
        (1, 1, "India", "Hardik Pandya", 1, "Mid-off", "Clean pickup", "clean pick", "", 1, 9, "Melbourne Cricket Ground"),
        (1, 1, "India", "Hardik Pandya", 6, "Deep square leg", "Good throw to keeper", "good throw", "missed stumping", -2, 13, "Melbourne Cricket Ground"),
        (1, 1, "India", "Hardik Pandya", 3, "Mid-wicket", "Excellent catch under pressure", "catch", "", 0, 17, "Melbourne Cricket Ground")
    ]
    
    for event in sample_events:
        analyzer.add_fielding_event(*event)
        
    return analyzer

if __name__ == "__main__":
    # Load sample data
    analyzer = load_sample_data()
    
    # Generate and display performance reports
    players = ["Virat Kohli", "Ravindra Jadeja", "Hardik Pandya"]
    
    print("=== CRICKET FIELDING ANALYSIS REPORT ===\n")
    
    for player in players:
        performance = analyzer.calculate_performance_matrix(player)
        if performance:
            print(f"Player: {performance['Player']}")
            print(f"Total Events: {performance['Total_Events']}")
            print(f"Catches: {performance['Catches']} | Drops: {performance['Drops']}")
            print(f"Catch Success Rate: {performance['Catch_Success_Rate']}%")
            print(f"Run Outs: {performance['Run_Outs']} | Missed: {performance['Missed_Run_Outs']}")
            print(f"Run Out Success Rate: {performance['Run_Out_Success_Rate']}%")
            print(f"Net Runs Impact: {performance['Net_Runs_Impact']}")
            print(f"Fielding Efficiency: {performance['Fielding_Efficiency']}%")
            print("-" * 50)
    
    # Export data
    analyzer.export_to_csv('cricket_fielding_data.csv')
    
    # Generate comprehensive report
    report = analyzer.generate_report(players)
    with open('fielding_report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print("\nReport generated successfully!")