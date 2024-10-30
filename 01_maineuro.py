# -*- coding: utf-8 -*-
"""MainEuro.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BtrEDHR0KxyeuOdssNbSjDiaQrLkIsSe
"""
from statsbombpy import sb

Competitions = sb.competitions()
Competitions

Euro = Competitions[(Competitions['competition_name'] == 'UEFA Euro') & (Competitions['season_name'] == '2024')]
Euro

Matches = sb.matches(competition_id = 55, season_id=282)
Matches

Spain = Matches[(Matches['home_team'] == 'Spain') | (Matches['away_team'] == 'Spain')]
Spain

Spain_Lineup = sb.lineups(match_id=3943043)["Spain"]
Spain_Lineup



Spain_events =  sb.events(match_id = 3943043, split=True, flatten_attrs=False)
Spain_events

Spain_Lineup.head(40)

player_positions = []
for index, player in Spain_Lineup.iterrows():
    positions = player['positions']
    if isinstance(positions, list) and len(positions) > 0:
        position = positions[0]
        print(f"Player: {player['player_name']}, Position Data: {position}")  # Print the position data to inspect its structure

import pandas as pd

import matplotlib.pyplot as plt

starting_xi_positions = []

for index, player in Spain_Lineup.iterrows():
    positions = player['positions']
    if isinstance(positions, list) and len(positions) > 0:
        position = positions[0]
        if position['start_reason'] == 'Starting XI':
            player_nickname = player['player_name']
            if player_nickname is None:
                player_nickname = player['player_name']
            starting_xi_positions.append({'player_name': player_nickname, 'position': position})

print(starting_xi_positions)

import mplsoccer

import matplotlib.pyplot as plt
from mplsoccer import Pitch,VerticalPitch
import pandas as pd

# Define a mapping from position names to pitch coordinates
position_to_coords = {
    'Goalkeeper': (10, 40),
    'Right Back': (30, 10),
    'Right Center Back': (30, 30),
    'Center Back': (30, 40),
    'Left Center Back': (30, 50),
    'Left Back': (30, 70),
    'Right Wing': (85, 10),
    'Right Midfield': (35, 25),
    'Center Midfield': (35, 40),
    'Left Midfield': (35, 55),
    'Left Wing': (85, 70),
    'Right Forward': (70, 25),
    'Center Forward': (100, 40),
    'Left Forward': (70, 55),
    'Right Wing Back': (35, 10),
    'Left Wing Back': (35, 70),
    'Left Defensive Midfield': (55, 60),
    'Right Defensive Midfield': (55, 20),
    'Center Attacking Midfield': (65, 40)
}

# Extract coordinates for the players
players_coordinates = []
for player in starting_xi_positions:
    position = player['position']['position']
    if position in position_to_coords:
        coord = position_to_coords[position]
        players_coordinates.append((player['player_name'], coord))
    else:
        print(f"Position {position} not found in mapping for player {player['player_name']}")

# Check the number of players in the starting XI
print(f"Total players in starting XI: {len(players_coordinates)}")
for player_name, coord in players_coordinates:
    print(f"Player: {player_name}, Coordinates: {coord}")

# Plot the pitch
# pitch = Pitch(pitch_type='statsbomb', pitch_color='grass', line_color='white')
# fig, ax = pitch.draw(figsize=(10, 7))
pitch = VerticalPitch(pitch_type='statsbomb', pitch_color='grass', line_color='white')
fig, ax = pitch.draw(figsize=(7, 10))
# Plot the players
for player_name, coord in players_coordinates:
    x, y = coord
    pitch.scatter(x, y, ax=ax, color='red', s=300, edgecolors='black')
    pitch.annotate(player_name, xy=(x, y), ax=ax, ha='center', va='center', color='yellow', fontsize=10, weight='bold')

plt.show()

substitution_positions = []

for index, player in Spain_Lineup.iterrows():
    positions = player['positions']
    if isinstance(positions, list) and len(positions) > 0:
        position = positions[0]
        if position['start_reason'] == 'Substitution - On (Tactical)':
            player_nickname = player['player_name']
            if player_nickname is None:
                player_nickname = player['player_name']
            substitution_positions.append({'player_name': player_nickname, 'position': position})

print(substitution_positions)

