from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# from boys.models import StaffSection
# from boys.serializers import StaffMemberSerializer

class Ping(APIView):
    
    def get(self, request):
        return Response({"message": "PONG"}, status=status.HTTP_200_OK)



@api_view(['GET'])
def echo(request, msg):
    return Response({"you said": msg}, status=status.HTTP_200_OK)

# @api_view(['GET'])
# def get_all_staff(request):
#     # Get all StaffSections
#     staff_sections = StaffSection.objects.all()
    
#     # Serialize the data
#     data = []
#     for section in staff_sections:
#         section_data = {
#             "name": section.name,
#             "peoples": StaffMemberSerializer(section.members.all(), many=True).data
#         }
#         data.append(section_data)
    
#     # Create the JSON file content
#     json_content = {"sections": data}
    
#     # Serialize to JSON and return as a response
#     response = JsonResponse(json_content, safe=False, json_dumps_params={'indent': 2})
    
#     # Set content type and attachment disposition for download
#     response['Content-Disposition'] = 'attachment; filename="staff_data.json"'
#     response['Content-Type'] = 'application/json'
    
#     return response