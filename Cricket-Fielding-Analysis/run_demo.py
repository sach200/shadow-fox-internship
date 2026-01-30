import sys
sys.path.append('.')
from data_collector import FieldingDataCollector

collector = FieldingDataCollector()
analyzer = collector.quick_demo_data()

print("\n=== FIELDING ANALYSIS ===")
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

analyzer.export_to_csv('demo_fielding_data.csv')
print(f"\n✓ Analysis complete for {len(players)} players")