# Extract coordinates for the players
players_coordinates = []
for player in substitution_positions:
    position = player['position']['position']
    if position in position_to_coords:
        coord = position_to_coords[position]
        players_coordinates.append((player['player_name'], coord))
    else:
        print(f"Position {position} not found in mapping for player {player['player_name']}")

# Check the number of players in the starting XI
print(f"Total players in substitution: {len(players_coordinates)}")
for player_name, coord in players_coordinates:
    print(f"Player: {player_name}, Coordinates: {coord}")

# Plot the pitch
# pitch = Pitch(pitch_type='statsbomb', pitch_color='grass', line_color='white')
# fig, ax = pitch.draw(figsize=(10, 7))
pitch = VerticalPitch(pitch_type='statsbomb', pitch_color='grass', line_color='white')
fig, ax = pitch.draw(figsize=(7, 10))
# Plot the players
for player_name, coord in players_coordinates:
    x, y = coord
    pitch.scatter(x, y, ax=ax, color='red', s=300, edgecolors='black')
    pitch.annotate(player_name, xy=(x, y), ax=ax, ha='center', va='center', color='yellow', fontsize=10, weight='bold')

plt.show()

Spain_events

Spain_events = sb.events(3943043)

# Filter events for spain players
spain_pass_receptions = Spain_events[(Spain_events['team'] == 'Spain') & (Spain_events['type'] == 'Pass')]

# Extract necessary columns
receptions = spain_pass_receptions[['player', 'location', 'pass_recipient', 'timestamp']]
receptions

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch,VerticalPitch
import seaborn as sns

# Sample DataFrame with pass reception data
# data = {
#     'player': ['Unai Simón Mendibil', 'Robin Aime Robert Le Normand', 'Daniel Carvajal Ramos',
#                'Álvaro Borja Morata Martín', 'Daniel Carvajal Ramos'],
#     'location': [[6.9, 39.6], [8.9, 57.2], [28.6, 76.4], [61.9, 67.1], [72.5, 80.0]],
#     'pass_recipient': ['Robin Aime Robert Le Normand', 'Daniel Carvajal Ramos', 'Daniel Olmo Carvajal',
#                        'Lamine Yamal Nasraoui Ebana', 'Daniel Olmo Carvajal'],
#     'timestamp': ['00:00:34.440', '00:00:36.279', '00:00:39.436', '00:00:41.878', '00:00:56.844']
# }

df = pd.DataFrame(receptions)

# Create the pitch using mplsoccer
pitch = VerticalPitch(pitch_type='statsbomb', pitch_color='white', line_color='black', goal_type='box', figsize=(10, 6))

# Function to plot heatmap for each player
def plot_player_heatmap(player_name, player_df):
    fig, ax = pitch.draw()

    # Extract the x and y coordinates from the player's location data
    x = player_df['location'].apply(lambda loc: loc[0])
    y = player_df['location'].apply(lambda loc: loc[1])

    # Plot heatmap using seaborn kdeplot
    sns.kdeplot(x=x, y=y, shade=True, cmap="coolwarm", n_levels=30)

    # Set title for the player
    ax.set_title(f"{player_name}'s Pass Reception Heatmap", fontsize=20)

    # Show the plot
    plt.show()

# Loop through all players and generate heatmaps
players = df['player'].unique()

for player in players:
    # Filter data for the current player
    player_df = df[df['player'] == player]

    # Plot the heatmap for the player
    plot_player_heatmap(player, player_df)

position_to_coords

import pandas as pd

# The input list of player dictionaries



# Convert the list of dictionaries into a pandas DataFrame
# Extract the 'position' dictionary into separate columns using pandas `json_normalize`
spain_starting_xi_positions = pd.json_normalize(starting_xi_positions)
spain_starting_xi_positions.columns = ['player', 'position_id', 'position', 'from', 'to', 'from_period', 'to_period', 'start_reason', 'end_reason']


# Show the resulting DataFrame
print(spain_starting_xi_positions)

import pandas as pd

# The input list of player dictionaries



# Convert the list of dictionaries into a pandas DataFrame
# Extract the 'position' dictionary into separate columns using pandas `json_normalize`
spain_substitute_positions = pd.json_normalize(substitution_positions)
spain_substitute_positions.columns = ['player', 'position_id', 'position', 'from', 'to', 'from_period', 'to_period', 'start_reason', 'end_reason']


