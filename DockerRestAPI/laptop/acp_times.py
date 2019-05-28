"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#Lists used to calculate open and close times
#defined here in case the rules change in the future
dist=[600,400,200,0]
maxSpeed = [28,30,32,34]
minSpeed = [11.428,15,15,15]
closeTime = {1000: 75, 600: 40, 400: 27, 300: 20, 200: 13.5}


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """

    if (brevet_dist_km * 1.2 < control_dist_km):
      return ""

    try:
      time = arrow.get(brevet_start_time)
    except:
      return ""

    if(control_dist_km == 0):
      return time.format()

    control_dist_km = min(brevet_dist_km, control_dist_km)
    hours = 0.0

    for i in range(4):
      d = dist[i]
      if(control_dist_km > d):
        x = control_dist_km - d
        hours += x/maxSpeed[i]
        control_dist_km = control_dist_km - x

    minutes = (hours*60) % 60
    hours = int(hours)
    minutes = round(minutes)
    time = time.shift(hours=hours, minutes=minutes)

    return time.format()


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """

    if (brevet_dist_km * 1.2 < control_dist_km):
      return ""

    try:
      time = arrow.get(brevet_start_time)
    except:
      return ""

    if(control_dist_km == 0):
      time = time.shift(hours=1)
      return time.format()

    control_dist_km = min(brevet_dist_km, control_dist_km)
    hours = 0.0

    if(control_dist_km == brevet_dist_km):
      hours = closeTime[brevet_dist_km]

    else:
      for i in range(4):
        d = dist[i]
        if(control_dist_km > d):
          x = control_dist_km - d
          hours += x/minSpeed[i]
          control_dist_km = control_dist_km - x

    minutes = (hours*60) % 60
    hours = int(hours)
    minutes = round(minutes)
    time = time.shift(hours=hours, minutes=minutes)

    return time.format()
