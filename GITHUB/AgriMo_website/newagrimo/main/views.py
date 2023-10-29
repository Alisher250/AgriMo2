from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Shapes, UserProfile, Sunradiation, Odor, Humidity, Raindrop, Temperature, Light, Moisture, Pressure, Shop, Specialists, Review, Table, Info, Statistics
from django.shortcuts import render
from django.conf import settings
import requests
import json
from django.db import transaction
from django.db.models import Q
import openai
from django.http import JsonResponse
import threading
import socket
import time
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

openai.api_key = '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'

@api_view(['POST'])
def update_graphsmin(request):
    if request.method == "POST":
        try:
            data = request.data

            for item in data:
                username = item['username']
                sensor = item['sensor']
                targetmin = item['targetmin']
                targetminper = item['targetminper']
                user1 = User.objects.get(username=username)
                print(item)
                if sensor == "Sunradiation":
                    matching_model = Sunradiation.objects.filter(user_id=user1.id, min=targetmin).first()
                elif sensor == "Humidity":
                    matching_model = Humidity.objects.filter(user_id=user1.id, min=targetmin).first()
                elif sensor == "Odor":
                    matching_model = Odor.objects.filter(user_id=user1.id, min=targetmin).first()
                elif sensor == "Raindrop":
                    matching_model = Raindrop.objects.filter(user_id=user1.id, min=targetmin).first()
                elif sensor == "Temperature":
                    matching_model = Temperature.objects.filter(user_id=user1.id, min=targetmin).first()
                elif sensor == "Light":
                    matching_model = Light.objects.filter(user_id=user1.id, min=targetmin).first()
                elif sensor == "Moisture":
                    matching_model = Moisture.objects.filter(user_id=user1.id, min=targetmin).first()
                elif sensor == "Pressure":
                    matching_model = Pressure.objects.filter(user_id=user1.id, min=targetmin).first()

                if matching_model:
                    matching_model.minper = targetminper
                    matching_model.save()
                    print("Model is saved")
            return Response({'message': 'Data successfully processed'})

        except json.JSONDecodeError as e:
            return Response({'error': 'Invalid JSON format'}, status=400)

        except Exception as e:
            return Response({'error': str(e)}, status=500)

    return Response({'error': 'Method not allowed'}, status=405)

def stats(request):
    tableinfo = Table.objects.all()
    sec1 = Statistics.objects.filter(name=1)
    s1 = sec1.first().value
    sec2 = Statistics.objects.filter(name=2)
    s2 = sec2.first().value
    sec3 = Statistics.objects.filter(name=3)
    s3 = sec3.first().value
    sec4 = Statistics.objects.filter(name=4)
    s4 = sec4.first().value
    sec5 = Statistics.objects.filter(name=5)
    s5 = sec5.first().value
    sec6 = Statistics.objects.filter(name=6)
    s6 = sec6.first().value
    sec7 = Statistics.objects.filter(name=7)
    s7 = sec7.first().value
    sec8 = Statistics.objects.filter(name=8)
    s8 = sec8.first().value
    sec9 = Statistics.objects.filter(name=9)
    s9 = sec9.first().value
    sec10 = Statistics.objects.filter(name=10)
    s10 = sec10.first().value
    sec11 = Statistics.objects.filter(name=11)
    s11 = sec11.first().value
    sec12 = Statistics.objects.filter(name=12)
    s12 = sec12.first().value

    my_list = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12]
    ss1 = ''
    ss2 = ''
    ss3 = ''
    ss4 = ''
    ss5 = ''
    ss6 = ''
    ss7 = ''
    ss8 = ''
    ss9 = ''
    ss10 = ''
    ss11 = ''
    ss12 = ''

    if int(s1) > 0:
        ss1 = 'Tomato spider mites, also known as two-spotted spider mites, are small arachnids that can cause significant damage to tomato plants. They typically feed on the underside of leaves, sucking out the plants fluids and causing a speckled appearance on the leaves. Severe infestations can cause the leaves to turn yellow and fall off, which can reduce yields. Spider mites are more common in hot, dry weather and can reproduce rapidly, making management of this disease challenging.'
    if int(s2) > 0:
        ss2 = 'Tomato leaf mold is a fungal disease that thrives in high humidity environments. It typically appears as yellowing leaves with brown spots and a fuzzy growth on the underside of the leaves. Infected leaves may eventually fall off the plant, and severe infestations can reduce yields. This disease can be challenging to manage, but cultural practices such as adequate air circulation and moisture control can help prevent its spread.'
    if int(s3) > 0:
        ss3 = 'Tomato blight is a fungal disease that can cause significant damage to tomato plants. It typically appears as dark spots on the leaves and stems, which can eventually lead to the entire plant turning brown and withering away. This disease can be caused by various types of fungi, and management strategies may vary depending on the specific type. Cultural practices such as crop rotation and avoiding overhead watering can help prevent the spread of this disease.'
    if int(s4) > 0:
        ss4 = 'Strawberry powdery mildew is a fungal disease that can cause significant damage to strawberry plants. It typically appears as a white powdery coating on the leaves, stems, and flowers of the plant. As the disease progresses, the leaves may curl, turn yellow, and fall off. Severe infestations can reduce yields and affect the quality of the fruit. This disease is more common in humid conditions and can be managed through cultural practices such as pruning, removing infected plant material, and avoiding overhead watering.'
    if int(s5) > 0:
        ss5 = 'Beans angular leaf spot is a bacterial disease that can affect various types of beans, including snap beans, lima beans, and kidney beans. It typically appears as water-soaked lesions on the leaves, which can eventually turn brown and necrotic. The lesions often have a yellow halo around them, giving them a distinctive angular appearance. Severe infestations can cause defoliation, reduced yields, and reduced quality of the beans. This disease can be managed through cultural practices such as crop rotation, avoiding overhead watering, and using disease-free seeds.'
    if int(s6) > 0:
        ss6 = 'Beans rust is a fungal disease that can affect various types of beans, including snap beans, lima beans, and kidney beans. It typically appears as rusty brown spots on the leaves, which can eventually cause them to wither and fall off. The disease can also affect the pods, causing them to become discolored and deformed. Severe infestations can lead to significant yield losses. This disease is more common in humid conditions and can be managed through cultural practices such as crop rotation, avoiding overhead watering, and using disease-free seeds.'
    if int(s7) > 0:
        ss7 = 'Strawberry angular leaf spot is a bacterial disease that can cause significant damage to strawberry plants. It typically appears as water-soaked lesions on the leaves, which can eventually turn brown and necrotic. The lesions often have a distinctive angular appearance and can be accompanied by yellow halos. The disease can also affect the fruit, causing it to become discolored and deformed. This disease can be managed through cultural practices such as removing infected plant material and using disease-resistant varieties.'
    if int(s8) > 0:
        ss8 = 'Strawberry anthracnose fruit rot is a fungal disease that can cause significant damage to strawberry plants. It typically appears as small, water-soaked lesions on the fruit, which can eventually turn brown and sunken. The disease can also affect the leaves and stems of the plant, causing them to become discolored and necrotic. Severe infestations can lead to significant yield losses. This disease is more common in humid conditions and can be managed through cultural practices such as crop rotation, removing infected plant material, and using fungicides.'
    if int(s9) > 0:
        ss9 = 'Strawberry blossom blight is a fungal disease that can cause significant damage to strawberry plants. It typically affects the flowers of the plant, causing them to become discolored and necrotic. Infected flowers may fail to produce fruit or may produce small, deformed fruit. The disease can also affect the leaves and stems of the plant. This disease can be managed through cultural practices such as removing infected plant material, using fungicides, and improving air circulation to reduce humidity.'
    if int(s10) > 0:
        ss10 = 'Strawberry gray mold is a fungal disease that can cause significant damage to strawberry plants. It typically appears as grayish-brown fuzzy growth on the fruit, leaves, and flowers of the plant. Infected fruit may become soft and watery, while infected flowers may fail to produce fruit. The disease can spread rapidly in humid conditions and can cause significant yield losses. This disease can be managed through cultural practices such as removing infected plant material, using fungicides, and improving air circulation to reduce humidity.'
    if int(s11) > 0:
        ss11 = 'Strawberry leaf spot is a fungal disease that can cause significant damage to strawberry plants. It typically appears as small, dark spots on the leaves, which can eventually merge and cause the leaves to become necrotic. The disease can also affect the fruit and stems of the plant. Severe infestations can cause defoliation, reduced yields, and reduced quality of the fruit. This disease can be managed through cultural practices such as removing infected plant material, using fungicides, and improving air circulation to reduce humidity.'
    if int(s12) > 0:
        ss12 = 'Strawberry powdery mildew fruit is a fungal disease that can cause significant damage to strawberry plants. It typically appears as a white powdery coating on the fruit, which can eventually cause it to become discolored and deformed. The disease can also affect the leaves and stems of the plant. Severe infestations can cause significant yield losses. This disease is more common in dry conditions and can be managed through cultural practices such as pruning, removing infected plant material, and avoiding overhead watering.'


    return render(request, 'main/stats.html', {'tableinfo': tableinfo, 's1':s1, 's2':s2, 's3':s3, 's4':s4, 's5':s5, 's6':s6, 's7':s7, 's8':s8, 's9':s9, 's10':s10, 's11':s11, 's12':s12, 'ss1':ss1, 'ss2':ss2, 'ss3':ss3, 'ss4':ss4, 'ss5':ss5, 'ss6':ss6, 'ss7':ss7, 'ss8':ss8, 'ss9':ss9, 'ss10':ss10, 'ss11':ss11, 'ss12':ss12})


