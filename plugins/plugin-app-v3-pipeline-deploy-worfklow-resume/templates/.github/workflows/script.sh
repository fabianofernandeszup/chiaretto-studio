COMMIT_MSG="First Commit StackSpot (Execution_id:01JMQ1GV93SJPXX174YVY5BY24,Job_id:job_suspend_dev_deploy)"
COMMIT_MSG="First Commit StackSpot"

GITHUB_OUTPUT=""

# Extrair Execution_id (combinação de letras e números)
EXECUTION_ID=$(echo "$COMMIT_MSG" | grep -oP 'Execution_id:\K[a-zA-Z0-9]+')

# Extrair Job_id (combinação de letras e números)
JOB_ID=$(echo "$COMMIT_MSG" | grep -oP 'Job_id:\K[a-zA-Z0-9-_]+')

# Validação rigorosa
if [ -z "$EXECUTION_ID" ]; then
  echo "::error::Execution_id não encontrado ou inválido!"
else
  echo "EXECUTION_ID=${EXECUTION_ID}" >> $GITHUB_OUTPUT
fi

if [ -z "$JOB_ID" ]; then
  echo "::error::Job_id não encontrado ou inválido!"
else
  echo "JOB_ID=${JOB_ID}" >> $GITHUB_OUTPUT
fi


print $GITHUB_OUTPUT
