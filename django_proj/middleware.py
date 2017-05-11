from datetime import datetime
from django_app.models import RequestStat
from django.utils import timezone
from django.db.models import Q

class RequestStatMiddleware(object):

    def process_request(self,request):
        time_request = timezone.now()#.strftime("%Y-%m-%d %H:%M:%S")
        line_request = str(request.method) + " " \
            + str(request.get_full_path()) + " " \
            + str(request.META['SERVER_PROTOCOL'])

        request_stat = RequestStat(
            line = line_request,
            time = time_request,
            is_new = True,
        )
        request_stat.save()
        # print 'request'
        return None

    def process_response(self, request, response):
        # print 'response'
        return response