def update_min_values(model, targetminper, targetmin, user):
    matching_model = model.objects.filter(user_id=user.id, min=targetmin).first()
    if matching_model:
        matching_model.minper = targetminper
        matching_model.save()
        return True

class SensorDataRetriever:
    def __init__(self):
        pass

    def start(self, user):
        print("Started")
        update_min_values(Sunradiation, 477, 42, user)

def startif(request):
    retriever = SensorDataRetriever()
    retrieving_thread = threading.Thread(target=retriever.start, args=(request.user,))
    retrieving_thread.daemon = True
    retrieving_thread.start()
    return redirect('profile')


def endif(request):
    return redirect('geolocation')


@transaction.atomic
def index(request):
    context = {}
    return render(request, 'main/index.html', context)


@login_required()
def graphs(request, param):
    sunradiation_values = Sunradiation.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
        f"{param}").values_list(
        f'{param}per', flat=True)
    sunradiation_data = list(sunradiation_values)

    odor_values = Odor.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
        f"{param}").values_list(f'{param}per',
                                flat=True)
    odor_data = list(odor_values)

    humidity_values = Humidity.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
        f"{param}").values_list(
        f'{param}per', flat=True)
    humidity_data = list(humidity_values)

    raindrop_values = Raindrop.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
        f"{param}").values_list(
        f'{param}per', flat=True)
    raindrop_data = list(raindrop_values)

    temperature_values = Temperature.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
        f"{param}").values_list(
        f'{param}per', flat=True)
    temperature_data = list(temperature_values)

    light_values = Light.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
        f"{param}").values_list(f'{param}per',
                                flat=True)
    light_data = list(light_values)

    moisture_values = Moisture.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
        f"{param}").values_list(
        f'{param}per', flat=True)
    moisture_data = list(moisture_values)

    pressure_values = Pressure.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
        f"{param}").values_list(
        f'{param}per', flat=True)
    pressure_data = list(pressure_values)

    context = {'humidity_data': humidity_data,
               'sunradiation_data': sunradiation_data,
               'odor_data': odor_data,
               'raindrop_data': raindrop_data,
               'temperature_data': temperature_data,
               'light_data': light_data,
               'moisture_data': moisture_data,
               'pressure_data': pressure_data,
               'interval': param,
               }

    print(temperature_data)
    print(humidity_data)
    print(sunradiation_data)

    return render(request, 'main/graphs.html', context)


