# ![Python](https://img.shields.io/badge/python-3776ab?style=for-the-badge&logo=python&logoColor=yellow) - yearly_patching_scheduler_calendar
Project to generate a yearly schedule for patching based on agreed offset.

I've worked with Microsoft Windows and Server for a number of years and no matter where we are the OS patching windows in most business tend to follow the prescribed Microsoft Patch Tuesday releases, emergency security patches not withstanding.
With this in mind it felt like a fun project to investigate and create a tool to calculate this value based on the year/month being provided.

## Status
<html>
<div style="text-align: centre;">
<img alt="GitHub Tag" src="https://img.shields.io/github/v/tag/roblangford/yearly_patching_scheduler_calendar?style=for-the-badge&logo=github">
<img alt="GitHub Issues Open" src="https://img.shields.io/github/issues-raw/roblangford/yearly_patching_scheduler_calendar?style=for-the-badge&logo=github">
<img alt="GitHub Issues Closed" src="https://img.shields.io/github/issues-closed-raw/roblangford/yearly_patching_scheduler_calendar?style=for-the-badge&logo=github">
</div>
</html>

![pylint]()

## Investigation

I had used an excel spreadsheet to perform calculations and worked out the there was a standard offset. Say if the first Day of the month was a Tuesday, then logically the second Tuesday (a.k.a Patch Tuesday) would be 7 days later (the 8th day). If the first day of the month fell on Monday, then the second Tuesday was 8 days later (the 9th day), this trend continues until we are back to Tuesday again..  

So with this in mind I would simply need to determine the day of the week that the first day of the Month fell on in order then use the offset to determine the numeric date that Patch Tuesday fell on.

Rather than calculate this I defined an offset dictionary in order to associate the day of the week with a numeric date that could be returned by a simple lookup.  

| day 1st of the month | Patch Tuesday date |
|-----|------|
| Wednesday | 14th |
| Thursday | 13th |
| Friday | 12th |
| Saturday | 11th |
| Sunday | 10th |
| Monday | 9th |
| Tuesday | 8th |

This would logically work for any similar offset based around an agreed window (e.g. 3rd Thursday), however you may end up rolling over to the following Month in some scenarios.  

## Program
```bash
python3 patch_tuesday.py
```

The program can be executed in a number of ways, if you simply start the program with no input variables, as above, you will be prompted for input values for the Year and Month.  
A formatted response will return the informatiln.

```bash
python3 patch_tuesday.py <YEAR>
```

If you input a single attribute this is assumed to be the year. The program will then provide all of the Patch Tuesday calculations for that year. Returning a formatted list output.

```bash
python3 patch_tuesday.py <YEAR> <MONTH>
```

If you provide two inputs at the command line during execution the first again is assumed to be the Year, and the second a Month. The month is validated and a relevant error message returned if not.
Similar to the prompted execution when not providing any values at cli execution a formatted response will return the Patch Tuesday information.

## Dependencies

![pylint]()  
![python]()  