# Show the resulting DataFrame
print(spain_substitute_positions)

receptions

spain_ball_receiptions = Spain_events[(Spain_events['team'] == 'Spain') & (Spain_events['type'] == 'Ball Receipt*') & (Spain_events['possession_team'] == 'Spain')]

# Extract necessary columns
heatmap_positional = spain_ball_receiptions[['player','possession','position','location','timestamp']]
heatmap_positional

spain_starting_xi_positions

# Assuming your DataFrame is named 'player_positions' and has the following columns:
# 'player', 'position_id', 'position', 'from', 'to', 'from_period', 'to_period', 'start_reason', 'end_reason'

# Define a mapping from the position column to x, y coordinates (you can adjust these based on your specific needs)
position_coordinates = {
    'Goalkeeper': [50, 20],
    'Left Back': [25, 35],
    'Right Back': [75, 35],
    'Left Center Back': [35, 30],
    'Right Center Back': [65, 30],
    'Left Defensive Midfield': [35, 50],
    'Right Defensive Midfield': [65, 50],
    'Center Attacking Midfield': [50, 60],
    'Left Wing': [25, 70],
    'Right Wing': [75, 70],
    'Center Forward': [50, 75],
}

# Define a vertical pitch
pitch = VerticalPitch(pitch_type='statsbomb', pitch_color='grass', line_color='black',stripe = True)

# Create the figure for the overall formation
fig, ax = plt.subplots(figsize=(12, 16))  # Increased figure size for a larger pitch
pitch.draw(ax=ax)  # Draw the main pitch

# Loop through each player and plot their heatmap based on the position
for index, row in spain_starting_xi_positions.iterrows():
    player = row['player']
    position = row['position']

    # Get the coordinates for the player's position
    x, y = position_coordinates.get(position, [50, 50])  # Default to center if position is missing

    # Create subplot for the player's heatmap
    ax_sub = fig.add_axes([x / 100 - 0.05, y / 100 - 0.05, 0.1, 0.1], zorder=2)
    pitch.draw(ax=ax_sub)  # Draw individual pitch for each player

    # Extract player data for heatmap
    player_data = heatmap_positional[heatmap_positional['player'] == player]
    if not player_data.empty:
        locations = list(player_data['location'])
        x_locs, y_locs = zip(*locations)
        pitch.kdeplot(x_locs, y_locs, ax=ax_sub, shade=True, levels=50, shade_lowest=False, alpha=0.5)

    # Add player name
    ax_sub.text(60, 130, player, fontsize=10, ha='center', va='center', color='black', fontweight='bold')

# Set title and display plot
plt.suptitle('HeatMap (Spain Starting XI) - Spain vs. England (2024 Euro Final)', fontsize=20, y=0.9)
plt.show()

spain_substitute_positions

# Assuming your DataFrame is named 'player_positions' and has the following columns:
# 'player', 'position_id', 'position', 'from', 'to', 'from_period', 'to_period', 'start_reason', 'end_reason'

# Define a mapping from the position column to x, y coordinates (you can adjust these based on your specific needs)
position_coordinates = {
    'Goalkeeper': [50, 20],
    'Left Back': [25, 35],
    'Right Back': [75, 35],
    'Left Center Back': [35, 30],
    'Right Center Back': [65, 30],
    'Left Defensive Midfield': [35, 50],
    'Right Defensive Midfield': [65, 50],
    'Center Attacking Midfield': [50, 60],
    'Left Wing': [25, 70],
    'Right Wing': [75, 70],
    'Center Forward': [50, 75],
}

# Define a vertical pitch
pitch = VerticalPitch(pitch_type='statsbomb', pitch_color='grass', line_color='black',stripe=True)

# Create the figure for the overall formation
fig, ax = plt.subplots(figsize=(12, 16))  # Increased figure size for a larger pitch
pitch.draw(ax=ax)  # Draw the main pitch

