#!/bin/sh

export PASSPHRASE= <insert PASSPHRASE here>

# Begin Minecraft data backup (1-2 GB)

# Stop minecraft server container
# Rsync
# Restart minecraft server container
lxc file pull\
    minecraft/home/minecraft\
    minecraft/home/ian\
    /home/ian/backup/minecraft_backup --recursive

duplicity\
    /home/ian/backup/minecraft_backup\
    rsync://NAS//mnt/sdb2/minecraft_data

rm -r /home/ian/backup/minecraft_backup/*
# End Minecraft data backup



# Stop HomeAssistant server container
# Stop HomeAssistant Snap service
# Rsync
# Restart HomeAssistant server container
# Restart HoomeAssistant Snap service

# Begin HomeAssistant data backup
lxc file pull\
    home-assistant/home/homeassistant\
    home-assistant/home/ian\
    /home/ian/backup/home_assistant_backup --recursive

duplicity\
    /home/ian/backup/home_assistant_backup\
    rsync://NAS//mnt/sdb2/home_assistant_data

rm -r /home/ian/backup/home_assistant_backup/*
# End HomeAssistant data backup

# Begin server backup
duplicity \
    --exclude /home/.cache\
    --include /home\
    --exclude '**'\
    /\
    rsync://NAS//mnt/sdb2/saitama_server

# End server backup


unset PASSPHRASE

exit 0
