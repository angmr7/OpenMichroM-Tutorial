import matplotlib.pyplot as plt
import numpy as np

def plot_traj(sim_chr10, beads=True, tube=False):
    xyz = sim_chr10.getPositions()
    
    x = xyz[:, 0]
    y = xyz[:, 1]
    z = xyz[:, 2]
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Color the beads by sequence
    num_points = len(x)
    colors = plt.cm.coolwarm(np.linspace(0, 1, num_points))
    
    # Plotting the data 
    ## beads
    if beads:
        ax.scatter(x, y, z, c=colors, marker='o')
    
    ## tube
    if tube:
        for i in range(num_points - 1):
            ax.plot([x[i], x[i + 1]], [y[i], y[i + 1]], [z[i], z[i + 1]], color=colors[i], linestyle='--')
        
    
    # Adding labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    # Display the plot
    plt.show()