
#
import matplotlib
matplotlib.use("Agg")  # Use the backend that does not require an X server
import matplotlib.pyplot as plt
import numpy as np
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os



def generate_graph(request):
    if request.method == 'POST':
        # Get user input from the form
        start = float(request.POST.get('start'))
        end = float(request.POST.get('end'))
        step = float(request.POST.get('step'))

        # Generate x values
        x = np.arange(start, end, step)

        # Generate y values (sine function)
        y = np.sin(x)

        # Create the plot
        plt.plot(x, y)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Sine Graph')

        # Save the plot to a temporary image file
        temp_img_path = os.path.join(settings.MEDIA_ROOT, 'sine_graph.png')
        plt.savefig(temp_img_path)
        plt.close()

        # Prepare the context data to pass to the template
        context = {'graph_generated': True, 'image_path': settings.MEDIA_URL + 'sine_graph.png'}
        return render(request, 'graph.html', context)

    return render(request, 'graph.html')


def index(request):
    return render(request, 'index.html')

