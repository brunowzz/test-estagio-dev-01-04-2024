from django.shortcuts import render
from .forms import ConsumoEnergiaForm

def calcular_economia(request):
    if request.method == 'POST':
        form = ConsumoEnergiaForm(request.POST)
        if form.is_valid():
            consumo_energia = form.save(commit=False)
            resultados = consumo_energia.calcular_economia()
            return render(request, 'calculator/resultado.html', {'resultados': resultados})
    else:
        form = ConsumoEnergiaForm()
    return render(request, 'calculator/formulario.html', {'form': form})