# Loop through each player and plot their heatmap based on the position
for index, row in spain_substitute_positions.iterrows():
    player = row['player']
    position = row['position']

    # Get the coordinates for the player's position
    x, y = position_coordinates.get(position, [50, 50])  # Default to center if position is missing

    # Create subplot for the player's heatmap
    ax_sub = fig.add_axes([x / 100 - 0.05, y / 100 - 0.05, 0.1, 0.1], zorder=2)
    pitch.draw(ax=ax_sub)  # Draw individual pitch for each player

    # Extract player data for heatmap
    player_data = heatmap_positional[heatmap_positional['player'] == player]
    if not player_data.empty:
        locations = list(player_data['location'])
        x_locs, y_locs = zip(*locations)
        pitch.kdeplot(x_locs, y_locs, ax=ax_sub, shade=True, levels=50, shade_lowest=False, alpha=0.5)

    # Add player name
    ax_sub.text(60, 130, player, fontsize=10, ha='center', va='center', color='black', fontweight='bold')

# Set title and display plot
plt.suptitle('HeatMap (Substitute players) - Spain vs. England (2024 Euro Final)', fontsize=20, y=0.9)
plt.show()

position_coordinates = {
    'Goalkeeper': [50, 20],
    'Left Back': [25, 35],
    'Right Back': [75, 35],
    'Left Center Back': [35, 30],
    'Right Center Back': [65, 30],
    'Left Defensive Midfield': [35, 50],
    'Right Defensive Midfield': [65, 50],
    'Center Attacking Midfield': [50, 60],
    'Left Wing': [25, 70],
    'Right Wing': [75, 70],
    'Center Forward': [50, 75],
}


# Define the main pitch (with grass and stripes)
pitch_main = VerticalPitch(pitch_type='statsbomb', pitch_color='grass', line_color='black', stripe=True)

# Define the subplots pitch (with white background)
pitch_subplot = VerticalPitch(pitch_type='statsbomb', pitch_color='white', line_color='black')

# Create the figure for the overall formation
fig, ax = plt.subplots(figsize=(12, 16))  # Increased figure size for a larger pitch
pitch_main.draw(ax=ax)  # Draw the main pitch

# Loop through each player and plot their heatmap based on the position
for index, row in spain_starting_xi_positions.iterrows():
    player = row['player']
    position = row['position']

    # Get the coordinates for the player's position
    x, y = position_coordinates.get(position, [50, 50])  # Default to center if position is missing

    # Create subplot for the player's heatmap with white background
    ax_sub = fig.add_axes([x / 100 - 0.05, y / 100 - 0.05, 0.1, 0.1], zorder=2)
    pitch_subplot.draw(ax=ax_sub)  # Draw individual pitch for each player

    # Extract player data for heatmap
    player_data = heatmap_positional[heatmap_positional['player'] == player]
    if not player_data.empty:
        locations = list(player_data['location'])
        x_locs, y_locs = zip(*locations)
        pitch_subplot.kdeplot(x_locs, y_locs, ax=ax_sub, shade=True, levels=50, shade_lowest=False, alpha=0.5)

    # Add player name
    ax_sub.text(60, 130, player, fontsize=10, ha='center', va='center', color='black', fontweight='bold')

# Set title and display plot
plt.suptitle('HeatMap (Spain Starting XI) - Spain vs. England (2024 Euro Final)', fontsize=20, y=0.9)
plt.show()

position_coordinates = {
    'Goalkeeper': [50, 20],
    'Left Back': [25, 35],
    'Right Back': [75, 35],
    'Left Center Back': [35, 30],
    'Right Center Back': [65, 30],
    'Left Defensive Midfield': [35, 50],
    'Right Defensive Midfield': [65, 50],
    'Center Attacking Midfield': [50, 60],
    'Left Wing': [25, 70],
    'Right Wing': [75, 70],
    'Center Forward': [50, 75],
}


# Define the main pitch (with grass and stripes)
pitch_main = VerticalPitch(pitch_type='statsbomb', pitch_color='grass', line_color='black', stripe=True)

# Define the subplots pitch (with white background)
pitch_subplot = VerticalPitch(pitch_type='statsbomb', pitch_color='white', line_color='black')

# Create the figure for the overall formation
fig, ax = plt.subplots(figsize=(12, 16))  # Increased figure size for a larger pitch
pitch_main.draw(ax=ax)  # Draw the main pitch

