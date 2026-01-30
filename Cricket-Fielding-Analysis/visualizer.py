import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from fielding_analyzer import CricketFieldingAnalyzer, load_sample_data

class FieldingVisualizer:
    def __init__(self, analyzer):
        self.analyzer = analyzer
        plt.style.use('seaborn-v0_8')
        
    def plot_player_comparison(self, players=None):
        """Create comparison chart for multiple players"""
        if players is None:
            players = list(set(event['Player_Name'] for event in self.analyzer.fielding_data))
        
        performances = []
        for player in players:
            perf = self.analyzer.calculate_performance_matrix(player)
            if perf:
                performances.append(perf)
        
        if not performances:
            print("No performance data available")
            return
            
        df = pd.DataFrame(performances)
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Cricket Fielding Performance Analysis', fontsize=16, fontweight='bold')
        
        # Net Runs Impact
        bars1 = ax1.bar(df['Player'], df['Net_Runs_Impact'], 
                       color=['green' if x >= 0 else 'red' for x in df['Net_Runs_Impact']])
        ax1.set_title('Net Runs Impact')
        ax1.set_ylabel('Runs')
        ax1.tick_params(axis='x', rotation=45)
        
        # Catch Success Rate
        bars2 = ax2.bar(df['Player'], df['Catch_Success_Rate'], color='skyblue')
        ax2.set_title('Catch Success Rate (%)')
        ax2.set_ylabel('Success Rate (%)')
        ax2.tick_params(axis='x', rotation=45)
        
        # Fielding Efficiency
        bars3 = ax3.bar(df['Player'], df['Fielding_Efficiency'], color='orange')
        ax3.set_title('Fielding Efficiency (%)')
        ax3.set_ylabel('Efficiency (%)')
        ax3.tick_params(axis='x', rotation=45)
        
        # Total Events
        bars4 = ax4.bar(df['Player'], df['Total_Events'], color='purple')
        ax4.set_title('Total Fielding Events')
        ax4.set_ylabel('Number of Events')
        ax4.tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('fielding_performance_comparison.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def plot_individual_breakdown(self, player_name):
        """Create detailed breakdown for individual player"""
        performance = self.analyzer.calculate_performance_matrix(player_name)
        if not performance:
            print(f"No data found for {player_name}")
            return
            
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
        fig.suptitle(f'Fielding Analysis: {player_name}', fontsize=16, fontweight='bold')
        
        # Catch/Drop breakdown
        catch_data = [performance['Catches'], performance['Drops']]
        ax1.pie(catch_data, labels=['Catches', 'Drops'], autopct='%1.1f%%', 
                colors=['green', 'red'], startangle=90)
        ax1.set_title('Catch Success/Failure')
        
        # Run Out breakdown
        runout_data = [performance['Run_Outs'], performance['Missed_Run_Outs']]
        if sum(runout_data) > 0:
            ax2.pie(runout_data, labels=['Successful', 'Missed'], autopct='%1.1f%%',
                    colors=['blue', 'orange'], startangle=90)
        ax2.set_title('Run Out Attempts')
        
        # Runs Impact
        runs_data = [performance['Runs_Saved'], performance['Runs_Conceded']]
        ax3.bar(['Runs Saved', 'Runs Conceded'], runs_data, color=['green', 'red'])
        ax3.set_title('Runs Impact')
        ax3.set_ylabel('Runs')
        
        # Performance Metrics
        metrics = ['Catch Success Rate', 'Run Out Success Rate', 'Fielding Efficiency']
        values = [performance['Catch_Success_Rate'], 
                 performance['Run_Out_Success_Rate'], 
                 performance['Fielding_Efficiency']]
        ax4.bar(metrics, values, color=['skyblue', 'lightgreen', 'gold'])
        ax4.set_title('Performance Percentages')
        ax4.set_ylabel('Percentage (%)')
        ax4.tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig(f'{player_name.replace(" ", "_")}_fielding_analysis.png', 
                   dpi=300, bbox_inches='tight')
        plt.show()
        
    def plot_team_heatmap(self, team_name):
        """Create heatmap of team fielding performance"""
        team_summary = self.analyzer.get_team_fielding_summary(team_name)
        if not team_summary:
            print(f"No data found for team {team_name}")
            return
            
        df = pd.DataFrame(team_summary)
        
        # Select key metrics for heatmap
        metrics = ['Catch_Success_Rate', 'Run_Out_Success_Rate', 'Fielding_Efficiency', 'Net_Runs_Impact']
        heatmap_data = df[['Player'] + metrics].set_index('Player')
        
        plt.figure(figsize=(10, 6))
        sns.heatmap(heatmap_data, annot=True, cmap='RdYlGn', center=50, 
                   fmt='.1f', cbar_kws={'label': 'Performance Score'})
        plt.title(f'{team_name} - Fielding Performance Heatmap')
        plt.tight_layout()
        plt.savefig(f'{team_name.replace(" ", "_")}_heatmap.png', dpi=300, bbox_inches='tight')
        plt.show()

def main():
    # Load sample data
    analyzer = load_sample_data()
    visualizer = FieldingVisualizer(analyzer)
    
    print("=== Cricket Fielding Visualization ===\n")
    
    # Generate all visualizations
    players = ["Virat Kohli", "Ravindra Jadeja", "Hardik Pandya"]
    
    print("1. Generating player comparison chart...")
    visualizer.plot_player_comparison(players)
    
    print("2. Generating individual player breakdowns...")
    for player in players:
        visualizer.plot_individual_breakdown(player)
    
    print("3. Generating team heatmap...")
    visualizer.plot_team_heatmap("India")
    
    print("\n✓ All visualizations generated and saved!")

if __name__ == "__main__":
    main()