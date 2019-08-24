from django.test import TestCase


from jdatetime import date as jdate

salon_instance = get_object_or_404(SalonModel,pk = pk)
if request.user == salon.sportclub.user:
    sessions = get_list_or_404(SessionModel,salon = salon_instance)

    first_day = sessions.order_by('day')[0].day
    last_day = sessions.order_by('day')[-1].day

    counter = 0
    while True:
        if counter == 0:
            now = first_day
            if now.month == 12:
                month_length =  (jdate(now.year+1, 1, 1) - jdate(now.year, 12, 1)).days
                previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year, now.month-1, 1)).days
                this_date = str(now.year)+'-12-'
                next_date = str(now.year+1)+'-1-'
                prev_date = str(now.year)+'-11-'
            elif now.month == 1:
                month_length =  (jdate(now.year, now.month+1, 1) - jdate(now.year, now.month, 1)).days
                previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year-1, 12, 1)).days
                this_date = str(now.year)+'-1-'
                next_date = str(now.year)+'-2-'
                prev_date = str(now.year-1)+'-12-'
            else:
                month_length =  (jdate(now.year, now.month+1, 1) - jdate(now.year, now.month, 1)).days
                previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year, now.month-1, 1)).days
                this_date = str(now.year)+'-'+str(now.month)+'-'
                next_date = str(now.year)+'-'+str(now.month+1)+'-'
                prev_date = str(now.year)+'-'+str(now.month-1)+'-'

            first_day_of_month_weekday = jdate(now.year, now.month, 1).weekday()
            array = [0,]
            days = [0,]
            if (month_length == 30 and first_day_of_month_weekday == 6) or (month_length == 31 and first_day_of_month_weekday >=5):
                for i in range(41):
                    array.append(0)
                    days.append(0)
            else:
                for i in range(34):
                    array.append(0)
                    days.append(0)


            for i in range(first_day_of_month_weekday):
                array[first_day_of_month_weekday-i-1] = prev_date + '' #str(previous_month_length - i)

            for i in range(month_length):
                array[first_day_of_month_weekday+i] = this_date + str(i + 1)

            for i in range(len(array) - array.index(0)):
                array[array.index(0)] = next_date+ '' #str(i+1)
            for i in range(len(array)):
                days[i] = array[(int(i/7)+1)*7-1-(i-int(i/7)*7)]
            for i in range(len(days)):
                if int((i)/7) == ((i)/7):
                    days[i] = days[i]+'-br'
            dictoinary = {'days_0':days,}
            counter = 1
            if now.year == last_day.year and now.month == last_day.month:
                break
        else:
            now = jdate(now.year,now.month,15)+timedelta(days=30)
            if now.month == 12:
                month_length =  (jdate(now.year+1, 1, 1) - jdate(now.year, 12, 1)).days
                previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year, now.month-1, 1)).days
                this_date = str(now.year)+'-12-'
                next_date = str(now.year+1)+'-1-'
                prev_date = str(now.year)+'-11-'
            elif now.month == 1:
                month_length =  (jdate(now.year, now.month+1, 1) - jdate(now.year, now.month, 1)).days
                previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year-1, 12, 1)).days
                this_date = str(now.year)+'-1-'
                next_date = str(now.year)+'-2-'
                prev_date = str(now.year-1)+'-12-'
            else:
                month_length =  (jdate(now.year, now.month+1, 1) - jdate(now.year, now.month, 1)).days
                previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year, now.month-1, 1)).days
                this_date = str(now.year)+'-'+str(now.month)+'-'
                next_date = str(now.year)+'-'+str(now.month+1)+'-'
                prev_date = str(now.year)+'-'+str(now.month-1)+'-'

            first_day_of_month_weekday = jdate(now.year, now.month, 1).weekday()
            array = [0,]
            days = [0,]
            if (month_length == 30 and first_day_of_month_weekday == 6) or (month_length == 31 and first_day_of_month_weekday >=5):
                for i in range(41):
                    array.append(0)
                    days.append(0)
            else:
                for i in range(34):
                    array.append(0)
                    days.append(0)


            for i in range(first_day_of_month_weekday):
                array[first_day_of_month_weekday-i-1] = prev_date + '' #str(previous_month_length - i)

            for i in range(month_length):
                array[first_day_of_month_weekday+i] = this_date + str(i + 1)

            for i in range(len(array) - array.index(0)):
                array[array.index(0)] = next_date+ '' #str(i+1)
            for i in range(len(array)):
                days[i] = array[(int(i/7)+1)*7-1-(i-int(i/7)*7)]
            for i in range(len(days)):
                if int((i)/7) == ((i)/7):
                    days[i] = days[i]+'-br'
            dictoinary['days_{first}'.format(first = str(counter))]
            counter += 1
            if now.year == last_day.year and now.month == last_day.month:
                break
    return render(request,'session/sessionlist.html',dictoinary)
