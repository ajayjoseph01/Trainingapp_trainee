from django. contrib import messages
from unicodedata import name
from django.shortcuts import render
from django.shortcuts import render, redirect
from trainingapp.models import *
from datetime import datetime,date
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from io import BytesIO
from django.core.files import File
from django.conf import settings
import qrcode
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate
from datetime import datetime

# Create your views here.

def login(request):
    des = designation.objects.get(designation_name='manager')
    des1 = designation.objects.get(designation_name='trainer')
    des2 = designation.objects.get(designation_name='trainee')
    des3 = designation.objects.get(designation_name='accounts')

    if request.method == 'POST':
        
        email  = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
                request.session['SAdm_id'] = user.id
                return redirect( 'Admin_Dashboard')
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation_id=des.id).exists():
                member = user_registration.objects.get(
                email=request.POST['email'], password=request.POST['password'])
                request.session['m_designation_id'] = member.designation_id
                request.session['m_fullname'] = member.fullname
                request.session['m_id'] = member.id
                return render(request, 'dashsec.html', {'member': member})
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation_id=des1.id).exists():
                member = user_registration.objects.get(
                email=request.POST['email'], password=request.POST['password'])
                request.session['tr_designation_id'] = member.designation_id
                request.session['tr_fullname'] = member.fullname
                request.session['tr_team_id'] = member.team_id
                request.session['tr_id'] = member.id
                return render(request, 'tr_sec.html', {'member': member})
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation_id=des2.id).exists():
                member = user_registration.objects.get(
                email=request.POST['email'], password=request.POST['password'])
                request.session['te_designation_id'] = member.designation_id
                request.session['te_fullname'] = member.fullname
                request.session['te_id'] = member.id
                request.session['te_team_id'] = member.team_id
                return render(request, 'traineesec.html', {'member': member})
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation_id=des3.id).exists():
                member = user_registration.objects.get(
                email=request.POST['email'], password=request.POST['password'])
                request.session['acc_designation_id'] = member.designation_id
                request.session['acc_fullname'] = member.fullname
                request.session['acc_id'] = member.id
                return render(request, 'accountsec.html', {'member': member})
        else:
                context = {'msg': 'Invalid username or password'}
                return render(request, 'login.html', context)
    return render(request,'login.html')       



    
        # if request.method == 'POST':
        #     username = request.POST.get('email', None)
        #     password = request.POST.get('password', None)
        #     user = authenticate(email=username, password=password)
        #     if user:
        #         login(request, user)
        #         return redirect('Admin_Dashboard')
        #     else:
        #           context = {'msg': 'Invalid username or password'}
        #           return render(request, 'login.html',context)
        # if request.method == 'POST':
        #     email  = request.POST['email']
        #     password = request.POST['password']
        #     user = authenticate(email=email, password=password)
        #     if user is not None:
        #             request.session['SAdm_id'] = user.id
        #             return redirect('Admin_Dashboard')

        #     else:
        #         context = {'msg': 'Invalid username or password'}
        #         return render(request, 'login.html', context)
    

def manager_logout(request):
    if 'm_id' in request.session:  
        request.session.flush()
        return redirect('login')
    else:
        return redirect('login') 

def index(request):
    return render(request,'software_training/training/index.html')
    
def Trainings(request):
    return render(request,'software_training/training/training.html')

#******************Manager*****************************

def Manager_Dashboard(request):
    return render(request,'software_training/training/manager/manager_Dashboard.html')

def Manager_trainer(request):
    return render(request,'software_training/training/manager/manager_trainer.html')

def manager_team(request):
    return render(request,'software_training/training/manager/manager_team.html')

def manager_current_team(request):
    return render(request,'software_training/training/manager/manager_current_team.html')

def Manager_current_task(request):
    return render(request,'software_training/training/manager/manager_current_task.html')

def manager_current_assigned(request):
    return render(request,'software_training/training/manager/manager_current_assigned.html')

def manager_current_trainees(request):
    return render(request,'software_training/training/manager/manager_current_trainees.html')

