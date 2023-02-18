from .models import userProfile, eventType, eventName, userPerfData
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
import json
# import pyodbc

# Create your views here.

def index(request):
    return render(request, 'home.html')
    
def signup(request):
    if request.method == 'POST':
        usr = request.POST['usr']
        email = request.POST['email']
        pwd = request.POST['psw']
        pwd2 = request.POST['psw2']
        if pwd == pwd2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=usr).exists():
                messages.info(request, 'User Name Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=usr, email=email, password=pwd)
                user.save()

                #log user in and redirect to settings page
                user_login = auth.authenticate(username=usr, password=pwd)
                auth.login(request, user_login)

                #Create user profile also
                user_model = User.objects.get(username=usr)
                new_profile = userProfile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('profile')
        else:
            messages.info(request, 'Passwords not matching')
            return redirect('signup')

    else:
        return render(request, 'register.html')

def signin(request):
    if request.method == 'POST':
        usr = request.POST['usr']
        pwd = request.POST['pwd']

        user = auth.authenticate(username=usr, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('signin')
    else:
        return render(request, 'signin.html')

def signout(request):
    auth.logout(request)
    return redirect('home')

@login_required(login_url='signin')
def profile(request):
    user_profile = userProfile.objects.get(user=request.user)

    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        mname = request.POST['mname']
        dob = request.POST['dob']
        sex = request.POST['sex']
        ph = request.POST['ph']
        add = request.POST['add']
        dist = request.POST['dist']
        state = request.POST['state']
        pin = request.POST['pin']
        repState = request.POST['rstate']
        uid = request.POST['uid']

        user_profile.userFirstName = fname
        user_profile.userLastName = lname
        user_profile.userMiddleName = mname
        user_profile.userDOB = dob
        user_profile.userGender = sex
        user_profile.userPhone = ph
        user_profile.userAddress = add
        user_profile.userDistrict = dist
        user_profile.userState = state
        user_profile.userPinCode = pin
        user_profile.userRepState = repState
        user_profile.userAadhar = uid

        user_profile.save()

    return render(request, 'profile.html', {'user_profile': user_profile})

@login_required(login_url='signin')
def add_event(request):
    event_type_list = eventType.objects.all()
    events = eventName()

    if request.method == 'POST':
        event_tp = request.POST['event_tp']
        event_nm = request.POST['event_nm']
        event_desc = request.POST['event_desc']

        event_type_model = eventType.objects.get(id=event_tp)

        events.Typeid = event_type_model
        events.Name = event_nm
        events.Description = event_desc
        events.save()
        
    return render(request, 'listevent.html', {'event_list': event_type_list})

def usrdta(request):
    evetp = eventType.objects.all()
    event_list = eventName.objects.all()

    tmpJson = serializers.serialize("json",event_list)
    tmpObj = json.loads(tmpJson)
    eventjson = json.dumps(tmpObj)

    updModel = userPerfData()
    records_to_insert = []
    if request.method == 'POST':
        usr_id1 = User.objects.get(username=request.user.username)
        usr_id = request.user.id
        event_id = request.POST['event_nm']
        dte = request.POST['dte']

        lap1 = request.POST['ip1']
        lap2 = request.POST['ip2']
        lap3 = request.POST['ip3']
        lap4 = request.POST['ip4']
        lap5 = request.POST['ip5']
        lap6 = request.POST['ip6']
        lap7 = request.POST['ip7']
        lap8 = request.POST['ip8']
        lap9 = request.POST['ip9']
        lap10 = request.POST['ip10']
            
        total = lap1 + lap2 + lap3 + lap4 + lap5 + lap6 + lap7 + lap8 + lap9 + lap10

        lap_dict = {
            "lap1" : lap1,
            "lap2" : lap2,
            "lap3" : lap3,
            "lap4" : lap4,
            "lap5" : lap5,
            "lap6" : lap6,
            "lap7" : lap7,
            "lap8" : lap8,
            "lap9" : lap9,
            "lap10" : lap10,
            "total" : total
        }

        # tbl_name = "core_userperfdata"

        # query = """Insert into core_userperfdata ([user_id],[eventID_id],[fld_value])
        # values (?,?,?)"""

        # try:
        #     conn_string = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:appserverdemo.database.windows.net,1433;Database=techsource;Uid=testadmin;Pwd=@AdminTest;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
        #     print("Connection Successfull")
        #     conn = pyodbc.connect(conn_string)
        #     cursor = conn.cursor()
        #     cursor.executemany(query, records_to_insert)
        #     conn.commit()
        # except Exception as Ex:
        #     print("Error during connection attempt: "+str(Ex))
        #     raise


    return render(request, "userdata.html", {'event_list':eventjson, 'types':evetp})

def perdta(request):
    event_list = eventName.objects.all()
    return render(request, "personaldata.html", {'event_list':event_list})

def select_test(request):
    # evetp = eventType.objects.all()
    evenme = eventName.objects.all()

    type_id = request.GET.get('typeid', None)
    event = None

    if type_id:
        gettype = eventType.objects.get(id = type_id)
        event = eventName.objects.filter(Typeid = gettype)
    
    evetp = eventType.objects.all()

    if request.method == 'POST':
        var_tp = request.POST['event_tp']
        var_nm = request.POST['event_nm']

        print(var_tp, var_nm)

    return render(request, "02.html", {'ev_types':evetp, 'ev_names':event})