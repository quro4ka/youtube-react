from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from mailing.models import ChannelMailingList
from video_hosting.models import Channel, Subscribers



# Create your views here.
class MailViewSet(viewsets.ViewSet):
	permission_classes = (permissions.IsAuthenticated,)

	@action(detail=True, methods=['get', 'post', 'delete'])
	def mail(self, request, pk=None):
		obj = ChannelMailingList.objects.filter(user=request.user, channel=pk)[:1]
		stat = not not obj
		if request.method == "GET":
			return Response({"status": stat})
		elif request.method == "POST":
			is_subscribe = Subscribers.objects.filter(user=request.user, channel=pk).exists()
			if not stat and is_subscribe:
				ChannelMailingList.objects.create(user=request.user, channel=get_object_or_404(Channel, pk=pk))
			else:
				return Response({'detail': "user is not subscribed"}, status=status.HTTP_403_FORBIDDEN )
		elif request.method == "DELETE":
			if stat:
				obj[0].delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
