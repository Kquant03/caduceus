import csv
import plotly.graph_objects as go

# Define the path to the CSV file
CSV_FILE = 'word_counts_and_measurements.csv'  # Update this to your CSV file path

def create_interactive_plot(csv_file, ratio_threshold=0.02, word_count_threshold=1000):
    word_counts = []
    measurements_ratios = []
    file_names = []
    
    # Read the CSV file
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            measurements_ratio = float(row['Measurements Ratio'])
            word_count = int(row['Word Count'])
            file_name = row['File Name']
            
            # Filter the data based on the thresholds
            if measurements_ratio > ratio_threshold and word_count > word_count_threshold:
                measurements_ratios.append(measurements_ratio)
                word_counts.append(word_count)
                file_names.append(file_name)
    
    # Create an interactive scatter plot using Plotly
    fig = go.Figure(data=go.Scatter(
        x=word_counts,
        y=measurements_ratios,
        mode='markers',
        marker=dict(
            size=10,
            color=measurements_ratios,
            colorscale='Viridis',
            showscale=True
        ),
        text=file_names,
        hovertemplate='File: %{text}<br>Word Count: %{x}<br>Measurements Ratio: %{y:.3f}<extra></extra>'
    ))
    
    fig.update_layout(
        title='Measurements Ratio vs Word Count (Subset)',
        xaxis_title='Word Count',
        yaxis_title='Measurements Ratio',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False
    )
    
    # Save the interactive plot as an HTML file
    fig.write_html('interactive_scatter_plot_subset.html')
    
    # Display the interactive plot
    fig.show()

if __name__ == "__main__":
    create_interactive_plot(CSV_FILE)