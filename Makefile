run_test:
	cd src && python3 cmsAddParticipations.py -s thuandp -c 1 ../files/sample.xls
rebuild:
	pyinstall --onefile cmsAddUsers.py && cp dist/cmsAddUsers executable/ &&
	pyinstall --onefile cmsAddParticipations.py && cp dist/cmsAddParticipations executable