def manager_current_empdetails(request):
    return render(request,'software_training/training/manager/manager_current_empdetails.html')

def manager_current_attendance(request):
    return render(request,'software_training/training/manager/manager_current_attendance.html')

def manager_current_attendance_list(request):
    return render(request,'software_training/training/manager/manager_current_attendance_list.html')

def manager_current_task_list(request):
    return render(request,'software_training/training/manager/manager_current_task_list.html')

def manager_current_task_details(request):
    return render(request,'software_training/training/manager/manager_current_task_details.html')
    
def manager_previous_team(request):
    return render(request,'software_training/training/manager/manager_previous_team.html')

def Manager_previous_task(request):
    return render(request,'software_training/training/manager/Manager_previous_task.html')

def manager_previous_assigned(request):
    return render(request,'software_training/training/manager/manager_previous_assigned.html')

def manager_previous_trainees(request):
    return render(request,'software_training/training/manager/manager_previous_trainees.html')

def manager_previous_empdetails(request):
    return render(request,'software_training/training/manager/manager_previous_empdetails.html')

def manager_previous_attendance(request):
    return render(request,'software_training/training/manager/manager_previous_attendance.html')

def manager_previous_attendance_list(request):
    return render(request,'software_training/training/manager/manager_previous_attendance_list.html')

def manager_previous_task_list(request):
    return render(request,'software_training/training/manager/manager_previous_task_list.html')

def manager_previous_task_details(request):
    return render(request,'software_training/training/manager/manager_previous_task_details.html')

def manager_trainee(request):
    return render(request,'software_training/training/manager/manager_trainee.html')

def Manager_trainees_details(request):
    return render(request,'software_training/training/manager/Manager_trainees_details.html')

def Manager_trainees_attendance(request):
    return render(request,'software_training/training/manager/Manager_trainees_attendance.html')

def Manager_reported_issues(request):
    return render(request,'software_training/training/manager/manager_reported_issues.html')

def manager_trainerreportissue(request):
    return render(request,'software_training/training/manager/manager_trainerreportissue.html')

def manager_trainer_unsolvedissue(request):
    return render(request,'software_training/training/manager/manager_trainer_unsolvedissue.html')

def manager_trainer_solvedissue(request):
    return render(request,'software_training/training/manager/manager_trainer_solvedissue.html')

def manager_traineereportissue(request):
    return render(request,'software_training/training/manager/manager_traineereportissue.html')

def manager_trainee_unsolvedissue(request):
    return render(request,'software_training/training/manager/manager_trainee_unsolvedissue.html')

def manager_trainee_solvedissue(request):
    return render(request,'software_training/training/manager/manager_trainee_solvedissue.html')

def manager_report_issue(request):
    return render(request,'software_training/training/manager/manager_report_issue.html')

def manager_reported_issue(request):
    return render(request,'software_training/training/manager/manager_reported_issue.html')

def manager_trainee_solvedissue(request):
    return render(request,'software_training/training/manager/manager_trainee_solvedissue.html')

def Manager_attendance(request):
    return render(request,'software_training/training/manager/manager_attendance.html') 

def manager_trainee_attendance(request):
    return render(request,'software_training/training/manager/manager_trainee_attendance.html') 

def manager_trainer_attendance(request):
    return render(request,'software_training/training/manager/manager_trainer_attendance.html') 

def manager_trainer_attendance_table(request):
    return render(request,'software_training/training/manager/manager_trainer_attendance_table.html') 

def manager_trainee_attendance_table(request):
    return render(request,'software_training/training/manager/manager_trainee_attendance_table.html') 

def manager_applyleave(request):
    return render(request,'software_training/training/manager/manager_applyleave.html') 

def manager_applyleavsub(request):
    return render(request,'software_training/training/manager/manager_applyleavsub.html')

def manager_requestedleave(request):
    return render(request,'software_training/training/manager/manager_requestedleave.html')

def manager_trainer_leave(request):
    return render(request,'software_training/training/manager/manager_trainer_leave.html')

