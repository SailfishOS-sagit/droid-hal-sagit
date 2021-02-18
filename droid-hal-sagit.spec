%define device sagit
%define vendor xiaomi
%define vendor_pretty Xiaomi
%define device_pretty Mi 6 (sagit)
%define installable_zip 1
%define droid_target_aarch64 1

%define straggler_files \
/bt_firmware\
/bugreports\
/d\
/persist\
/product\
/product_services\
/sdcard\
%{nil}

%include rpm/dhd/droid-hal-device.inc