@login_required()
def graphspredict(request, param):
    sunradiation_values = Sunradiation.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
        f"{param}").values_list(
        f'{param}per', flat=True)
    sunradiation_data = list(sunradiation_values)

    odor_values = Odor.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
        f"{param}").values_list(f'{param}per',
                                flat=True)
    odor_data = list(odor_values)

    humidity_values = Humidity.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
        f"{param}").values_list(
        f'{param}per', flat=True)
    humidity_data = list(humidity_values)

    raindrop_values = Raindrop.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
        f"{param}").values_list(
        f'{param}per', flat=True)
    raindrop_data = list(raindrop_values)

    temperature_values = Temperature.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
        f"{param}").values_list(
        f'{param}per', flat=True)
    temperature_data = list(temperature_values)

    light_values = Light.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
        f"{param}").values_list(f'{param}per',
                                flat=True)
    light_data = list(light_values)

    moisture_values = Moisture.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
        f"{param}").values_list(
        f'{param}per', flat=True)
    moisture_data = list(moisture_values)

    pressure_values = Pressure.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
        f"{param}").values_list(
        f'{param}per', flat=True)
    pressure_data = list(pressure_values)

    context = {'humidity_data': humidity_data,
               'sunradiation_data': sunradiation_data,
               'odor_data': odor_data,
               'raindrop_data': raindrop_data,
               'temperature_data': temperature_data,
               'light_data': light_data,
               'moisture_data': moisture_data,
               'pressure_data': pressure_data,
               'interval': param,
               }

    print(temperature_data)
    print(humidity_data)
    print(sunradiation_data)
    # sunradiation_values = Sunradiation.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
    #     f"{param}").values_list(
    #     f'{param}per', flat=True)
    # sunradiation_data = list(sunradiation_values)
    #
    # odor_values = Odor.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
    #     f"{param}").values_list(f'{param}per',
    #                             flat=True)
    # odor_data = list(odor_values)
    #
    # humidity_values = Humidity.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
    #     f"{param}").values_list(
    #     f'{param}per', flat=True)
    # humidity_data = list(humidity_values)
    #
    # raindrop_values = Raindrop.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
    #     f"{param}").values_list(
    #     f'{param}per', flat=True)
    # raindrop_data = list(raindrop_values)
    #
    # temperature_values = Temperature.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
    #     f"{param}").values_list(
    #     f'{param}per', flat=True)
    # temperature_data = list(temperature_values)
    #
    # light_values = Light.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
    #     f"{param}").values_list(f'{param}per',
    #                             flat=True)
    # light_data = list(light_values)
    #
    # moisture_values = Moisture.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
    #     f"{param}").values_list(
    #     f'{param}per', flat=True)
    # moisture_data = list(moisture_values)
    #
    # pressure_values = Pressure.objects.filter(user=request.user, **{f"{param}per__isnull": False}).order_by(
    #     f"{param}").values_list(
    #     f'{param}per', flat=True)
    # pressure_data = list(pressure_values)
    #
    # superlist = [humidity_data, sunradiation_data, odor_data, raindrop_data, temperature_data, light_data,
    #              moisture_data, pressure_data]
    # for i in superlist:
    #     input_sequence = str(i)
    #     response = openai.Completion.create(
    #         engine="text-davinci-003",
    #         prompt=input_sequence + "\nHere is my array with values. Your task is to predict next values(if all are 0, then just return the same list) and give me array with the same length, but with predicted values.",
    #         max_tokens=120,
    #         n=1,
    #         stop=None,
    #         temperature=0.7
    #     )
    #
    #     predicted_sequence = response.choices[0].text
    #     list_sequence = eval(predicted_sequence)
    #     i = list_sequence
    #
    # context = {'humidity_data': humidity_data,
    #            'sunradiation_data': sunradiation_data,
    #            'odor_data': odor_data,
    #            'raindrop_data': raindrop_data,
    #            'temperature_data': temperature_data,
    #            'light_data': light_data,
    #            'moisture_data': moisture_data,
    #            'pressure_data': pressure_data,
    #            'interval': param,
    #            }
    #
    # print(light_data)
    # print(humidity_data)
    # print(sunradiation_data)

    return render(request, 'main/graphspredict.html', context)


def graphsai(request):
    print(request.user)
    context = {}
    return render(request, 'main/graphsai.html', context)


def profile(request):
    context = {}
    return render(request, 'main/profile.html', context)


