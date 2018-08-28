# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).
#
# print 2 ** 10      # one kilobit, kb
# print 2 ** 10 * 8  # one kilobyte, kB
#
# print 2 ** 20      # one megabit, Mb
# print 2 ** 20 * 8  # one megabyte, MB
#
# print 2 ** 30      # one gigabit, Gb
# print 2 ** 30 * 8  # one gigabyte, GB
#
# print 2 ** 40      # one terabit, Tb
# print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).


def download_time(filesize, fileUnit, BandWidth, BandWiddthUnit):
    bits = {'kb': 1024, 'kB': 8192, 'Mb': 1048576, 'MB': 8388608, 'Gb': 1073741824,
            'GB': 8589934592, 'Tb': 1099511627776, 'TB': 8796093022208}

    filesize_bits = filesize * bits[fileUnit]
    bandwidth_bits = BandWidth * bits[BandWiddthUnit]

    # download time in seconds
    download_time = filesize_bits / bandwidth_bits

    # converting download_time into hour minute and seconds mark
    hours, m = divmod(download_time, 3600)  # int(download_time/3600)
    minutes,m1 = divmod(m, 60)  # int((download_time%3600)/60)
    seconds = m % 60

    time = ''

    if hours == 1:
        time = time + str(int(hours)) + " hour, "
    else:
        time = time + str(int(hours)) + " hours, "

    if minutes == 1:
        time = time + str(int(minutes)) + " minute, "
    else:
        time = time + str(int(minutes)) + " minutes, "

    if seconds == 1:
        time = time + str(seconds) + " second"
    else:
        time = time + str(seconds) + " seconds"

    return time


print download_time(1024, 'kB', 1, 'MB')
# >>> 0 hours, 0 minutes, 1 second

print download_time(1024, 'kB', 1, 'Mb')
# >>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13, 'GB', 5.6, 'MB')
# >>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13, 'GB', 5.6, 'Mb')
# >>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10, 'MB', 2, 'kB')
# >>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10, 'MB', 2, 'kb')
# >>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable
