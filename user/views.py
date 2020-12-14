from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm


# Create your views here.
def home(request):
    return render(request, "home.html")


# Create your views here.
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, "patient-list.html", {'patients': patients})


def patient_create(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('patient-list')
            except:
                pass
    else:
        form = PatientForm()
    return render(request, 'patient-create.html', {'form': form})


def patient_update(request, id):
    patient = Patient.objects.get(id=id)
    form = PatientForm(initial={'name': patient.name, 'last_name': patient.last_name, 'phone': patient.phone,
                                'address': patient.address})
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/patient-list')
            except Exception as e:
                pass
    return render(request, 'patient-update.html', {'form': form})


def patient_delete(request, id):
    patient = Patient.objects.get(id=id)
    try:
        patient.delete()
    except:
        pass
    return redirect('patient-list')
