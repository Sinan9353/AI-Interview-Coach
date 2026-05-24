from django.shortcuts import render
from .forms import ResumeForm
import PyPDF2
from openai import OpenAI

client = OpenAI(api_key="Your_API_KEY")
def upload_resume(request):

    if request.method == "POST":

        form = ResumeForm(request.POST, request.FILES)

        if form.is_valid():

            pdf = request.FILES['resume']

            role = form.cleaned_data['role']

            reader = PyPDF2.PdfReader(pdf)

            resume_text = ""

            for page in reader.pages:

                text = page.extract_text()

                if text:
                    resume_text += text

            prompt = f"""
            You are an AI Interview Coach.

            Based on this resume:

            {resume_text}

            Generate 20 a to z  professional interview questions use technology meantioned in resume
            for a {role} role it shudnt be generic give all project based also.
            """

            response = client.chat.completions.create(model="gpt-3.5-turbo",messages=[{"role":"user","content":prompt}])

            questions = response.choices[0].message.content

            return render(request, 'question.html', {
                'questions': questions
            })

    else:

        form = ResumeForm()

    return render(request, 'upload.html', {
        'form': form
    })