def manager_trainers_leavelist(request):
    return render(request,'software_training/training/manager/manager_trainers_leavelist.html')

def manager_trainer_leavestatus(request):
    return render(request,'software_training/training/manager/manager_trainer_leavestatus.html')

def manager_trainee_leave(request):
    return render(request,'software_training/training/manager/manager_trainee_leave.html')

def manager_trainee_leavelist(request):
    return render(request,'software_training/training/manager/manager_trainee_leavelist.html')

def manager_trainee_leavestatus(request):
    return render(request,'software_training/training/manager/manager_trainee_leavestatus.html')

def manager_new_team(request):
    return render(request,'software_training/training/manager/manager_new_team.html')

def manager_new_teamcreate(request):
    return render(request,'software_training/training/manager/manager_new_teamcreate.html')

def manager_newtrainees(request):
    return render(request,'software_training/training/manager/manager_newtrainees.html')

    
#******************Trainer*****************************

def trainer_dashboard(request):
    return render(request,'software_training/training/trainer/trainer_dashboard.html')

def trainer_applyleave(request):
    return render(request, 'software_training/training/trainer/trainer_applyleave.html')

def trainer_applyleave_form(request):
    return render(request, 'software_training/training/trainer/trainer_applyleave_form.html')

def trainer_traineesleave_table(request):
    return render(request, 'software_training/training/trainer/trainer_traineesleave_table.html')

def trainer_reportissue(request):
    return render(request, 'software_training/training/trainer/trainer_reportissue.html')

def trainer_reportissue_form(request):
    return render(request, 'software_training/training/trainer/trainer_reportissue_form.html')

def trainer_reportedissue_table(request):
    return render(request, 'software_training/training/trainer/trainer_reportedissue_table.html')

def trainer_topic(request):
    return render(request,'software_training/training/trainer/trainer_topic.html')

def trainer_addtopic(request):
    return render(request,'software_training/training/trainer/trainer_addtopic.html')

def trainer_viewtopic(request):
    return render(request,'software_training/training/trainer/trainer_viewtopic.html')

def trainer_attendance(request):
    return render(request,'software_training/training/trainer/trainer_attendance.html')

def trainer_attendance_trainees(request):
    return render(request,'software_training/training/trainer/trainer_attendance_trainees.html')

def trainer_attendance_trainer(request):
    return render(request, 'software_training/training/trainer/trainer_attendance_trainer.html')

def trainer_attendance_trainer_viewattendance(request):
    return render(request,'software_training/training/trainer/trainer_attendance_trainer_viewattendance.html')

def trainer_attendance_trainer_viewattendancelist(request):
    return render(request,'software_training/training/trainer/trainer_attendance_trainer_viewattendancelist.html')

def trainer_team(request):
    return render(request,'software_training/training/trainer/trainer_team.html')

def trainer_currentteam(request):
    return render(request,'software_training/training/trainer/trainer_current_team_list.html')

def trainer_currenttrainees(request):
    return render(request, 'software_training/training/trainer/trainer_current_trainees_list.html')

def trainer_currenttraineesdetails(request):
    return render(request,'software_training/training/trainer/trainer_current_tainees_details.html')

def trainer_currentattentable(request):
    return render(request,'software_training/training/trainer/trainer_current_atten_table.html')

def trainer_currentperform(request):
    return render(request,'software_training/training/trainer/trainer_current_perform.html')

def trainer_currentattenadd(request):
    return render(request,'software_training/training/trainer/trainer_current_atten_add.html')

def trainer_previousteam(request):
    return render(request,'software_training/training/trainer/trainer_previous_team_list.html')

def trainer_previoustrainees(request):
    return render(request,'software_training/training/trainer/trainer_previous_trainess_list.html')

def trainer_previoustraineesdetails(request):
    return render(request, 'software_training/training/trainer/trainer_previous_trainees_details.html')

def trainer_previousattentable(request):
    return render(request,'software_training/training/trainer/trainer_previous_atten_table.html')

