from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from scheduler.models import TimeSlot
from scheduler.utils import find_common_timeslots


class TimeSlotView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """
        API to add available time slots
        @param request:
        @return:
        """
        try:
            start_time = request.data.get('start_time', None)
            end_time = request.data.get('end_time', None)
            if start_time and end_time:
                user = request.user
                # Convert the string to datetime format
                start_date_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
                end_date_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

                # end_time should be greater than the start_time
                if end_date_time > start_date_time:
                    time_slot = TimeSlot(user=user, start_time=start_date_time, end_time=end_date_time)
                    time_slot.save()

                    return Response(
                        data={"success": True, "message": "Successfully saved available time slot", "data": {}})
                else:
                    return Response(
                        data={"success": False,
                              "message": "Invalid parameter, end time should be greater than start time", "data": {}})

            return Response(data={"success": False,
                                  "message": """
                                            Invalid arguments, 
                                            please provide start_time and end_time in %Y-%m-%d %H:%M:%S format
                                            """,
                                  "data": {}})
        except Exception as e:
            print("Error while saving available time slot")
            print(e)
            return Response(data={"success": False, "message": "Failed to save available time slot", "data": {}})


class AvailableTimeSlotView(APIView):
    def get(self, request):
        """
        API to fetch the available interview timeslots
        @param request:
        @return:
        """
        try:
            candidate_id = request.GET.get('candidate_id')
            interviewer_id = request.GET.get('interviewer_id')

            # fetch available time slots of candidate and interviewer
            time_slots = TimeSlot.objects.filter(user__in=[candidate_id, interviewer_id]).all()

            available_timeslots = find_common_timeslots(time_slots)

            return Response(
                data={"success": True, "message": "Successfully fetched common available interview timeslots",
                      "data": available_timeslots})
        except Exception as e:
            print("Error while fetching available time slots")
            print(e)
            return Response(data={"success": True, "message": "Something went wrong!!", "data": {}})


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
