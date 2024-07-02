from .serializers import RouteSerializer, OriginSerializer, DestinationSerializer, instanceSerializer, UserSerializer
from rest_framework import permissions, viewsets
from route import models
from django.contrib.auth.models import User 

class RouteSerializerViewSet(viewsets.ModelViewSet):

    queryset = models.Route.objects.all().order_by('-preparation_date')
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        
        if self.request.method == 'GET':
            
            query_p = self.request.GET.get('p', None)
            
            query_c = self.request.GET.get('c', None)
            
            if query_p is not None:
                
                state, origin_id= query_p.split('!')
                
                if origin_id == 'all':
                    
                    return models.Route.objects.filter(status= state)
                
                else:
                
                    return models.Route.objects.filter(status= state).filter(origin= origin_id)
            
            elif query_c is not None:
                
                state, destination_id= query_c.split('!')
                
                if destination_id == 'all':
                    
                    return models.Route.objects.filter(status= state)
                
                else:
                
                    return models.Route.objects.filter(status= state).filter(destination= destination_id)
            
            
            else:
                queryset = models.Route.objects.all().order_by('-preparation_date')
                return queryset

        else:
            queryset = models.Route.objects.all().order_by('-preparation_date')
            return queryset

class InstanceSerializerViewSet(viewsets.ModelViewSet):

    queryset = models.RouteInstance.objects.all().order_by('route')
    serializer_class = instanceSerializer
    permission_classes = [permissions.IsAuthenticated]


class OriginSerializerViewSet(viewsets.ModelViewSet):

    queryset = models.NodeOrigin.objects.all().order_by('id')
    serializer_class = OriginSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class DestinationSerializerViewSet(viewsets.ModelViewSet):

    queryset = models.NodeDestination.objects.all().order_by('name')
    serializer_class = DestinationSerializer

    permission_classes =[permissions.IsAuthenticated]
    
class UserSerializerViewSet(viewsets.ModelViewSet):
    
    queryset= User.objects.all()
    serializer_class= UserSerializer 
    permission_classes= [permissions.IsAuthenticated]
    
    def get_queryset(self, *args, **kwargs):
        return User.objects.filter(username =self.request.user)
    

        
   