def trainer_previousperfomtable(request):
    return render(request,'software_training/training/trainer/trainer_previous_performtable.html')

def trainer_current_attendance(request):
    return render(request,'software_training/training/trainer/trainer_current_attendance.html')

def trainer_Task(request) :
    return render(request,'software_training/training/trainer/trainer_task.html')
    
def trainer_teamlistpage(request) :
    return render(request,'software_training/training/trainer/trainer_teamlist.html')
    
def trainer_taskpage(request) :
    return render(request, 'software_training/training/trainer/trainer_taskfor.html')
    
def trainer_givetask(request) :
    return render(request, 'software_training/training/trainer/trainer_givetask.html')
    
def trainer_taskgivenpage(request) :
    return render(request,'software_training/training/trainer/trainer_taskgiven.html')
    
def trainer_taska(request):
    return render(request, 'software_training/training/trainer/trainer_taska.html')

def trainer_task_completed_teamlist(request):
    return render(request, 'software_training/training/trainer/trainer_task_completed_teamlist.html')

def trainer_task_completed_team_tasklist(request):
    return render(request, 'software_training/training/trainer/trainer_task_completed_team_tasklist.html')

def trainer_task_previous_teamlist(request):
    return render(request, 'software_training/training/trainer/trainer_task_previous_teamlist.html')

def trainer_task_previous_team_tasklist(request):
    return render(request, 'software_training/training/trainer/trainer_task_previous_team_tasklist.html')

def trainer_trainees(request):
    return render(request, 'software_training/training/trainer/trainer_trainees.html')

def trainer_previous_trainees(request):
    return render(request,'software_training/training/trainer/trainer_previous_trainees.html')

def trainer_current_trainees(request):
    return render(request,'software_training/training/trainer/trainer_current_trainees.html')

def trainer_myreportissue_table(request):
    return render(request, 'software_training/training/trainer/trainer_myreportissue_table.html')

def trainer_current_attendance_view(request):
    return render(request,'software_training/training/trainer/trainer_current_attendance_view.html')

def trainer_attendance_trainees_viewattendance(request):
    return render(request,'software_training/training/trainer/trainer_attendance_trainees_viewattendance.html')

def trainer_attendance_trainees_viewattendancelist(request):
    return render(request,'software_training/training/trainer/trainer_attendance_trainees_viewattendancelist.html')

def trainer_attendance_trainees_addattendance(request):
    return render(request,'software_training/training/trainer/trainer_attendance_trainees_addattendance.html')
    
#******************  Trainee  *****************************

def trainee_dashboard_trainee(request):
    if 'te_id' in request.session: 
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        z = user_registration.objects.filter(id=te_id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=te_id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'software_training/training//trainee/trainee_dashboard_trainee.html',{'z': z ,'labels': labels,'data': data,})
    else:
        return redirect('/')
       
def trainee_task(request):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        else:
            te_id = "dummy"
        z=user_registration.objects.filter(id=te_id)
        return render(request,'software_training/training/trainee/trainee_task.html',{'z':z})   
    else:
        return redirect('/')

def trainee_task_list(request):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        else:
            te_id = "dummy"
        z=user_registration.objects.filter(id=te_id)
        mem=trainer_task.objects.filter(trainer_task_user=te_id,trainer_task_status = 0).all().order_by('-id')
        return render(request,'software_training/training/trainee/trainee_task_list.html',{'z':z,'mem':mem})
    else:
        return redirect('/')

def trainee_task_details(request,id):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        else:
            te_id = "dummy"
        z=user_registration.objects.filter(id=te_id)
        mem=trainer_task.objects.get(id=id)
        if request.method=="POST":
            mem.trainer_task_user_description=request.POST['description']
            mem.trainer_task_user_files=request.FILES['files']
            mem.trainer_task_submitteddate=datetime.now()
            mem.trainer_task_status=1
            mem.save()
            return redirect('trainee_task_list')
        return render(request,'software_training/training/trainee/trainee_task_details.html',{'z':z,'mem':mem})
    else:
        return redirect('/')

