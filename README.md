# yearly_patching_scheduler_calendar
Project to generate a yearly schedule for patching based on agreed offset.

Our patching schedule is currently designed as an offset to follow Microsofts Patch Tuesday, this project will create a monthly offset schedule for the year. 
The output of which can be fed to generate scheduling for downstream services.

## Schedule:
Microsoft Patch Tuesday - 2nd Tuesday of every month

Non Production day - Thursday after Patch Tuesday

Production patching - 2nd week following Patch Tuesday (client agreed day within the week).


