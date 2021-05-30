#!/usr/bin/env bash

if [[ ! "$(python3 -V)" =~ "Python 3" ]]
then
  echo "Missing python3, please install python3 first"
  exit 1
fi

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

function do_clean_dummy_resource() {
  rm -rf build dist
}

case "$1" in
  "build") do_build ;;
  "test") do_test ;;
  "install") do_install_requirement ;;
  "clean" do)do_clean_dummy_resource ;;
esac

deactivate