def trainee_completed_taskList(request):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        else:
            te_id = "dummy"
        z=user_registration.objects.filter(id=te_id)
        mem=trainer_task.objects.filter(trainer_task_user=te_id,trainer_task_status = 1).all().order_by('-id')
        return render(request,'software_training/training/trainee/trainee_completed_taskList.html',{'z':z,'mem':mem})
    else:
        return redirect('/')

def trainee_completed_details(request):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        else:
            te_id = "dummy"
        z=user_registration.objects.filter(id=te_id)
        return render(request,'software_training/training/trainee/trainee_completed_details.html',{'z':z})
    else:
        return redirect('/')

def trainee_topic(request):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        else:
            te_id = "dummy"
        z=user_registration.objects.filter(id=te_id)
        return render(request, 'software_training/training/trainee/trainee_topic.html',{'z':z})
    else:
        return redirect('/')

def trainee_currentTopic(request):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        if request.session.has_key('te_team_id'):
            te_team_id = request.session['te_team_id']         
        else:
            te_id = "dummy"
        z=user_registration.objects.filter(id=te_id)
        mem=topic.objects.filter(topic_trainee=te_id,topic_team=te_team_id,topic_status = 0).all().order_by('-id')
        return render(request, 'software_training/training/trainee/trainee_currentTopic.html',{'z':z,'mem':mem})
    else:
        return redirect('/')  

def save_trainee_review(request,id):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        if request.session.has_key('te_team_id'):
            te_team_id = request.session['te_team_id']         
        else:
            te_id = "dummy"
        z=user_registration.objects.filter(id=te_id)
        vars=topic.objects.get(id=id)
        vars.topic_review = request.POST.get('review')
        vars.topic_status = 1
        vars.save()
        return redirect('trainee_currentTopic')
    else:
        return redirect('/')  

def trainee_previousTopic(request):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        if request.session.has_key('te_team_id'):
            te_team_id = request.session['te_team_id']
        else:
            te_id = "dummy"
        z=user_registration.objects.filter(id=te_id)
        mem=topic.objects.filter(topic_trainee=te_id,topic_team=te_team_id,topic_status = 1).all().order_by('-id')
        return render(request, 'software_training/training/trainee/trainee_previousTopic.html',{'z':z,'mem':mem})
    else:
        return redirect('/')
def trainee_reported_issue(request):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        else:
            te_id = "dummy"
        z=user_registration.objects.filter(id=te_id)
        mem=reported_issue.objects.filter(reported_issue_reporter=te_id).all().order_by('-id')    
        return render(request, 'software_training/training/trainee/trainee_reported_issue.html',{'z':z,'mem':mem})
    else:
        return redirect('/')

def trainee_report_reported(request):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        if request.session.has_key('te_designation_id'):
            te_designation_id = request.session['te_designation_id']
        else:
            te_id = "dummy"
        z=user_registration.objects.filter(designation_id=te_designation_id).filter(id=te_id)
        var = reported_issue()
        if request.method == 'POST':
            var.reported_issue_designation_id=designation.objects.get(id=te_designation_id)
            var.reported_issue_reported_to  = user_registration.objects.get(id=int(request.POST['reportto']))
            var.reported_issue_issue = request.POST['report']
            var.reported_issue_reporter  = user_registration.objects.get(id=te_id)
            var.reported_issue_reported_date = datetime.now()
            var.reported_issue_issuestatus=0
            var.save()
        return render(request, 'software_training/training/trainee/trainee_report_reported.html',{'z':z})
    else:
        return redirect('/')

def trainee_report_issue(request):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        else:
            te_id = "dummy"
        z=user_registration.objects.filter(id=te_id)
        des = designation.objects.get(designation_name='manager')
        mem = user_registration.objects.filter(designation_id=des.id)
        des1 = designation.objects.get(designation_name='trainer')
        mem1= user_registration.objects.filter(designation_id=des1.id)
        return render(request, 'software_training/training/trainee/trainee_report_issue.html',{'z':z,'mem':mem,'mem1':mem1})
    else:
        return redirect('/')

