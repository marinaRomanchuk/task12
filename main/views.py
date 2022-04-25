from django.shortcuts import render
import json
from main.models import InputData
from main.forms import InputDataForm


def main(request):
    if request.method == "POST":
        form = InputDataForm(request.POST)
        if form.is_valid():
            input_form = form.cleaned_data["name"]
            data = json.dumps(input_form, ensure_ascii=False)
            InputData.objects.create(data=data)

            for count in range(1, len(request.POST) - 1):
                input_value = request.POST[f"name{str(count)}"]
                data = json.dumps(input_value, ensure_ascii=False)
                InputData.objects.create(data=data)
    form = InputDataForm()
    return render(request, "main.html", {"form": form})


def result(request):
    query = InputData.objects.all().values("id", "data")
    return render(request, "result.html", {"list_of_results": list(query)})
