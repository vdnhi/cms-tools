#!/usr/bin/env bash

if [[ ! -d venv ]]
then
  python3 -m venv venv
fi

source venv/bin/activate

function do_build() {
  rm -rf build dist
  pyinstaller --onefile src/cmsAddUsers.py
  pyinstaller --onefile src/cmsAddParticipations.py
  cp dist/cmsAddUsers executable
  cp dist/cmsAddParticipations executable
}

function do_test() {
  python3 src/cmsAddParticipations.py -s thuandp -c 1 ../files/sample.xls
}

function do_install_requirement() {
  if [[ -d ./venv ]]
  then
    pip3 install -r requirements.txt
  fi
}

case "$1" in
  "build") do_build ;;
  "test") do_test ;;
  "install") do_install_requirement ;;
esac

deactivate