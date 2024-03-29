import matplotlib
matplotlib.use('Agg')  # Required for non-GUI backend
import matplotlib.pyplot as plt

def create_plot1(data1):
    # graph1
    Gwalior_df = data1
    plt.figure(figsize=(10, 4))
    plt.plot(Gwalior_df['Year'], Gwalior_df['RICE AREA (1000 ha)'], marker='o', linestyle='-', color='b')
    plt.title('Rice Area Over Time in Gwalior')
    plt.xlabel('Year')
    plt.ylabel('RICE AREA (1000 ha)')
    plt.grid(True)

    return plt

def create_plot2(data2):
    #graph 2
    Gwalior_df = data2
    plt.figure(figsize=(10, 6))
    plt.plot(Gwalior_df['Year'], Gwalior_df['RICE PRODUCTION (1000 tons)'], marker='o', linestyle='-', color='b', label='Rice Production')
    plt.plot(Gwalior_df['Year'], Gwalior_df['WHEAT PRODUCTION (1000 tons)'], marker='o', linestyle='-', color='r', label='Wheat Production')
    plt.plot(Gwalior_df['Year'], Gwalior_df['MAIZE PRODUCTION (1000 tons)'], marker='o', linestyle='-', color='g', label='Maize Production')

    plt.title('Crop Production Over Time in Gwalior')
    plt.xlabel('Year')
    plt.ylabel('Rice Production (1000 tons)')
    plt.grid(True)

    return plt