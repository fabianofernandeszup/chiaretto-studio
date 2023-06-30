errors=()
exitcode=0
publish=""
publish=$(stk-alpha publish action --studio chiaretto-studio)
exitcode=$?
if [[ "$exitcode" -ne "0" ]]; then
#    echo "has-errors=true" >> "$GITHUB_OUTPUT"
    errors=(${errors[@]} "Error on publish: ${i}")
    echo "x Error on publish!"
else
    echo "Publish successfully!"
fi