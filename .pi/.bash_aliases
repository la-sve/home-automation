# lasve alias-definitions
# -----------------------
alias ll='ls -lah'

#alias arduino='~/Downloads/arduino-1.8.7/arduino'
alias su_hass='sudo -u homeassistant -H -s'

# Backup Home Assistant Properties
alias hass_backup='sudo -u homeassistant -H -s bash -c "cd /home/homeassistant; zip -r $(date +%y%m%d)_back.zip .homeassistant"'

# Log Output von Home Assistant
alias hass_log='sudo journalctl -f -u home-assistant@homeassistant.service'
alias hass_tmux='sudo -H -u homeassistant bash -c "tmux a"'
alias hass_start='sh ~/hass_autostart.sh'

# Use git for configuration files within home directory
# (use sparse checkout and see github documentation of la-sve/home-automation )
alias githass='git --work-tree=/home/homeassistant --git-dir=/home/homeassistant/.home'

# Rollo Steuerung
alias rollo_log='journalctl --user-unit rolloctl.service'
alias rollo_status='systemctl --user status rolloctl.service'