# Loop through each player and plot their heatmap based on the position
for index, row in spain_substitute_positions.iterrows():
    player = row['player']
    position = row['position']

    # Get the coordinates for the player's position
    x, y = position_coordinates.get(position, [50, 50])  # Default to center if position is missing

    # Create subplot for the player's heatmap with white background
    ax_sub = fig.add_axes([x / 100 - 0.05, y / 100 - 0.05, 0.1, 0.1], zorder=2)
    pitch_subplot.draw(ax=ax_sub)  # Draw individual pitch for each player

    # Extract player data for heatmap
    player_data = heatmap_positional[heatmap_positional['player'] == player]
    if not player_data.empty:
        locations = list(player_data['location'])
        x_locs, y_locs = zip(*locations)
        pitch_subplot.kdeplot(x_locs, y_locs, ax=ax_sub, shade=True, levels=50, shade_lowest=False, alpha=0.5)

    # Add player name
    ax_sub.text(60, 130, player, fontsize=10, ha='center', va='center', color='black', fontweight='bold')

# Set title and display plot
plt.suptitle('HeatMap (Substitute Players) - Spain vs. England (2024 Euro Final)', fontsize=20, y=0.9)
plt.show()

Spain_events

Spain_events= Spain_events[Spain_events['team'] == 'Spain']
Spain_events

# Extract xG for shots
shots = Spain_events[Spain_events['type'] == 'Shot']
player_xg = shots.groupby('player')['shot_statsbomb_xg'].sum()

# Extract Key Passes (Passes leading to a shot)
passes = Spain_events[Spain_events['type'] == 'Pass']
key_passes = passes[passes['pass_outcome'].isna() & (passes['pass_goal_assist'] == True)]

# Extract Progressive Passes (You will need to calculate based on start and end locations)
progressive_passes = passes[passes['pass_end_location'].apply(lambda loc: loc[0] >= 60)]  # Example: passes ending in opponent's half

# Dribbles Completed
dribbles = Spain_events[(Spain_events['type'] == 'Dribble') & (Spain_events['dribble_outcome'] == 'Complete')]
player_dribbles = dribbles.groupby('player').size()

player_xg = shots.groupby('player')['shot_statsbomb_xg'].sum()
player_key_passes = key_passes.groupby('player').size()
player_progressive_passes = progressive_passes.groupby('player').size()
player_dribbles = dribbles.groupby('player').size()

# 1. Miscontrols
miscontrols = Spain_events[Spain_events['type'] == 'Miscontrol']
player_miscontrols = miscontrols.groupby('player').size()

# 2. Touches in the box
touches_in_box = Spain_events[
    ((Spain_events['type'] == 'Ball Receipt') | (Spain_events['type'] == 'Carry')) &
    (Spain_events['location'].notna()) &
    (Spain_events['location'].apply(lambda loc: isinstance(loc, list) and loc[0] >= 102 and 18 <= loc[1] <= 62))  # Penalty box coordinates
]
player_touches_in_box = touches_in_box.groupby('player').size()

# 3. Non-Penalty Goals
shots = Spain_events[Spain_events['type'] == 'Shot']
non_penalty_goals = shots[
    (shots['shot_outcome'] == 'Goal') & (shots['shot_type'] != 'Penalty')
]
player_non_penalty_goals = non_penalty_goals.groupby('player').size()

# 4. Through Balls
passes = Spain_events[Spain_events['type'] == 'Pass']
through_balls = passes[passes['pass_through_ball'] == True]
player_through_balls = through_balls.groupby('player').size()

# Shot-Creating Actions (Pass, Dribble, Foul Won)
sc_actions = Spain_events[
    (Spain_events['type'] == 'Pass') |
    (Spain_events['type'] == 'Dribble') |
    (Spain_events['type'] == 'Foul Won')
]
player_scas = sc_actions.groupby('player').size()

# Goal-Creating Actions (same actions but leading directly to a goal)
gc_actions = Spain_events[
    (Spain_events['type'] == 'Pass') |
    (Spain_events['type'] == 'Dribble') |
    (Spain_events['type'] == 'Foul Won') &
    (Spain_events['shot_outcome'] == 'Goal')
]
player_gcas = gc_actions.groupby('player').size()

# 7. Pressure Regains
pressure_regains = Spain_events[(Spain_events['type'] == 'Pressure') & (Spain_events['related_events'].notnull())]
player_pressure_regains = pressure_regains.groupby('player').size()

