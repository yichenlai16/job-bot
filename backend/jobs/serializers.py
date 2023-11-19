from rest_framework import serializers

from .models import Jobs, Companys, CompanySource



class SourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanySource
        fields = '__all__'




class JobSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    company_name = serializers.CharField(source='company.name')
    class Meta:
        model = Jobs
        fields = '__all__'

class CompanyDetailSerializer(serializers.ModelSerializer):
    job = JobSerializer(source='get_jobs',many=True,read_only=True)
    class Meta:
        model = Companys
        fields ='__all__'
