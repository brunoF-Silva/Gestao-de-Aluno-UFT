from django.views.generic import TemplateView, TemplateView
from home.models import Aluno
from home.forms import FiltroForm

import json

class IndexTemplateView(TemplateView):
    model = Aluno
    template_name = 'home/Index.html'
    context_object_name = 'alunos'
    form_class = FiltroForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        alunosVinculados = Aluno.objects.filter(situacao='Vinculado')
        alunosFormados = Aluno.objects.filter(situacao='Formado')
        alunosJubilados = Aluno.objects.filter(situacao='Jubilado')
        alunosEvadidos = Aluno.objects.filter(situacao='Evadido')

        totalAlunos = Aluno.objects.all()
        totalAlunosCount = totalAlunos.count()
        amarela = Aluno.objects.filter(raca = 'Amarela').count()
        branca = Aluno.objects.filter(raca = 'Branca').count()
        indigena = Aluno.objects.filter(raca = 'Indigena').count()
        print('indigena',indigena)
        parda = Aluno.objects.filter(raca = 'Parda').count()
        preta = Aluno.objects.filter(raca = 'Preta').count()
        
        enem = Aluno.objects.filter(formaDeIngresso = 'ENEM').count()
        psc = Aluno.objects.filter(formaDeIngresso = 'PSC').count()
        vestibular = Aluno.objects.filter(formaDeIngresso = 'Vestibular').count()

        
        formaIngressoTotal = enem + psc + vestibular
        enemProp = int(100 * (enem / formaIngressoTotal))
        pscProp = int(100 * (psc / formaIngressoTotal))
        vestibularProp = int(100 * (vestibular / formaIngressoTotal))
        print('Oiiii',vestibularProp)
        
        anos = []
        for aluno in totalAlunos:
            ano = aluno.matricula[:5]
            if ano in anos:
                continue
            else:
                anos.append(ano)
                
        anos = sorted(anos)
        
        print(anos)
        
        anoQtd = {}
        for ano in anos:
            cont = 0
            for aluno in totalAlunos:
                
                if aluno.matricula[:5] == ano:
                    print('entrou')
                    cont+=1
                anoQtd[ano] = cont
        print(anoQtd)
        campos = list(anoQtd.keys())

        valores = list(anoQtd.values())
        print(campos,valores)
        
        context = {
            'totalAlunosCount': totalAlunosCount,
            'amarela': '{:.2f}'.format(100 *(amarela / totalAlunosCount)),
            'branca': '{:.2f}'.format(100 *(branca / totalAlunosCount)),
            'indigena': '{:.2f}'.format(100 *(indigena / totalAlunosCount)),
            'parda': '{:.2f}'.format(100 *(parda / totalAlunosCount)),
            'preta': '{:.2f}'.format(100 *(preta / totalAlunosCount)),
            'amarelaQtd': amarela,
            'brancaQtd': branca,
            'indigenaQtd': indigena,
            'pardaQtd': parda,
            'pretaQtd': preta,
            'totalAlunosVinculados': alunosVinculados.count(),
            'totalAlunosFormados': alunosFormados.count(),
            'totalAlunosJubilados': alunosJubilados.count(),
            'totalAlunosEvadidos': alunosEvadidos.count(),
            'enem': enem,
            'psc': psc,
            'vestibular': vestibular,
            'enemProp' : enemProp,
            'pscProp' : pscProp,
            'vestibularProp' : vestibularProp,
            'camposJson': json.dumps(campos),
            'valoresJson': json.dumps(valores),
        }

        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.form_class(self.request.POST or None)
        if form.is_valid():
            cursoSelecionado = form.cleaned_data['curso']
            campusSelecionado = form.cleaned_data['campus']
            if cursoSelecionado and campusSelecionado:
                queryset = Aluno.objects.filter(curso=cursoSelecionado, campus=campusSelecionado)
        return queryset

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)
