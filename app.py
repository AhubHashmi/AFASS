from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from io import BytesIO
import base64
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsbombpy import sb
from mplsoccer import VerticalPitch
import seaborn as sns

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Function to encode matplotlib figures to base64
def create_chart(fig):
    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches='tight')
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')

# Step 1: Fetch competition and match data (from the original code)
competitions = sb.competitions()
euro_2024 = competitions[(competitions['competition_name'] == 'UEFA Euro') & (competitions['season_name'] == '2024')]
matches = sb.matches(competition_id=55, season_id=282)

# Filter matches involving Spain
spain_matches = matches[(matches['home_team'] == 'Spain') | (matches['away_team'] == 'Spain')]

# Fetch the lineup for a specific match (Spain vs. England, match_id = 3943043)
spain_lineup = sb.lineups(match_id=3943043)["Spain"]

# Step 2: Extract and process player positions (Starting XI)
starting_xi_positions = []
for index, player in spain_lineup.iterrows():
    positions = player['positions']
    if isinstance(positions, list) and len(positions) > 0:
        position = positions[0]
        if position['start_reason'] == 'Starting XI':
            starting_xi_positions.append({'player_name': player['player_name'], 'position': position['position']})

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
}

# Fetch event data for the match
spain_events = sb.events(match_id=3943043)

# Route to render the starting XI positions
@app.route('/chart/starting_xi')
def starting_xi_chart():
    players_coordinates = []
    for player in starting_xi_positions:
        position = player['position']
        if position in position_to_coords:
            coord = position_to_coords[position]
            players_coordinates.append((player['player_name'], coord))

    pitch = VerticalPitch(pitch_type='statsbomb', pitch_color='grass', line_color='white')
    fig, ax = pitch.draw(figsize=(7, 10))
    
    for player_name, coord in players_coordinates:
        x, y = coord
        pitch.scatter(x, y, ax=ax, color='red', s=300, edgecolors='black')
        pitch.annotate(player_name, xy=(x, y), ax=ax, ha='center', va='center', color='yellow', fontsize=10, weight='bold')
    
    plt.title('Spain Starting XI - Euro 2024 Final')
    
    chart = create_chart(fig)
    return jsonify({'chart': chart})

# Route for player pass reception heatmap
@app.route('/chart/player_heatmap/<player_name>')
def player_heatmap(player_name):
    receptions = spain_events[(spain_events['team'] == 'Spain') & (spain_events['type'] == 'Pass')]
    player_df = receptions[receptions['player'] == player_name]
    
    if player_df.empty:
        return jsonify({'error': 'No data found for this player'}), 404
    
    fig, ax = VerticalPitch(pitch_type='statsbomb', pitch_color='grass', line_color='white').draw()
    x = player_df['location'].apply(lambda loc: loc[0])
    y = player_df['location'].apply(lambda loc: loc[1])
    
    sns.kdeplot(x=x, y=y, shade=True, cmap="coolwarm", n_levels=30, ax=ax)
    ax.set_title(f"{player_name}'s Pass Reception Heatmap", fontsize=20)
    
    chart = create_chart(fig)
    return jsonify({'chart': chart})

# Route to get xG and other stats
@app.route('/stats/player_stats')
def player_stats():
    shots = spain_events[spain_events['type'] == 'Shot']
    player_xg = shots.groupby('player')['shot_statsbomb_xg'].sum()

    passes = spain_events[spain_events['type'] == 'Pass']
    key_passes = passes[passes['pass_outcome'].isna() & (passes['pass_goal_assist'] == True)]
    progressive_passes = passes[passes['pass_end_location'].apply(lambda loc: loc[0] >= 60)]

    dribbles = spain_events[(spain_events['type'] == 'Dribble') & (spain_events['dribble_outcome'] == 'Complete')]

    return jsonify({
        'xg_by_player': player_xg.to_dict(),
        'key_passes_by_player': key_passes.groupby('player').size().to_dict(),
        'progressive_passes_by_player': progressive_passes.groupby('player').size().to_dict(),
        'dribbles_by_player': dribbles.groupby('player').size().to_dict(),
    })

# Home route
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)