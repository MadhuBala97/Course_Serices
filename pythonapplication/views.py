from django.shortcuts import render,redirect
from django.http import HttpResponse
from pythonapplication.models import Contact,Register,Feedback,Addservice,Addfeedback
from django.core.files.storage import FileSystemStorage
from django.conf.urls.static import static
def first(request):
    return HttpResponse("<h1>welcome to python project</h1>");
def home(request):
    return render(request,'template/home.html');
def about(request):
    return render(request,'template/about.html');
def services(request):
    return render(request,'template/services.html');
def contact(request):
    return render(request,'template/contact.html');
def contactcode(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		data=Contact(name=a,email=b,subject=c,message=d)
		data.save()
		msg="contact registered successfully"
		return render(request,'template/msg.html',{"msg":msg})
	else:
		return render(request,'template/contact.html')

def register(request):
    return render(request,'template/register.html');
def registercode(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		e=request.FILES['t5']
		data=Register(name=a,password=b,email=c,phoneno=d,image=e)
		data.save()
		msg="registerd successfully"
		return render(request,'template/msg.html',{"msg":msg})
	else:
		return render(request,'template/register.html')
def login(request):
    return render(request,'template/login.html');
def logincode(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		if a=="mb@gmail.com" and b=="madhu12345":
			request.session['admin']=a
			return redirect("/admin1/")
		else:
			user=Register.objects.filter(email=a,password=b).count()
			if(user==0):
				msg="Not match"
				return render(request,"template/msg.html",{"msg":msg})
			else:
				request.session['user']=a
				return redirect("/user1/")
	else:
		return redirect("/login/")
def admin1(request):
	if request.session.has_key('admin'):
		return render(request,'template/admin1.html')
	else:
		return redirect("/login/")
def user1(request):
	if request.session.has_key('user'):
		return render(request,'template/user1.html')
	else:
		return redirect("/login/")
def feedback(request):
    return render(request,'template/feedback.html');
def feedbackcode(request):
		if request.method=="POST":
			a=request.POST['t1']
			b=request.POST['t2']
			c=request.POST['t3']
			d=request.POST['t4']
			data=Feedback(name=a,email=b,phoneno=c,feedback=d)
			data.save()
			msg="Thank you for feedback"
			return render(request,"template/msg.html",{"msg":msg})
		else:
			return render(request,'template/feedback.html');
def showfeedback(request):
	data=Feedback.objects.all()
	return render(request,'template/showfeedback.html',{"alldata":data})
def showuser(request):
	data=Register.objects.all()
	return render(request,'template/showuser.html',{"alldata":data})
def addservice(request):
	return render(request,'template/addservice.html')
def addservicecode(request):
		if request.method=="POST":
			a=request.POST['t1']
			b=request.POST['t2']
			c=request.POST['t3']
			d=request.POST['t4']
			e=request.POST['t5']
			data=Addservice(stitle=a,sdescribe=b,sprice=c,sduration=d,mcharges=e)
			data.save()
			msg="Thank you for adding services"
			return render(request,"template/msg.html",{"msg":msg})
		else:
			return render(request,'template/addservice.html');
def showservices(request):
	data=Addservice.objects.all()
	return render(request,'template/showservices.html',{"alldata":data})
def addfeedback(request):
    return render(request,'template/addfeedback.html');
def addfeedbackcode(request):
		if request.method=="POST":
			a=request.POST['t1']
			b=request.POST['t2']
			c=request.POST['t3']
			d=request.POST['t4']
			data=Addfeedback(name=a,email=b,phoneno=c,feedback=d)
			data.save()
			msg="Thank you for your feedback"
			return render(request,"template/msg.html",{"msg":msg})
		else:
			return render(request,'template/addfeedback.html');
def showaddfeedback(request):
	data=Addfeedback.objects.all()
	return render(request,'template/showaddfeedback.html',{"alldata":data})
def logout(request):
	if request.session.has_key('user'):
		del request.session['user']
	if request.session.has_key('admin'):
		del request.session['admin']
	return redirect("/login/")
def delete_user(request,pk):
	id=pk
	Register.objects.filter(p_id=id).delete()
	return redirect("/showuser/")
def delete_feedback(request,pk):
	id=pk
	Feedback.objects.filter(p_id=id).delete()
	return redirect("/showfeedback/")
def delete_userfeedback(request,pk):
	id=pk
	Addfeedback.objects.filter(p_id=id).delete()
	return redirect("/showaddfeedback/")
def delete_services(request,pk):
	id=pk
	Addservice.objects.filter(p_id=id).delete()
	return redirect("/showaddservices/")
def showuserservices(request):
	data=Addservice.objects.all()
	return render(request,'template/showuserservices.html',{"alldata":data})
def updateuser(request,pk):
	id=pk
	data=Register.objects.filter(p_id=id).all()
	return render(request,'template/updateuser.html',{"alldata":data})
def updatefeedback(request,pk):
	id=pk
	data=Feedback.objects.filter(p_id=id).all()
	return render(request,'template/updatefeedback.html',{"alldata":data})
def updateservices(request,pk):
	id=pk
	data=Addservice.objects.filter(p_id=id).all()
	return render(request,'template/updateservices.html',{"alldata":data})
def savefeedback(request):
	if request.session.has_key('admin'):
		if request.method=="POST":
			a=request.POST['t1']
			b=request.POST['t2']
			c=request.POST['t3']
			d=request.POST['t4']
			id=request.POST['t5']
			Feedback.objects.filter(p_id=id).update(name=a,email=b,phoneno=c,feedback=d)
			return redirect('/showfeedback/')
		else:
			return redirect('/showfeedback/')
	else:
		return redirect('/login/')
def saveservices(request):
	if request.session.has_key('admin'):
		if request.method=="POST":
			a=request.POST['t1']
			b=request.POST['t2']
			c=request.POST['t3']
			d=request.POST['t4']
			e=request.POST['t5']
			Addservice.objects.filter(p_id=id).updte(stitle=a,sdescribe=b,sprice=c,sduration=d,mcharges=e)
			msg="Data Save"
			return render(request,"template/msg.html",{"msg":msg})
		else:
			return render(request,'template/addservice.html');
def saveuser(request):
	if request.session.has_key('admin'):
		if request.method=="POST":
			a=request.POST['t1']
			b=request.POST['t2']
			c=request.POST['t3']
			d=request.POST['t4']
			e=request.POST['t5'];
			id=request.POST['t6']
			Register.objects.filter(p_id=id).update(name=a,password=b,email=c,phoneno=d,image=e)
			return redirect('/showuser/')
		else:
			return redirect('/showuser/')
	else:
		return redirect('/login/')



# Create your views here.