def trainee_applyleave_form(request):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        else:
            te_id = "dummy"
        mem = user_registration.objects.all()
        des=designation.objects.get(designation_name="trainee")
        z=user_registration.objects.filter(designation_id=des.id)
        user=user_registration.objects.get(id=te_id)
        le=leave()
        if request.method=="POST":
            le.leave_from_date=request.POST['from']
            le.leave_to_date=request.POST['to']
            le.leave_reason=request.POST['reason']
            le.leave_leave_status =request.POST['haful']
            le.leave_leaveapproved_status=0
            le.leave_designation_id=des.id
            le.leave_user=user
            le.save()
            return redirect('trainee_applyleave_card')
        return render(request, 'software_training/training/trainee/trainee_applyleave_form.html',{'mem': mem,'z':z}) 
    else:
        return redirect('/')
    
def trainee_applyleave_card(request):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        else:
            te_id = "dummy"
        mem = user_registration.objects.all()
        des=designation.objects.get(designation_name="trainee")
        z=user_registration.objects.filter(designation_id=des.id)
        return render(request, 'software_training/training/trainee/trainee_applyleave_cards.html',{'mem':mem,'z':z})
    else:
        return redirect('/')
    
def trainee_appliedleave(request):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        else:
            te_id = "dummy"
        z=user_registration.objects.filter(id=te_id)
        des=designation.objects.get(designation_name="trainee")
        le=leave.objects.filter(leave_designation_id=des.id ,leave_user=te_id).all().order_by('-id')
        return render(request, 'software_training/training/trainee/trainee_appliedleave.html',{'z':z,'le':le})
    else:
        return redirect('/')

def Attendance(request):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        else:
            te_id = "dummy"
        z=user_registration.objects.filter(id=te_id)
        return render(request,'software_training/training/trainee/trainees_attendance.html',{'z':z})
    else:
        return redirect('/')

def trainees_attendance_viewattendance(request):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        else:
            te_id = "dummy"
        z=user_registration.objects.filter(id=te_id)
        return render(request,'software_training/training/trainee/trainees_attendance_viewattendance.html',{'z':z})
    else:
        return redirect('/')

def trainees_attendance_viewattendancelist(request):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        else:
            te_id = "dummy"
        z=user_registration.objects.filter(id=te_id)
        if request.method == 'POST':
            std = request.POST['startdate']
            edd = request.POST['enddate']
            user=te_id
            atten = attendance.objects.filter(attendance_date__gte=std,attendance_date__lte=edd,attendance_user_id=user)
        return render(request,'software_training/training/trainee/trainees_attendance_viewattendancelist.html',{'z':z,'atten':atten})
    else:
        return redirect('/')

def trainee_payment(request):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        else:
            te_id = "dummy"
        z=user_registration.objects.filter(id=te_id)
        return render(request,'software_training/training/trainee/trainee_payment.html',{'z':z})
    else:
        return redirect('/')
   
def trainee_payment_addpayment(request):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        else:
            te_id = "dummy"
        z=user_registration.objects.filter(id=te_id)
        pay=paymentlist()
        if request.method=="POST":
            pay.paymentlist_user_id = user_registration.objects.get(id=te_id)
            pay.paymentlist_amount_pay = request.POST['amount']
            pay.paymentlist_amount_date = request.POST['paymentdate']
            pay.paymentlist_current_date = datetime.now()
            pay.paymentlist_amount_downlod = request.FILES['files']
            pay.paymentlist_amount_status = 0 
            member = user_registration.objects.get(id=te_id)
            co = course.objects.get(id = member.course_id)
            member.total_pay=int(request.POST['amount'])+member.total_pay
            member.payment_balance = co.course_total_fee - member.total_pay
            member.save()
            pay.save()
            return redirect('trainee_payment')

        return render(request,'software_training/training/trainee/trainee_payment_addpayment.html',{'z':z})
    else:
        return redirect('/')
