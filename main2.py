from pyscript import document
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO

# Data Storage where its stores all selected days and absences
days = []
absences = []

# Function to display the graph based on user input
def displaying(e):

    # Get user input from HTML
    day = document.getElementById('dayOfTheWeek').value
    absence_value = document.getElementById('absences').value

    # If Absence value is empty or not a valid number, show warning
    if absence_value == "" or absence_value is None:
        document.getElementById('output').innerText = "Please enter a valid number of absences."
        return
    
    absence = int(absence_value)
    
    if absence < 0:
        document.getElementById('output').innerText = "Please enter a valid number of absences."
        return
    else:
        document.getElementById('output').innerText = ""

    # Save inputs into lists
    days.append(day)
    absences.append(absence)

    # Convert list to NumPy array (for plotting)
    converted_absences = np.array(absences)

    # Clear previous Graph
    plt.clf()
    plt.figure(figsize=(5, 4))

    # Create Graph
    plt.plot(days, converted_absences, marker='o')
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Day")
    plt.ylabel("Number of Absences")
    plt.grid()

    # Convert Graph to Image
    buffer = BytesIO()
    plt.tight_layout()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)

    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')

    # Display Graph inside HTML
    graph_div = document.getElementById("graph-area")
    graph_div.innerHTML = f'<img src="data:image/png;base64,{image_base64}" class="img-fluid"/>'
