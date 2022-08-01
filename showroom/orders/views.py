from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from orders.models import CustomerOrder, DealerOrder
from orders.serializers import CustomerOrderSerializer, ActionCustomerOrderSerializer, DealerOrderSerializer, \
    ActionDealerOrderSerializer


class CustomerOrderViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer
    permission_classes = (IsAuthenticated,)
    serializer_action_classes = {
        'create': ActionCustomerOrderSerializer
    }

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomerOrderSerializer
        else:
            return ActionCustomerOrderSerializer


class DealerOrderViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    queryset = DealerOrder.objects.all()
    serializer_class = DealerOrderSerializer
    permission_classes = (IsAuthenticated,)
    serializer_action_classes = {
        'create': ActionDealerOrderSerializer
    }

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DealerOrderSerializer
        else:
            return ActionDealerOrderSerializer