def trainee_payment_viewpayment(request):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        else:
            te_id = "dummy"
        z=user_registration.objects.filter(id=te_id)
        mem=paymentlist.objects.filter(paymentlist_user_id = te_id).order_by('-id')
        return render(request,'software_training/training/trainee/trainee_payment_viewpayment.html',{'z':z,'mem':mem})
    else:
        return redirect('/')

def trainee_logout(request):
    if 'te_id' in request.session:  
        request.session.flush()
        return redirect('login')
    else:
        return redirect('login') 

def trainees_account(request):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        else:
            te_id = "dummy"
        z=user_registration.objects.filter(id=te_id)
        return render(request,'software_training/training/trainee/trainees_account.html',{'z':z})
    else:
        return redirect('/')

def imagechange_trainees(request,id):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        else:
            te_id = "dummy"
        z=user_registration.objects.filter(id=te_id)     
        mem=user_registration.objects.get(id=id)
        if request.method=="POST":
            mem.photo = request.FILES['filenamees']
            mem.save()
            return redirect('trainees_account')
    else:
        return redirect('/')

def trainees_chpasswd(request):
    if 'te_id' in request.session:
        if request.session.has_key('te_id'):
            te_id = request.session['te_id']
        else:
            te_id = "dummy"
        z=user_registration.objects.filter(id=te_id)
        if request.method == 'POST':
            abc = user_registration.objects.get(id=te_id)   
            oldps = request.POST['currentPassword']
            newps = request.POST['newPassword']
            cmps = request.POST.get('confirmPassword')
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return redirect('trainee_dashboard_trainee')
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')                
            return render(request, 'software_training/training/trainee/trainees_chpasswd.html', {'z': z})   
        return render(request, 'software_training/training/trainee/trainees_chpasswd.html', {'z': z})
    else:
        return redirect('/')


#****************************  Admin- view  ********************************

def Admin_Dashboard(request):
    return render(request,'software_training/training/admin/admin_Dashboard.html')

def Admin_categories(request):
    return render(request,'software_training/training/admin/admin_categories.html') 

def Admin_emp_categories(request):
    return render(request,'software_training/training/admin/admin_emp_categories.html')  

def Admin_courses(request):
    return render(request,'software_training/training/admin/admin_courses.html')

def Admin_emp_course_list(request):
    return render(request,'software_training/training/admin/admin_emp_course_list.html')

def Admin_emp_course_details(request):
    return render(request,'software_training/training/admin/admin_emp_course_details.html')

def Admin_emp_profile(request):
    return render(request,'software_training/training/admin/admin_emp_profile.html')

def Admin_emp_attendance(request):
    return render(request,'software_training/training/admin/admin_emp_attendance.html')

def Admin_emp_attendance_show(request):
    return render(request,'software_training/training/admin/admin_emp_attendance_show.html')

def Admin_task(request):
    return render(request,'software_training/training/admin/admin_task.html')

def Admin_givetask(request):
    return render(request,'software_training/training/admin/admin_givetask.html')

def Admin_current_task(request):
    return render(request,'software_training/training/admin/admin_current_task.html')

def Admin_previous_task(request):
    return render(request,'software_training/training/admin/admin_previous_task.html')

def Admin_registration_details(request):
    return render(request,'software_training/training/admin/admin_registration_details.html')  

def Admin_attendance(request):
    return render(request,'software_training/training/admin/admin_attendance.html') 

def Admin_attendance_show(request):
    return render(request,'software_training/training/admin/admin_attendance_show.html')

def Admin_reported_issues(request):
    return render(request,'software_training/training/admin/admin_reported_issues.html') 

def Admin_emp_reported_detail(request):
    return render(request,'software_training/training/admin/admin_emp_reported_detail.html')

def Admin_emp_reported_issue_show(request):
    return render(request,'software_training/training/admin/admin_emp_reported_issue_show.html')

def Admin_manager_reported_detail(request):
    return render(request,'software_training/training/admin/admin_manager_reported_detail.html')

