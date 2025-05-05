from django.shortcuts import render, redirect
from .models import UploadedFile
import pandas as pd

def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        instance = UploadedFile(file=uploaded_file)
        instance.save()
        # Example: Read the file
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith('.json'):
            df = pd.read_json(uploaded_file)
        # Process df as needed
        return render(request, 'analyzer/result.html', {'data': df.to_html()})
    return render(request, 'analyzer/upload.html')