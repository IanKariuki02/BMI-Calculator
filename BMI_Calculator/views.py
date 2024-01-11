from django.shortcuts import render


def bmi_calculator(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            gender = request.POST['gender']
            age = int(request.POST['age'])
            address = request.POST['address']
            hobbies = request.POST.getlist('hobbies')
            weight = float(request.POST['weight'])
            height = float(request.POST['height'])
            bmi = weight / ((height / 100) ** 2)
        except ValueError:
            return render(request, 'bmi_calculator.html', {'error': 'Invalid input'})
        return render(request, 'bmi_result.html',
                      {'name': name, 'gender': gender, 'age': age, 'address': address, 'hobbies': hobbies,
                       'weight': weight, 'height': height, 'bmi': bmi})
    else:
        return render(request, 'bmi_calculator.html')