def Admin_manager_reported_issue_show(request):
    return render(request,'software_training/training/admin/admin_manager_reported_issue_show.html')

def Admin_add(request):
    return render(request,'software_training/training/admin/admin_add.html') 

def Admin_addcategories(request):
    return render(request,'software_training/training/admin/admin_addcategories.html') 

def Admin_categorieslist(request):
    return render(request,'software_training/training/admin/admin_categorieslist.html') 

def Admin_addcourse(request):
    return render(request,'software_training/training/admin/admin_addcourse.html') 

def Admin_addnewcourse(request):
    return render(request,'software_training/training/admin/admin_addnewcourse.html') 

def Admin_addnewcategories(request):
    return render(request,'software_training/training/admin/admin_addnewcategories.html') 

def Admin_courselist(request):
    return render(request,'software_training/training/admin/admin_courselist.html') 

def Admin_coursedetails(request):
    return render(request,'software_training/training/admin/admin_coursedetails.html') 

#******************accounts****************

def accounts_Dashboard(request):
    return render(request, 'software_training/training/account/accounts_Dashboard.html')

def accounts_registration_details(request):
    return render(request, 'software_training/training/account/accounts_registration_details.html')

def accounts_payment_details(request):
    return render(request, 'software_training/training/account/account_payment_details.html')

def accounts_payment_salary(request):
    return render(request, 'software_training/training/account/account_payment_salary.html')

def accounts_payment_view(request):
    return render(request, 'software_training/training/account/account_payment_view.html')

def accounts_report_issue(request):
    return render(request, 'software_training/training/account/account_report_issue.html')

def accounts_report(request):
    return render(request, 'software_training/training/account/account_report.html')

def accounts_reported_issue(request):
    return render(request, 'software_training/training/account/account_reported_issue.html')

def accounts_acntpay(request):
    return render(request, 'software_training/training/account/accounts_acntpay.html')

def accounts_employee(request):
    return render(request, 'software_training/training/account/accounts_employee.html')

def accounts_emp_dep(request):
    return render(request, 'software_training/training/account/accounts_emp_dep.html')

def accounts_emp_list(request):
    return render(request, 'software_training/training/account/accounts_emp_list.html')

def accounts_emp_details(request):
    return render(request, 'software_training/training/account/accounts_emp_details.html')

def accounts_add_bank_acnt(request):
    return render(request, 'software_training/training/account/accounts_add_bank_acnt.html')

def accounts_bank_acnt_details(request):
    return render(request, 'software_training/training/account/accounts_bank_acnt_details.html')

def accounts_salary_details(request):
    return render(request, 'software_training/training/account/accounts_salary_details.html')

def accounts_expenses(request):
    return render(request, 'software_training/training/account/accounts_expenses.html')

def accounts_expenses_viewEdit(request):
    return render(request, 'software_training/training/account/accounts_expenses_viewEdit.html')

def accounts_expenses_viewEdit_Update(request):
    return render(request, 'software_training/training/account/accounts_expenses_viewEdit.html')

def accounts_expense_newTransaction(request):
    return render(request, 'software_training/training/account/accounts_expense_newTransaction.html')

def accounts_paydetails(request):
    return render(request, 'software_training/training/account/accounts_paydetails.html')

def accounts_print(request):
    return render(request, 'software_training/training/account/accounts_print.html')

def accounts_payment(request):
    return render(request,'software_training/training/account/accounts_payment.html')

def accounts_payment_dep(request):
    return render(request, 'software_training/training/account/accounts_payment_dep.html')

def accounts_payment_list(request):
    return render(request, 'software_training/training/account/accounts_payment_list.html')

def accounts_payment_details(request):
    return render(request, 'software_training/training/account/accounts_payment_details.html')

def accounts_payment_detail_list(request):
    return render(request, 'software_training/training/account/accounts_payment_detail_list.html')

def accounts_payslip(request):
    return render(request, 'software_training/training/account/accounts_payslip.html')