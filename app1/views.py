from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.models import Student

# Create your views here.
def calculations(values):
    total = 0
    for i in values:
        if i != '':
            total += int(i)
    return total

def organized(names, email, contact, address, cname, college, yop, marks, skill, hobbie, strength, fathername, gender, nationality, maritalstatus, languageknow, category, religion, dob, lang):
    datas = {}
    datas["name"] = names
    datas["email"] = email
    datas["contact"] = contact
    datas["address"] = address

    qualifications = []
    skills = []
    hobbies = []
    strengths = []
    language = []

    
    for i in range(len(cname)):
        data = {"id": i,"cname": cname[i], "college": college[i], "yearofpassing": yop[i], "marks": marks[i]}
        qualifications.append(data)

    for i in range(len(skill)):
        s = {"skill": skill[i]}
        skills.append(s)

    for i in range(len(hobbie)):
        h = {"hobbie": hobbie[i]}
        hobbies.append(h)

    for i in range(len(strength)):
        st = {"strength": strength[i]}
        strengths.append(st)

    for i in range(len(lang)):
        if i >= 1:
            lan = {"lang": "/"+lang[i]}
            language.append(lan)
        else:
            lan = {"lang": lang[i]}
            language.append(lan)

    
    
    datas["experience"] = ""
    datas["qualifications"] = qualifications
    datas["skills"] = skills
    datas["hobbies"] = hobbies
    datas["strengths"] = strengths
    datas["fathername"] = fathername
    datas["gender"] = gender
    datas["nationality"] = nationality
    datas["maritalstatus"] = maritalstatus
    # datas["languageknow"] = languageknow
    datas["category"] = category
    datas["religion"] = religion
    datas["dob"] = dob
    datas["lang"] = language

    
    return datas

def home(request):
    if request.method == "POST":
        names = request.POST.get('name')
        courses = request.POST.get('email')
        feeses = request.POST.get('contact')
        address = request.POST.get('address')

        #qualifications details
        cname = request.POST.getlist('cname')
        college = request.POST.getlist('college')
        yop = request.POST.getlist('yearofpassing')
        marks = request.POST.getlist('marks')

        #Profesional skills
        skills = request.POST.getlist('skills')
        hobbies = request.POST.getlist('hobbies')
        strength = request.POST.getlist('strength')

        #aditional personal details
        fathername = request.POST.get('fathername')
        gender = request.POST.get('gender')
        nationality = request.POST.get('nationality')
        maritalstatus = request.POST.get('maritalstatus')
        languageknow = request.POST.get('languageknow')
        category = request.POST.get('category')
        religion = request.POST.get('religion')
        dob = request.POST.get('dob')
        lang = request.POST.getlist('lang')

        print()

        datas = organized(names, courses, feeses, address, cname, college, yop, marks, skills, hobbies, strength, fathername, gender, nationality, maritalstatus, languageknow, category, religion, dob, lang)
        print("data : ", datas)
        return render(request, "temp1.html", {"datas": datas})
    return render(request, "index.html")

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            data = Student.objects.get(email=email)
            if data.email == email and data.password == password:
                return redirect('temp')
        except:
            print("data not found")
    return render(request, 'login.html')

def temp(request):
    return render(request, 'temp1.html')