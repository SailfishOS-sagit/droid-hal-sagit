%define device sagit
%define vendor xiaomi
%define vendor_pretty Xiaomi
%define device_pretty Mi 6 (sagit)
%define installable_zip 1
%define droid_target_aarch64 1

# Fixes WebBrowser crashes
%define android_config \
#define WANT_ADRENO_QUIRKS 1 \
%{nil}

%define straggler_files \
/bugreports\
/cache\
/d\
/sdcard\
%{nil}

%define makefstab_skip_entries /dev/stune /dev/cpuset /sys/fs/pstore /dev/cpuctl

%include rpm/dhd/droid-hal-device.inc
