
if [ $# -eq 0 ]
  then
    echo "Usage : start.sh <CONTROLLER_IP> [<CONTROLLER_PORT>]"
    exit
fi

CONTROLLER_IP=${1}

if [ -z "$2" ]
  then
    CONTROLLER_PORT=${2}
else
  CONTROLLER_PORT=7820
fi

CONTROLLER_PORT
AGENT_OPTS="$AGENT_OPTS -javaagent:prismo_agent_jdk11.jar"
AGENT_OPTS="$AGENT_OPTS -Dprismo.agent.log_file=logs/prismoagent.log"
AGENT_OPTS="$AGENT_OPTS -Dprismo_application_entity=\"Unix|Default Project|Spring - Hello World|Java 11|Engineering Org\""
AGENT_OPTS="$AGENT_OPTS -Dprismo.agent.log_level=DEBUG -Dprismo_controller_host=${CONTROLLER_IP} -DPrismo_controller_port=${CONTROLLER_PORT}"

echo
echo
echo
echo $AGENT_OPTS
echo
echo
echo

./mvnw clean spring-boot:run -Dspring-boot.run.jvmArguments="$AGENT_OPTS"