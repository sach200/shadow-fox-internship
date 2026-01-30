from fielding_analyzer import CricketFieldingAnalyzer
import json

class FieldingDataCollector:
    def __init__(self):
        self.analyzer = CricketFieldingAnalyzer()
        self.pick_types = ['clean pick', 'good throw', 'fumble', 'bad throw', 'catch', 'drop catch']
        self.throw_types = ['run out', 'missed stumping', 'missed run out', 'stumping', '']
        
    def collect_event_data(self):
        """Interactive data collection for fielding events"""
        print("=== Cricket Fielding Data Collection ===\n")
        
        # Match details
        match_no = input("Enter Match Number: ")
        innings = int(input("Enter Innings (1 or 2): "))
        team = input("Enter Fielding Team: ")
        venue = input("Enter Venue: ")
        
        print(f"\nCollecting data for {team} fielding in innings {innings}")
        print("Enter 'done' as player name to finish data collection\n")
        
        while True:
            player_name = input("Player Name: ")
            if player_name.lower() == 'done':
                break
                
            try:
                ball_count = int(input("Ball Count (1-6): "))
                over_count = int(input("Over Number: "))
                position = input("Fielding Position: ")
                description = input("Short Description: ")
                
                print("\nPick Types:", ', '.join(self.pick_types))
                pick_type = input("Pick Type: ")
                
                print("\nThrow Types:", ', '.join(self.throw_types))
                throw_type = input("Throw Type (press Enter if none): ")
                
                runs = int(input("Runs (+saved/-conceded): "))
                
                self.analyzer.add_fielding_event(
                    match_no, innings, team, player_name, ball_count,
                    position, description, pick_type, throw_type, runs,
                    over_count, venue
                )
                
                print(f"✓ Event recorded for {player_name}\n")
                
            except ValueError:
                print("Invalid input. Please enter numbers where required.\n")
                continue
                
        return self.analyzer
    
    def quick_demo_data(self):
        """Load quick demo data for testing"""
        print("Loading demo data...")
        
        # Demo match: Mumbai Indians vs Chennai Super Kings
        events = [
            (101, 2, "Mumbai Indians", "Rohit Sharma", 4, "Mid-off", "Quick pickup and throw", "clean pick", "", 1, 8, "Wankhede Stadium"),
            (101, 2, "Mumbai Indians", "Rohit Sharma", 2, "Cover", "Brilliant diving catch", "catch", "", 0, 12, "Wankhede Stadium"),
            (101, 2, "Mumbai Indians", "Kieron Pollard", 6, "Long-on", "Dropped catch at boundary", "drop catch", "", -6, 15, "Wankhede Stadium"),
            (101, 2, "Mumbai Indians", "Kieron Pollard", 3, "Deep mid-wicket", "Good fielding effort", "clean pick", "", 2, 18, "Wankhede Stadium"),
            (101, 2, "Mumbai Indians", "Suryakumar Yadav", 1, "Point", "Direct hit run out", "clean pick", "run out", 5, 6, "Wankhede Stadium"),
            (101, 2, "Mumbai Indians", "Suryakumar Yadav", 5, "Cover", "Fumbled easy pickup", "fumble", "", -2, 14, "Wankhede Stadium")
        ]
        
        for event in events:
            self.analyzer.add_fielding_event(*event)
            
        print("Demo data loaded successfully!")
        return self.analyzer

def main():
    collector = FieldingDataCollector()
    
    print("Choose data collection method:")
    print("1. Manual data entry")
    print("2. Load demo data")
    
    choice = input("Enter choice (1 or 2): ")
    
    if choice == '1':
        analyzer = collector.collect_event_data()
    elif choice == '2':
        analyzer = collector.quick_demo_data()
    else:
        print("Invalid choice. Loading demo data...")
        analyzer = collector.quick_demo_data()
    
    # Generate analysis
    print("\n=== FIELDING ANALYSIS ===")
    
    # Get all players
    players = list(set(event['Player_Name'] for event in analyzer.fielding_data))
    
    for player in players:
        performance = analyzer.calculate_performance_matrix(player)
        if performance:
            print(f"\n{player}:")
            print(f"  Events: {performance['Total_Events']}")
            print(f"  Catches: {performance['Catches']} (Success: {performance['Catch_Success_Rate']}%)")
            print(f"  Run Outs: {performance['Run_Outs']} (Success: {performance['Run_Out_Success_Rate']}%)")
            print(f"  Net Impact: {performance['Net_Runs_Impact']} runs")
            print(f"  Efficiency: {performance['Fielding_Efficiency']}%")
    
    # Export data
    analyzer.export_to_csv('collected_fielding_data.csv')
    
    # Save detailed report
    report = analyzer.generate_report(players)
    with open('detailed_fielding_report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n✓ Data exported to CSV and JSON files")
    print(f"✓ Analysis complete for {len(players)} players")

if __name__ == "__main__":
    main()