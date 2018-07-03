#!/usr/bin/python
# -*- coding: utf-8 -*-

NEW_MOON = "🌑"
new_moon_count = 0

WAXING_CRESCENT = "🌒"
waxing_crescent_count= 0

FIRST_QUARTER = "🌓"
first_quarter_count = 0

WAXING_GIBBOUS = "🌔"
waxing_gibbous_count = 0

FULL_MOON = "🌕"
full_moon_count = 0

WANING_GIBBOUS = "🌖"
waning_gibbous_count = 0

LAST_QUARTER = "🌗"
last_quarter_count = 0

WANING_CRESCENT = "🌘"
waning_crescent_count = 0

total_moons_found = 0

members_with_multiple_moons = 0
members_with_no_moons = 0
lines_parsed = float(0)

with open('members.txt') as f:
    for line in f:
        moons_found = 0
        if NEW_MOON in line:
            moons_found += 1
            new_moon_count += 1
        if WAXING_CRESCENT in line:
            moons_found += 1
            waxing_crescent_count += 1
        if FIRST_QUARTER in line:
            moons_found += 1
            first_quarter_count += 1
        if WAXING_GIBBOUS in line:
            moons_found += 1
            waxing_gibbous_count += 1
        if FULL_MOON in line:
            moons_found += 1
            full_moon_count += 1
        if WANING_GIBBOUS in line:
            moons_found += 1
            waning_gibbous_count += 1
        if LAST_QUARTER in line:
            moons_found += 1
            last_quarter_count += 1
        if WANING_CRESCENT in line:
            moons_found += 1
            waning_crescent_count += 1
        total_moons_found += moons_found
        if moons_found == 0:
            members_with_no_moons += 1
        elif moons_found > 1:
            members_with_multiple_moons += 1
        lines_parsed += 1

print('Member Statistics for Gore And HardVore')
print('Total Moons: {}'.format(total_moons_found))
print('Total Members: {}'.format(int(lines_parsed)))
print('(that\'s {:0.2f}% of Super Mario Odessey!)'.format(float(total_moons_found)/999*100))

print('{}: {:0.2f}%'.format(NEW_MOON, new_moon_count/lines_parsed*100))
print('{}: {:0.2f}%'.format(WAXING_CRESCENT, (waxing_crescent_count + waning_crescent_count )/lines_parsed*100))
print('{}: {:0.2f}%'.format(FIRST_QUARTER, (first_quarter_count + last_quarter_count)/lines_parsed*100))
print('{}: {:0.2f}%'.format(WAXING_GIBBOUS, (waxing_gibbous_count + waning_gibbous_count)/lines_parsed*100))
print('{}: {:0.2f}%'.format(FULL_MOON, full_moon_count/lines_parsed*100))
#print('{}: {:0.2f}%'.format(WANING_GIBBOUS, waning_gibbous_count/lines_parsed*100))
#print('{}: {:0.2f}%'.format(LAST_QUARTER, last_quarter_count/lines_parsed*100))
#print('{}: {:0.2f}%'.format(WANING_CRESCENT, waning_crescent_count/lines_parsed*100))

print('{} had more than one moon! Whoa!'.format(members_with_multiple_moons))
print('{} didn\'t have any moons :| get with the program'.format(members_with_no_moons))