# Combine all extracted metrics into a single DataFrame
player_stats = pd.DataFrame({
    'xG': player_xg,
    'Key Passes': player_key_passes,
    'Progressive Passes': player_progressive_passes,
    'Dribbles Completed': player_dribbles,
    'Miscontrols': player_miscontrols,
    'Touches in Box': player_touches_in_box,
    'Non-Penalty Goals': player_non_penalty_goals,
    'Through Balls': player_through_balls,
    'Shot-Creating Actions': player_scas,
    'Goal-Creating Actions': player_gcas,
    'Pressure Regains': player_pressure_regains
})

# Filling NaN values with 0 for players without certain metrics
player_stats = player_stats.fillna(0)

# Display the player stats
print(player_stats)

spain_starting_xi_positions





# Ball Recoveries (players winning possession of the ball)
ball_recoveries = Spain_events[Spain_events['type'] == 'Ball Recovery']
player_ball_recoveries = ball_recoveries.groupby('player').size()


# Clearances
clearances = Spain_events[Spain_events['type'] == 'Clearance']
player_clearances = clearances.groupby('player').size()


# Defensive Duels (as a proxy for tackles, focusing on types like 'Tackle')
duels = Spain_events[
    (Spain_events['type'] == 'Duel') &
    (Spain_events['duel_type'].isin(['Tackle', 'Ground Loose Ball'])) &
    (Spain_events['duel_outcome'] == 'Won')
]
player_duels = duels.groupby('player').size()


# Adding Tackles, Clearances, and Duels to player_stats DataFrame
player_stats['Ball Recoveries'] = player_ball_recoveries
player_stats['Clearances'] = player_clearances
player_stats['Duels Won'] = player_duels

# Filling NaN values with 0 for players without certain metrics
player_stats = player_stats.fillna(0)

# Display the updated player stats
print(player_stats)

import matplotlib.pyplot as plt
from mplsoccer import Radar

# Updated radar chart parameters
params = [
    'xG', 'Key Passes', 'Progressive Passes', 'Dribbles Completed',
    'Miscontrols', 'Touches in Box', 'Non-Penalty Goals', 'Through Balls',
    'Shot-Creating Actions', 'Goal-Creating Actions', 'Pressure Regains',
    'Duels Won', 'Ball Recoveries', 'Clearances'
]

# Compute min and max ranges based on the data in player_stats dataframe
min_range = player_stats[params].min().values  # Minimum value for each parameter
max_range = player_stats[params].max().values  # Maximum value for each parameter

# Instantiate the radar chart
radar = Radar(params=params, min_range=min_range, max_range=max_range)

# Assuming you want to plot a specific player
player = 'Álvaro Borja Morata Martín'  # Replace with any player from your dataset
player_values = player_stats.loc[player, params].values  # Get values for the player

# Create a figure and axis using matplotlib
fig, ax = plt.subplots(figsize=(9, 9))  # Adjust size as necessary

# Plot the radar chart
radar.setup_axis(ax=ax)
# Draw inner circles
rings_inner = radar.draw_circles(ax=ax, facecolor='#ffb2b2', edgecolor='#fc5f5f')

# Draw the radar chart itself with player values
radar_output = radar.draw_radar(player_values, ax=ax,
                                kwargs_radar={'facecolor': '#aa65b2'},
                                kwargs_rings={'facecolor': '#66d8ba'})
radar_poly, rings_outer, vertices = radar_output

# Add range labels and parameter labels to the radar chart
range_labels = radar.draw_range_labels(ax=ax, fontsize=15)
param_labels = radar.draw_param_labels(ax=ax, fontsize=15)

# Add title manually with matplotlib
plt.title(f"{player} - Radar Chart", fontsize=20, color='red')

# Show the radar chart
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
from mplsoccer import Radar

# Radar chart parameters based on your data
params = [
    'xG', 'Key Passes', 'Progressive Passes', 'Dribbles Completed',
    'Miscontrols', 'Touches in Box', 'Non-Penalty Goals', 'Through Balls',
    'Shot-Creating Actions', 'Goal-Creating Actions', 'Pressure Regains',
    'Duels Won', 'Ball Recoveries', 'Clearances'
]

# Compute min and max ranges based on the data in player_stats dataframe
min_range = player_stats[params].min().values  # Minimum value for each parameter
max_range = player_stats[params].max().values  # Maximum value for each parameter

# Instantiate the radar chart
radar = Radar(params=params, min_range=min_range, max_range=max_range)

