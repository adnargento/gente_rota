# Updates the package list first
sudo pacman -Sy

# Installs Apertium development package and language packs for Spanish, English, Portuguese, Croatian, and Japanese
#sudo pacman -S apertium-all-dev apertium-es apertium-en apertium-pt apertium-hr apertium-ja

sudo pamac install apertium apertium-spa apertium-eng apertium-es-pt apertium-fr-es apertium-hbs apertium-hbs-eng apertium-hbs-mkd apertium-hbs-slv apertium-ita apertium-mkd-eng apertium-pol apertium-por apertium-recursive apertium-regtest 
