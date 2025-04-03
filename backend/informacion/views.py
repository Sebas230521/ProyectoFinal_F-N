import pdfcrowd
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from fish_management.models import Estanque
from procedimientos.models import Procedimientos


class EstanquesPorUsuario(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        usuario = request.user
        estanques = Estanque.objects.filter(id_user=usuario).values('id', 'nombre_finca', 'numero_estanque')
        return Response(list(estanques))


class DetalleEstanqueView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        estanque = get_object_or_404(Estanque, pk=pk, id_user=request.user)
        procedimientos = Procedimientos.objects.filter(estanque=estanque.id)
        print(estanque.id)

        formato = request.query_params.get('formato', 'json').lower()

        if formato == 'pdf':
            context = {
                "estanque": estanque,
                "procedimientos": procedimientos,
            }
            html_string = render_to_string('informe_estanque.html', context)

            try:
                client = pdfcrowd.HtmlToPdfClient('fish_nexus0', '3b734213f73c4300e8ee9ecc2289de1c')
                pdf_content = client.convertString(html_string)
            except pdfcrowd.Error as error:
                return HttpResponse(f"Error al generar el PDF: {error}", status=500)

            response = HttpResponse(pdf_content, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="Informe_Estanque_{estanque.nombre_finca}_{estanque.numero_estanque}.pdf"'
            return response

        elif formato == 'html':
            context = {
                "estanque": estanque,
                "procedimientos": procedimientos,
            }
            html_string = render_to_string('informe_estanque.html', context)
            return HttpResponse(html_string, content_type='text/html')

        else:
            data = {
                "estanque": {
                    "id": estanque.id,
                    "nombre_finca": estanque.nombre_finca,
                    "numero_estanque": estanque.numero_estanque,
                    "tipo_estanque": estanque.tipo_estanque,
                    "profundidad": estanque.profundidad,
                    "ancho": estanque.ancho,
                    "largo": estanque.largo,
                    "especie_pez": estanque.especie_pez,
                    "cantidad": estanque.cantidad,
                    "numero_alimento": estanque.numero_alimento,
                    "fecha_siembra": str(estanque.fecha_siembra),
                },
                "procedimientos": [
                    {
                        "id": proc.id,
                        "nombreProcedimiento": proc.nombreProcedimiento,
                        "tipoConcentrado": proc.tipoConcentrado,
                        "descripcionProcedimiento": proc.descripcionProcedimiento,
                        "observaciones": proc.observaciones,
                        "fecha": proc.fecha.strftime("%Y-%m-%d %H:%M:%S"),
                    }
                    for proc in procedimientos
                ]
            }
            return Response(data)
