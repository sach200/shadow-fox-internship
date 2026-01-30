# Cricket Fielding Analysis System

A comprehensive Python-based system for analyzing cricket fielding performance in T20 matches. This project provides detailed insights into individual player fielding contributions and their impact on team defensive play.

## Features

- **Data Collection**: Interactive and programmatic fielding event recording
- **Performance Analysis**: Comprehensive metrics calculation for individual players
- **Team Analysis**: Team-wide fielding performance summaries
- **Visualization**: Charts, graphs, and heatmaps for performance insights
- **Export Capabilities**: CSV and JSON export functionality

## Dataset Features

The system tracks the following fielding metrics:

- **Match No.**: Identifier for the match
- **Innings**: Which innings the data is recorded for (1 or 2)
- **Team**: The team in the field
- **Player Name**: The fielder involved in the action
- **Ball Count**: Sequence number of the ball in the over (1-6)
- **Position**: Fielding position at the time of the ball
- **Short Description**: Brief description of the fielding event
- **Pick**: Categorized as clean pick, good throw, fumble, bad throw, catch, or drop catch
- **Throw**: Classified as run out, missed stumping, missed run out, or stumping
- **Runs**: Number of runs saved (+) or conceded (-) through fielding effort
- **Over Count**: The over number in which the event occurred
- **Venue**: Location of the match

## Performance Metrics Calculated

- **Catch Success Rate**: Percentage of successful catches
- **Run Out Success Rate**: Percentage of successful run out attempts
- **Fielding Efficiency**: Percentage of clean picks
- **Net Runs Impact**: Total runs saved minus runs conceded
- **Total Events**: Number of fielding actions recorded

## Installation

1. Clone or download the project files
2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### 1. Basic Analysis with Sample Data

```python
from fielding_analyzer import load_sample_data

# Load sample data (India vs Australia T20)
analyzer = load_sample_data()

# Analyze specific player
performance = analyzer.calculate_performance_matrix("Virat Kohli")
print(performance)

# Get team summary
team_summary = analyzer.get_team_fielding_summary("India")
```

### 2. Interactive Data Collection

```python
from data_collector import FieldingDataCollector

collector = FieldingDataCollector()
analyzer = collector.collect_event_data()  # Interactive input
# OR
analyzer = collector.quick_demo_data()     # Load demo data
```

### 3. Generate Visualizations

```python
from visualizer import FieldingVisualizer

visualizer = FieldingVisualizer(analyzer)
visualizer.plot_player_comparison(["Player1", "Player2", "Player3"])
visualizer.plot_individual_breakdown("Player Name")
visualizer.plot_team_heatmap("Team Name")
```

### 4. Run Complete Analysis

```bash
python fielding_analyzer.py    # Run sample analysis
python data_collector.py       # Interactive data collection
python visualizer.py          # Generate all visualizations
```

## Sample Data Included

The system includes sample data from a T20 match featuring:

**India vs Australia at Melbourne Cricket Ground**

**Players Analyzed:**
- **Virat Kohli**: 4 fielding events (1 catch, 1 run out, 1 missed run out, 1 fumble)
- **Ravindra Jadeja**: 4 fielding events (1 catch, 2 run outs, excellent efficiency)
- **Hardik Pandya**: 4 fielding events (1 catch, 1 drop, mixed performance)

## File Structure

```
cricket_fielding_analysis/
├── fielding_analyzer.py      # Main analysis engine
├── data_collector.py         # Interactive data collection
├── visualizer.py            # Performance visualization
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Output Files Generated

- `cricket_fielding_data.csv`: Raw fielding event data
- `fielding_report.json`: Comprehensive performance report
- `fielding_performance_comparison.png`: Player comparison charts
- `[Player_Name]_fielding_analysis.png`: Individual player breakdowns
- `[Team_Name]_heatmap.png`: Team performance heatmap

## Key Classes and Methods

### CricketFieldingAnalyzer
- `add_fielding_event()`: Record new fielding event
- `calculate_performance_matrix()`: Calculate player metrics
- `get_team_fielding_summary()`: Team-wide analysis
- `export_to_csv()`: Export data to CSV
- `generate_report()`: Create comprehensive report

### FieldingDataCollector
- `collect_event_data()`: Interactive data entry
- `quick_demo_data()`: Load demonstration data

### FieldingVisualizer
- `plot_player_comparison()`: Multi-player comparison charts
- `plot_individual_breakdown()`: Detailed player analysis
- `plot_team_heatmap()`: Team performance heatmap

## Example Performance Output

```
Player: Virat Kohli
Total Events: 4
Catches: 1 | Drops: 0
Catch Success Rate: 100.0%
Run Outs: 1 | Missed: 1
Run Out Success Rate: 50.0%
Net Runs Impact: 1 runs
Fielding Efficiency: 50.0%
```

## Advanced Features

- **Real-time Analysis**: Add events and get instant performance updates
- **Multiple Match Support**: Track performance across multiple matches
- **Position-based Analysis**: Analyze performance by fielding position
- **Export Capabilities**: Multiple export formats for further analysis

## Future Enhancements

- Database integration for persistent storage
- Web interface for easier data entry
- Advanced statistical analysis
- Machine learning predictions
- Integration with ball-by-ball commentary data

## Contributing

Feel free to contribute by:
- Adding new performance metrics
- Improving visualization capabilities
- Adding support for different cricket formats
- Enhancing the user interface

## License

This project is open source and available for educational and analytical purposes.