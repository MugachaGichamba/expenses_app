from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TenantSerializer
from .models import Tenant


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'EndPoint': '/notes/',
            'method': 'GET',
            'body': 'None',
            'description': 'Returns an array of notes',
        },
        {
            'EndPoint': '/notes/id',
            'method': 'GET',
            'body': 'None',
            'description': 'Returns a single notes object',
        },
        {
            'EndPoint': '/notes/create',
            'method': 'POST',
            'body': '{body: ""}',
            'description': 'jugjghkj kjhikuh',

        },
        {
            'EndPoint': '/notes/id/update',
            'method': 'PUT',
            'body': '{body: ""}',
            'description': 'jugjghkj kjhikuh',

        },
        {
            'EndPoint': '/notes/id/delete',
            'method': 'POST',
            'body': '{body: ""}',
            'description': 'jugjghkj kjhikuh',

        }
    ]

    return Response(routes)

@api_view(['GET'])
def getTenants(request):
    tenants = Tenant.objects.all()
    serializers = TenantSerializer(tenants, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def getTenant(request, pk):
    tenant = Tenant.objects.get(id=pk)
    serializers = TenantSerializer(tenant, many=False)
    return Response(serializers.data)

@api_view(['POST'])
def createTenant(request):
    # data = request.data
    # tenant = Tenant.objects.create(
    #     first_name=data['first_name'],
    #     last_name=data['last_name'],
    #     phone_number=data['phone_number'],
    #     rent_per_month=data['rent_per_month']
    #
    # )
    serializer = TenantSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateTenant(request,pk):
    # data = request.data
    tenant = Tenant.objects.get(id=pk)

    # tenant = Tenant.objects.create(
    #     first_name=data['first_name'],
    #     last_name=data['last_name'],
    #     phone_number=data['phone_number'],
    #     rent_per_month=data['rent_per_month']
    #
    # )

    serializer = TenantSerializer(instance=tenant, data=request.data)
    if serializer.is_valid():
        print(serializer)
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteTenant(request,pk):

    tenant = Tenant.objects.get(id=pk)
    tenant.delete()
    return Response("item succesfully deleted")