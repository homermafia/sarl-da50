#!/usr/bin/env bash

if [ -z "$MAVEN_CMD" ]
then
	MAVEN_CMD="mvn"
fi

if test "${TRAVIS_EVENT_TYPE}" != 'cron'
then

	if test -z "$MAVEN_COMPILATION_OPTS"
	then
		echo "No Maven setting file in MAVEN_COMPILATION_SETTING" 2>&1
		exit 255
	fi

	exec "$MAVEN_CMD" -B $MAVEN_COMPILATION_OPTS -DMAVENSARLIO_URL="$MAVENSARLIO_URL" -DUPDATESSARLIO_URL="$UPDATESARLIO_URL" -DDEPENDENCIESSARLIO_URL="$DEPENDENCIESSARLIO_URL" clean install


else

	echo "[WARNING] The compilation is enabled only outside a cron task."

fi

exit 0