def add_shape(request):
    if request.method == "POST":
        userprofile = UserProfile.objects.get(user=request.user)
        drawn_shapes = request.POST.getlist('drawn_shapes[]')
        print(drawn_shapes)
        for shape in drawn_shapes:
            shape_obj = Shapes.objects.create(user=request.user, shape=shape)
            userprofile.shapes.add(shape_obj)
        return redirect('geolocation')


def geolocation(request):
    userprofile = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        lat = request.POST['lat']
        long = request.POST['long']
        userprofile.geolocation1 = str(lat)
        userprofile.geolocation2 = str(long)
        userprofile.save()

    else:
        if userprofile.geolocation1:
            lat = float(userprofile.geolocation1)
            long = float(userprofile.geolocation2)
        else:
            return render(request, 'main/geolocation.html')

    shapes = userprofile.shapes.all()
    drawn_shapes = [shape.shape for shape in shapes]
    print(drawn_shapes)
    context = {'lat': lat, 'long': long, 'drawn_shapes': drawn_shapes}
    return render(request, 'main/geolocation.html', context)


def shop(request):
    goods = Shop.objects.all()
    context = {'goods': goods}
    return render(request, 'main/shop.html', context)


def specialists(request):
    experience = request.GET.getlist('experience')
    city = request.GET.getlist('city')
    specialization = request.GET.getlist('profession')

    conditions = Q()
    if experience:
        if 'no' in experience:
            conditions |= Q(experience__gte=0)
        if '1-3' in experience:
            conditions |= Q(experience__range=(1, 3))
        if '3-6' in experience:
            conditions |= Q(experience__range=(3, 6))
        if '6-9' in experience:
            conditions |= Q(experience__range=(6, 9))
        if '10+' in experience:
            conditions |= Q(experience__gte=10)

    if city:
        if 'all' not in city:
            conditions &= Q(city__in=city)  # Filter by selected cities

    if specialization:
        if 'all' not in specialization:
            conditions &= Q(specialization__in=specialization)  # Filter by selected specializations

    filtered_specialists = Specialists.objects.filter(conditions)

    context = {'specialists': filtered_specialists}
    return render(request, 'main/specialists.html', context)


def education(request):
    context = {}
    return render(request, 'main/education.html', context)


def events(request):
    context = {}
    return render(request, 'main/events.html', context)


def profileo(request):
    userprofile = UserProfile.objects.get(user=request.user)
    context = {'userprofile': userprofile}
    return render(request, 'main/profile-owner.html', context)


def change(request):
    if request.method == "POST":
        userprofile = UserProfile.objects.get(user=request.user)
        userprofile.city = request.POST['city']
        userprofile.region = request.POST['region']
        userprofile.farm = request.POST['farm']

    return redirect('profileo')


def loginsystem(request):
    if request.method == "GET":
        return render(request, 'main/loginsystem.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'main/loginsystem.html',
                          {'form': AuthenticationForm, 'error': 'Неверный логин и/или пароль'})


