# from rest_framework import serializers
# from .models import StaffSection, StaffMember

# class StaffMemberSerializer(serializers.ModelSerializer):
#     name = serializers.CharField(source='full_name')
#     class Meta:
#         model = StaffMember
#         fields = ['name', 'role', 'img']  # Include all fields from the StaffMember model

# class StaffSectionSerializer(serializers.ModelSerializer):
#     # Define a nested serializer for the 'members' field
#     members = StaffMemberSerializer(many=True, read_only=True)
    
#     class Meta:
#         model = StaffSection
#         fields = '__all__' 
