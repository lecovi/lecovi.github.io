#!/bin/bash

CMD="docker run --name nikola-lecovi --rm -ti "

if [ -z $1 ]; then
    NIKOLA_CMD="auto"
else
    NIKOLA_CMD=$1
fi

if [ $NIKOLA_CMD != "help" ]
then
    if [ -z $2 ]
    then 
        PORT=8000 
    else
        PORT=$2
    fi
    CMD+="-v $PWD/mis:/nikola "
    CMD+="-p $PORT:$PORT "
fi

CMD+="dragas/nikola "
CMD+="nikola $NIKOLA_CMD "

if [ $NIKOLA_CMD = "help" ]
then
    CMD+="$2 "
fi

if [ $NIKOLA_CMD = "auto" ]; then
    CMD+="--address 0.0.0.0 "
    CMD+="--port $PORT"
fi

echo "$CMD"
$CMD