def signupsystem(request):
    if request.method == "GET":
        return render(request, 'main/signupsystem.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] != request.POST['password2']:
            return render(request, 'main/signupsystem.html',
                          {'form': UserCreationForm, 'error': 'Passwords don\'t match!'})
        else:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'],
                                                first_name=request.POST['name'],
                                                last_name=request.POST['lastname']
                                                )
                user.save()
                login(request, user)

                profession = request.POST['profession']
                if profession == "Владелец Фермы":
                    user_profile = UserProfile.objects.create(user=request.user)
                    phone = int(request.POST['phone'])
                    profession = request.POST['profession']
                    user_profile.telephone = phone
                    user_profile.profession = profession
                    user_profile.save()

                    val10 = [Humidity, Raindrop, Moisture]
                    val7 = [Temperature, Light, Pressure, Odor]
                    val30 = [Sunradiation, ]

                    val7_data = [
                        {'min': i, 'minper': 0} for i in range(0, 61, 2)
                    ]
                    val7_data1 = [
                        {'day': i, 'dayper': 0} for i in range(0, 25)
                    ]
                    val7_data2 = [
                        {'week': i, 'weekper': 0} for i in range(0, 8)
                    ]
                    val7_data3 = [
                        {'month': i, 'monthper': 0} for i in range(0, 31)
                    ]
                    val7_data4 = [
                        {'year': i, 'yearper': 0} for i in range(0, 13)
                    ]

                    val10_data = [
                        {'min': 0, 'minper': 0},
                        {'min': 6, 'minper': 0},
                        {'min': 12, 'minper': 0},
                        {'min': 18, 'minper': 0},
                        {'min': 24, 'minper': 0},
                        {'min': 30, 'minper': 0},
                        {'min': 36, 'minper': 0},
                        {'min': 42, 'minper': 0},
                        {'min': 48, 'minper': 0},
                        {'min': 54, 'minper': 0},
                        {'min': 60, 'minper': 0}
                    ]

                    val10_data1 = [
                        {'day': 0, 'dayper': 0},
                        {'day': 2, 'dayper': 0},
                        {'day': 4, 'dayper': 0},
                        {'day': 6, 'dayper': 0},
                        {'day': 8, 'dayper': 0},
                        {'day': 10, 'dayper': 0},
                        {'day': 12, 'dayper': 0},
                        {'day': 14, 'dayper': 0},
                        {'day': 16, 'dayper': 0},
                        {'day': 18, 'dayper': 0},
                        {'day': 20, 'dayper': 0},
                        {'day': 22, 'dayper': 0},
                        {'day': 24, 'dayper': 0}
                    ]

                    val10_data2 = [
                        {'week': 0, 'weekper': 0},
                        {'week': 1, 'weekper': 0},
                        {'week': 2, 'weekper': 0},
                        {'week': 3, 'weekper': 0},
                        {'week': 4, 'weekper': 0},
                        {'week': 5, 'weekper': 0},
                        {'week': 6, 'weekper': 0},
                        {'week': 7, 'weekper': 0}
                    ]

                    val10_data3 = [
                        {'month': 0, 'monthper': 0},
                        {'month': 3, 'monthper': 0},
                        {'month': 6, 'monthper': 0},
                        {'month': 9, 'monthper': 0},
                        {'month': 12, 'monthper': 0},
                        {'month': 15, 'monthper': 0},
                        {'month': 18, 'monthper': 0},
                        {'month': 21, 'monthper': 0},
                        {'month': 24, 'monthper': 0},
                        {'month': 27, 'monthper': 0},
                        {'month': 30, 'monthper': 0},
                    ]

                    val10_data4 = [
                        {'year': 0, 'yearper': 0},
                        {'year': 1, 'yearper': 0},
                        {'year': 2, 'yearper': 0},
                        {'year': 3, 'yearper': 0},
                        {'year': 4, 'yearper': 0},
                        {'year': 5, 'yearper': 0},
                        {'year': 6, 'yearper': 0},
                        {'year': 7, 'yearper': 0},
                        {'year': 8, 'yearper': 0},
                        {'year': 9, 'yearper': 0},
                        {'year': 10, 'yearper': 0},
                        {'year': 11, 'yearper': 0},
                        {'year': 12, 'yearper': 0},
                    ]

                    odors_data = [
                        {'min': 0, 'minper': 0},
                        {'min': 10, 'minper': 0},
                        {'min': 20, 'minper': 0},
                        {'min': 30, 'minper': 0},
                        {'min': 40, 'minper': 0},
                        {'min': 50, 'minper': 0},
                        {'min': 60, 'minper': 0}
                    ]

                    odors_data1 = [
                        {'day': 0, 'dayper': 0},
                        {'day': 4, 'dayper': 0},
                        {'day': 8, 'dayper': 0},
                        {'day': 12, 'dayper': 0},
                        {'day': 16, 'dayper': 0},
                        {'day': 20, 'dayper': 0},
                        {'day': 24, 'dayper': 0}
                    ]

                    odors_data2 = [
                        {'week': 0, 'weekper': 0},
                        {'week': 1, 'weekper': 0},
                        {'week': 2, 'weekper': 0},
                        {'week': 3, 'weekper': 0},
                        {'week': 4, 'weekper': 0},
                        {'week': 5, 'weekper': 0},
                        {'week': 6, 'weekper': 0},
                        {'week': 7, 'weekper': 0}
                    ]

                    odors_data3 = [
                        {'month': 0, 'monthper': 0},
                        {'month': 5, 'monthper': 0},
                        {'month': 10, 'monthper': 0},
                        {'month': 15, 'monthper': 0},
                        {'month': 20, 'monthper': 0},
                        {'month': 25, 'monthper': 0},
                        {'month': 30, 'monthper': 0},
                    ]

                    odors_data4 = [
                        {'year': 0, 'yearper': 0},
                        {'year': 2, 'yearper': 0},
                        {'year': 4, 'yearper': 0},
                        {'year': 6, 'yearper': 0},
                        {'year': 8, 'yearper': 0},
                        {'year': 10, 'yearper': 0},
                        {'year': 12, 'yearper': 0},
                    ]

                    for data in val7_data:
                        sunradiation = Sunradiation.objects.create(user=request.user, min=data['min'],
                                                                   minper=data['minper'])
                        user_profile.sunradiation.add(sunradiation)

                    for data in val7_data1:
                        sunradiation = Sunradiation.objects.create(user=request.user, day=data['day'],
                                                                   dayper=data['dayper'])
                        user_profile.sunradiation.add(sunradiation)

                    for data in val7_data2:
                        sunradiation = Sunradiation.objects.create(user=request.user, week=data['week'],
                                                                   weekper=data['weekper'])
                        user_profile.sunradiation.add(sunradiation)

                    for data in val7_data3:
                        sunradiation = Sunradiation.objects.create(user=request.user, month=data['month'],
                                                                   monthper=data['monthper'])
                        user_profile.sunradiation.add(sunradiation)

                    for data in val7_data4:
                        sunradiation = Sunradiation.objects.create(user=request.user, year=data['year'],
                                                                   yearper=data['yearper'])
                        user_profile.sunradiation.add(sunradiation)

                    for data in val10_data:
                        humidity = Humidity.objects.create(user=request.user, min=data['min'], minper=data['minper'])
                        raindrop = Raindrop.objects.create(user=request.user, min=data['min'], minper=data['minper'])
                        moisture = Moisture.objects.create(user=request.user, min=data['min'], minper=data['minper'])
                        user_profile.humidity.add(humidity)
                        user_profile.raindrop.add(raindrop)
                        user_profile.moisture.add(moisture)

                    for data in val10_data1:
                        humidity = Humidity.objects.create(user=request.user, day=data['day'], dayper=data['dayper'])
                        raindrop = Raindrop.objects.create(user=request.user, day=data['day'], dayper=data['dayper'])
                        moisture = Moisture.objects.create(user=request.user, day=data['day'], dayper=data['dayper'])
                        user_profile.humidity.add(humidity)
                        user_profile.raindrop.add(raindrop)
                        user_profile.moisture.add(moisture)

                    for data in val10_data2:
                        humidity = Humidity.objects.create(user=request.user, week=data['week'],
                                                           weekper=data['weekper'])
                        raindrop = Raindrop.objects.create(user=request.user, week=data['week'],
                                                           weekper=data['weekper'])
                        moisture = Moisture.objects.create(user=request.user, week=data['week'],
                                                           weekper=data['weekper'])
                        user_profile.humidity.add(humidity)
                        user_profile.raindrop.add(raindrop)
                        user_profile.moisture.add(moisture)

                    for data in val10_data3:
                        humidity = Humidity.objects.create(user=request.user, month=data['month'],
                                                           monthper=data['monthper'])
                        raindrop = Raindrop.objects.create(user=request.user, month=data['month'],
                                                           monthper=data['monthper'])
                        moisture = Moisture.objects.create(user=request.user, month=data['month'],
                                                           monthper=data['monthper'])
                        user_profile.humidity.add(humidity)
                        user_profile.raindrop.add(raindrop)
                        user_profile.moisture.add(moisture)

                    for data in val10_data4:
                        humidity = Humidity.objects.create(user=request.user, year=data['year'],
                                                           yearper=data['yearper'])
                        raindrop = Raindrop.objects.create(user=request.user, year=data['year'],
                                                           yearper=data['yearper'])
                        moisture = Moisture.objects.create(user=request.user, year=data['year'],
                                                           yearper=data['yearper'])
                        user_profile.humidity.add(humidity)
                        user_profile.raindrop.add(raindrop)
                        user_profile.moisture.add(moisture)

                    for odor_data in odors_data:
                        odor = Odor.objects.create(user=request.user, min=odor_data['min'], minper=odor_data['minper'])
                        temperature = Temperature.objects.create(user=request.user, min=odor_data['min'],
                                                                 minper=odor_data['minper'])
                        light = Light.objects.create(user=request.user, min=odor_data['min'],
                                                     minper=odor_data['minper'])
                        pressure = Pressure.objects.create(user=request.user, min=odor_data['min'],
                                                           minper=odor_data['minper'])
                        user_profile.odor.add(odor)
                        user_profile.temperature.add(temperature)
                        user_profile.light.add(light)
                        user_profile.pressure.add(pressure)

                    for odor_data in odors_data1:
                        odor = Odor.objects.create(user=request.user, day=odor_data['day'], dayper=odor_data['dayper'])
                        temperature = Temperature.objects.create(user=request.user, day=odor_data['day'],
                                                                 dayper=odor_data['dayper'])
                        light = Light.objects.create(user=request.user, day=odor_data['day'],
                                                     dayper=odor_data['dayper'])
                        pressure = Pressure.objects.create(user=request.user, day=odor_data['day'],
                                                           dayper=odor_data['dayper'])
                        user_profile.odor.add(odor)
                        user_profile.temperature.add(temperature)
                        user_profile.light.add(light)
                        user_profile.pressure.add(pressure)

                    for odor_data in odors_data2:
                        odor = Odor.objects.create(user=request.user, week=odor_data['week'],
                                                   weekper=odor_data['weekper'])
                        temperature = Temperature.objects.create(user=request.user, week=odor_data['week'],
                                                                 weekper=odor_data['weekper'])
                        light = Light.objects.create(user=request.user, week=odor_data['week'],
                                                     weekper=odor_data['weekper'])
                        pressure = Pressure.objects.create(user=request.user, week=odor_data['week'],
                                                           weekper=odor_data['weekper'])
                        user_profile.odor.add(odor)
                        user_profile.temperature.add(temperature)
                        user_profile.light.add(light)
                        user_profile.pressure.add(pressure)

                    for odor_data in odors_data3:
                        odor = Odor.objects.create(user=request.user, month=odor_data['month'],
                                                   monthper=odor_data['monthper'])
                        temperature = Temperature.objects.create(user=request.user, month=odor_data['month'],
                                                                 monthper=odor_data['monthper'])
                        light = Light.objects.create(user=request.user, month=odor_data['month'],
                                                     monthper=odor_data['monthper'])
                        pressure = Pressure.objects.create(user=request.user, month=odor_data['month'],
                                                           monthper=odor_data['monthper'])
                        user_profile.odor.add(odor)
                        user_profile.temperature.add(temperature)
                        user_profile.light.add(light)
                        user_profile.pressure.add(pressure)

                    for odor_data in odors_data4:
                        odor = Odor.objects.create(user=request.user, year=odor_data['year'],
                                                   yearper=odor_data['yearper'])
                        temperature = Temperature.objects.create(user=request.user, year=odor_data['year'],
                                                                 yearper=odor_data['yearper'])
                        light = Light.objects.create(user=request.user, year=odor_data['year'],
                                                     yearper=odor_data['yearper'])
                        pressure = Pressure.objects.create(user=request.user, year=odor_data['year'],
                                                           yearper=odor_data['yearper'])
                        user_profile.odor.add(odor)
                        user_profile.temperature.add(temperature)
                        user_profile.light.add(light)
                        user_profile.pressure.add(pressure)

                    user_profile.save()
                    return redirect('graphsai')
                else:
                    specialist = Specialists.objects.create(user=request.user)
                    specialist.fullname = str(request.POST['name']) + " " + str(request.POST['lastname'])
                    specialist.save()

                    return redirect('index')
            except IntegrityError:
                return render(request, 'main/signupsystem.html',
                              {'form': UserCreationForm, 'error': 'Username is already taken!'})


@login_required
def logoutsystem(request):
    if request.method == "GET":
        logout(request)
        return redirect('loginsystem')