# Select a specific player
player = 'Álvaro Borja Morata Martín'  # Replace with any player from your dataset
player_values = player_stats.loc[player].values  # Get values for the player
player_position = spain_starting_xi_positions.loc[spain_starting_xi_positions['player'] == player, 'position'].values[0]  # Position


# Customize the theme with a completely black background
fig, ax = plt.subplots(figsize=(9, 9), facecolor='white')  # Set figure background to black
ax.set_facecolor('white')  # Set axis background to black

# Setup radar chart
radar.setup_axis(ax=ax)

# Draw inner circles with vibrant colors
rings_inner = radar.draw_circles(ax=ax, facecolor='#72b7b2', edgecolor='#1e615a')

# Draw the radar chart with contrasting colors
radar_output = radar.draw_radar(player_values, ax=ax,
                                kwargs_radar={'facecolor': '#ea2e7e', 'alpha': 0.6},
                                kwargs_rings={'facecolor': '#72b7b2', 'alpha': 0.4})
radar_poly, rings_outer, vertices = radar_output

# Draw range labels and parameter labels with custom fonts and sizes
range_labels = radar.draw_range_labels(ax=ax, fontsize=15, color='black')
param_labels = radar.draw_param_labels(ax=ax, fontsize=15, color='darkgray')

# Customize marker styles (e.g., diamonds) and edge colors for vertices
ax.scatter(vertices[:, 0], vertices[:, 1], color='yellow', edgecolor='black', s=50, marker='D', zorder=5)

# Set the title with multiple lines for name and position
plt.title(f"{player}\n{player_position}", fontsize=20, color='black', weight='bold', loc='left', pad=20)

# Adjust the grid lines to match the theme
# ax.grid(color='#333333')  # Set grid lines color to dark gray
plt.tight_layout()

# Show the radar chart
plt.show()

import matplotlib.pyplot as plt
from mplsoccer import Radar

# Radar chart parameters based on your data
params = [
    'xG', 'Key Passes', 'Progressive Passes', 'Dribbles Completed',
    'Miscontrols', 'Touches in Box', 'Non-Penalty Goals', 'Through Balls',
    'Shot-Creating Actions', 'Goal-Creating Actions', 'Pressure Regains',
    'Duels Won', 'Ball Recoveries', 'Clearances'
]


# Compute min and max ranges based on the data in player_stats dataframe
min_range = player_stats[params].min().values  # Minimum value for each parameter
max_range = player_stats[params].max().values  # Maximum value for each parameter

# Instantiate the radar chart
radar = Radar(params=params, min_range=min_range, max_range=max_range)

# Loop through each player in the spain_starting_xi_positions dataframe
for index, row in spain_starting_xi_positions.iterrows():
    player = row['player']  # Extract player name
    player_position = row['position']  # Extract player position

    # Get values for the player from player_stats dataframe
    player_values = player_stats.loc[player].values

    # Set the figure and axis for each player
    fig, ax = plt.subplots(figsize=(9, 9), facecolor='white')
    ax.set_facecolor('white')

    # Setup radar chart
    radar.setup_axis(ax=ax)

    # Draw inner circles
    rings_inner = radar.draw_circles(ax=ax, facecolor='#72b7b2', edgecolor='#1e615a')

    # Draw the radar chart with contrasting colors
    radar_output = radar.draw_radar(player_values, ax=ax,
                                    kwargs_radar={'facecolor': '#ea2e7e', 'alpha': 0.6},
                                    kwargs_rings={'facecolor': '#72b7b2', 'alpha': 0.4})
    radar_poly, rings_outer, vertices = radar_output

    # Draw range labels and parameter labels with custom fonts and sizes
    range_labels = radar.draw_range_labels(ax=ax, fontsize=15, color='black')
    param_labels = radar.draw_param_labels(ax=ax, fontsize=15, color='darkgray')

    # Customize marker styles for vertices (small circles)
    ax.scatter(vertices[:, 0], vertices[:, 1], color='yellow', edgecolor='black', s=50, marker='o', zorder=5)

    # Set the title with player name in red and position in yellow
    plt.text(0, 1.10, player, fontsize=20, color='black', weight='bold', ha='left', transform=ax.transAxes)
    plt.text(0, 1.05, player_position, fontsize=18, color='red', weight='bold', ha='left', transform=ax.transAxes)

    # Adjust the layout
    plt.tight_layout()

    # Show the radar chart for each player
    plt.show()
